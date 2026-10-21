"""Seat-local atomic record writer and mechanical checks; no model calls."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path('/home/lingxufeng/ArxivDaily')
OUT = Path(__file__).parent
MANIFEST = json.loads((ROOT / 'research/v2/runs/rsi-v22-20261021-01/batches/r04b/manifest.json').read_text())
WEIGHTS = dict(zip(['G', 'M', 'X', 'E.measurement', 'E.causality', 'E.holdout', 'E.statistics', 'E.cost'], [15, 20, 20, 10, 15, 10, 5, 5]))


def emit(key: str, claim: str, evidence: list, signatures: list, gap: dict,
         rs: list, domains: list, expectations: list, claims: list,
         assessment: dict, ratings: list, rationale: str) -> None:
    detail = next(x for x in MANIFEST['paper_details'] if x['paper_key'] == key)
    material = detail['material']
    text = (ROOT / material['text_path']).read_text()
    assert hashlib.sha256((ROOT / material['text_path']).read_bytes()).hexdigest() == material['sha256']
    ev = []
    for i, (locator, quote, explanation) in enumerate(evidence, 1):
        assert quote in text, (key, i, quote)
        ev.append(dict(evidence_id=f'E{i:03}', material_id=key + '.txt', sha256=material['sha256'], locator=locator, quote=quote, support_explanation=explanation, kind='author_report'))
    items = {}
    for item, value in zip(WEIGHTS, ratings):
        rating, reason, ids, scope = value
        status = 'unknown' if rating is None else ('not_reported' if rating == 0 and scope else 'resolved')
        items[item] = dict(status=status, rating=rating, reason=reason, evidence_ids=ids, counterevidence_ids=[], search_scope=scope)
    lower = sum(WEIGHTS[k] * v['rating'] / 4 for k, v in items.items() if v['rating'] is not None)
    coverage = sum(WEIGHTS[k] for k, v in items.items() if v['rating'] is not None) / 100
    upper = lower + sum(WEIGHTS[k] for k, v in items.items() if v['rating'] is None)
    score = dict(raw=lower if coverage == 1 else None, display=round(lower, 1) if coverage == 1 else None, lower=lower, upper=upper, coverage=coverage, rubric_hash=MANIFEST['rubric']['sha256'])
    record = dict(schema_version='radar-review-v2.2', run_id=MANIFEST['run_id'], batch_id='r04b', attempt_id='a1', seat='sol', status='reviewed', reason='完整固定正文和附录已读；证据局限与作者未报告事项按冻结锚点评定，不以未报告冒充材料缺失。',
        paper=dict(paper_key=key, paper_id=detail['arxiv'], title=detail['title'], version=detail['version'], claim_type='system_method', central_claim=claim),
        provenance=dict(input_hash=MANIFEST['input_hash'], rubric_version='frozen-v1.0', rubric_hash=MANIFEST['rubric']['sha256'], rs_manifest_hash=MANIFEST['assets']['rs_manifest']['sha256'], domain_cards_hash=MANIFEST['assets']['domain_cards_dir']['sha256'], expectations_hash=MANIFEST['assets']['domain_conditions']['sha256'], model_type='sol(gpt-6.1-sol)', actual_model=None, session_id=None, receipt_ref=None, notes='任务与环境声明实际模型为 gpt-6.1-sol；无独立运行回执或可验证模型/session标识，按模板保留 null，未额外探测。', timestamp=datetime.now(timezone.utc).isoformat()),
        materials=[dict(material_id=key+'.txt', url=material['source_url'], version=detail['version'], sha256=material['sha256'], sections_read=['全文：摘要、引言、相关工作、方法、实验、结论/局限及材料内全部附录'], complete=True, missing_sections=[])], evidence=ev, signatures=signatures, gap=gap,
        rs_pattern=dict(primary=rs[0]['main_id'] if rs else None, supporting=[x['main_id'] for x in rs[1:]], matches=rs, outside_taxonomy=not bool(rs), reason='按操作及条件而非术语匹配；匹配不直接计分。', executes_pattern=bool(rs), resolves_problem=False),
        domain_pattern=dict(namespace='rsi', matches=domains, unassigned=not bool(domains), revision_proposals=[]),
        pattern_mapping=[dict(rs_main=r['main_id'], rs_sub=r['sub_id'], domain=dict(namespace='rsi', main=d['main'], sub=d['sub']), operation_correspondence=d['fit'], necessary_conditions_and_differences='冻结模型下持久化非权重产物并在后续任务读取；结构性匹配不等于因果、留出或长期可靠性已证。', evidence_ids=d['evidence_ids']) for r in rs[:1] for d in domains],
        expectations=expectations, claims=claims, assessment=assessment, ratings=items, score=score, rationale=rationale)
    known = {e['evidence_id'] for e in ev}
    def check_refs(obj: object) -> None:
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k in ('evidence_ids', 'counterevidence_ids'):
                    assert set(v) <= known, (k, v)
                check_refs(v)
        elif isinstance(obj, list):
            for v in obj:
                check_refs(v)
    check_refs(record)
    parents = dict(line.split('\t') for line in (ROOT/'research/reference/researchstudio-15-31/PARENTS.tsv').read_text().splitlines()[1:] if line)
    for r in rs:
        assert r['sub_id'] is None or parents[r['sub_id']] == r['main_id']
    for exp in expectations:
        assert exp['id'].startswith(('rs:', 'rsi:', 'local:'))
    target = OUT / (key + '.json')
    assert not target.exists(), 'Do not overwrite completed attempt'
    tmp = target.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(record, ensure_ascii=False, indent=2) + '\n')
    json.loads(tmp.read_text())
    tmp.replace(target)


def rs(main: str, sub: str | None, reason: str, ids: list, checks: str) -> dict:
    return dict(main_id=main, sub_id=sub, role='primary', fit='strong' if sub else 'partial', tactic_steps_checked=checks, success_failure_checks=checks, evidence_ids=ids, reason=reason)


def domain(main: str, sub: str, fit: str, ids: list, checks: str) -> dict:
    return dict(main=main, sub=sub, version='manifest-frozen', fit=fit, condition_checks=checks, evidence_ids=ids)


def exp(key: str, status: str, reason: str, ids: list, item: str, source: str, applies: str) -> dict:
    return dict(id=key, version='manifest-frozen', source_strength='single_source', source_refs=[source], applies_when=applies, applicable=True, status=status, reason=reason, evidence_ids=ids, score_item=item)
