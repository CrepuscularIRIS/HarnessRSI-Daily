"""Read-only checks of this seat's five records; emit own batch report if valid."""
import csv
import hashlib
import json
import os
import re
import runpy
from pathlib import Path

ROOT = Path('/home/lingxufeng/ArxivDaily')
OUT = Path(__file__).parent
MAN = json.loads((OUT.parents[3] / 'manifest.json').read_text())
V = runpy.run_path(str(ROOT / 'research/v2/tools/rv2.py'))
IDS = V['card_ids']()


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def references(node: object, legal: set[str]) -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            if key in {'evidence_ids', 'counterevidence_ids'}:
                assert isinstance(value, list) and set(value) <= legal, (key, value)
            references(value, legal)
    elif isinstance(node, list):
        for value in node:
            references(value, legal)


def main() -> None:
    canon = V['canon']
    unbound = {k: v for k, v in MAN.items() if k != 'input_hash'}
    assert hashlib.sha256(canon(unbound).encode()).hexdigest() == MAN['input_hash']
    for key, asset in MAN['assets'].items():
        if key in {'domain_cards_dir', 'rs_cards_dir'}:
            base = ROOT / ('patterns' if key == 'domain_cards_dir' else 'research/reference/researchstudio-15-31')
            stream = b''.join(str(p.relative_to(ROOT)).encode() + p.read_bytes()
                              for p in sorted(base.rglob('*.md')))
            actual = hashlib.sha256(stream).hexdigest()
        else:
            actual = digest(ROOT / asset['path'])
        assert actual == asset['sha256'], ('asset hash mismatch', key)
    assert digest(ROOT / MAN['rubric']['path']) == MAN['rubric']['sha256']
    ref = ROOT / 'research/reference/researchstudio-15-31'
    with (ref / 'MANIFEST.tsv').open() as stream:
        for row in csv.DictReader(stream, delimiter='\t'):
            assert digest(ref / row['path']) == row['sha256'], row['path']
    tax = json.loads((ROOT / 'research/patterns/taxonomy.json').read_text())
    parents = {p['id']: p['parent'] for p in tax['sub_patterns']}
    files = sorted(p.stem for p in OUT.glob('*.json') if p.name != 'batch-report.json')
    assert files == sorted(MAN['papers']) and len(files) == len(set(files))
    records = []
    requests = []
    for paper in MAN['paper_details']:
        key = paper['paper_key']
        record = json.loads((OUT / f'{key}.json').read_text())
        errors = V['check_record'](record, IDS)
        assert not errors, (key, errors)
        assert record['run_id'] == MAN['run_id'] and record['batch_id'] == 'r01b'
        assert record['attempt_id'] == 'a1' and record['seat'] == 'sol'
        assert record['paper']['paper_key'] == key
        assert record['paper']['paper_id'] == paper['arxiv']
        assert record['paper']['version'] == paper['version']
        assert record['paper']['title'] == paper['title']
        assert record['reason'] and 0 < len(record['rationale']) <= 150
        prov = record['provenance']
        assert prov['input_hash'] == MAN['input_hash']
        assert prov['rubric_hash'] == MAN['rubric']['sha256']
        for field, asset in [('rs_manifest_hash','rs_manifest'), ('domain_cards_hash','domain_cards_dir'), ('expectations_hash','domain_conditions')]:
            assert prov[field] == MAN['assets'][asset]['sha256']
        assert prov['actual_model'] == 'gpt-6.1-sol'
        assert prov['model_type'] == 'sol(gpt-6.1-sol)'
        assert prov['notes'] and prov['session_id'] is None and prov['receipt_ref'] is None
        path = ROOT / paper['material']['text_path']
        assert digest(path) == paper['material']['sha256']
        text = path.read_text()
        materials = {m['material_id']: m for m in record['materials']}
        assert len(materials) == len(record['materials']) == 1
        material = materials['fulltext']
        assert material['sha256'] == paper['material']['sha256']
        assert material['version'] == paper['version']
        assert material['url'] == paper['material']['source_url']
        assert material['sections_read']
        evidence = record['evidence']
        legal = {e['evidence_id'] for e in evidence}
        assert len(legal) == len(evidence)
        for item in evidence:
            assert item['material_id'] in materials
            assert item['sha256'] == material['sha256']
            assert item['quote'] and item['quote'] in text
            assert item['locator'] and item['support_explanation']
            assert item['kind'] in {'author_report','our_inference','static_code_check'}
        references(record, legal)
        for match in record['rs_pattern']['matches']:
            assert 'success/failure_checks' in match and match['tactic_steps_checked']
        for match in record['domain_pattern']['matches']:
            assert match['sub'] is None or parents[match['sub']] == match['main']
            assert match['version'] and match['condition_checks']
        for expectation in record['expectations']:
            assert re.fullmatch(r'(?:rs:[^/]+/RE-[^/]+|rsi:[^/]+/(?:S\d+|F\d+|H\d+|step[^/]*?)|local:[^-]+-\d+)', expectation['id'])
            assert expectation['status'] in {'met','partial','unmet','unknown','challenged_with_evidence'}
            assert expectation['source_refs'] and expectation['reason']
            assert expectation['score_item'] in V['RATING_KEYS']
        want = V['compute_score'](record)
        if record['status'] == 'needs_fulltext':
            assert record['score'] is None and not material['complete'] and material['missing_sections']
            assert all(x['status'] == 'unknown' and x['rating'] is None for x in record['ratings'].values())
            assert record['score_interval'] == {'lower':0,'upper':100,'coverage':0}
        else:
            assert material['complete'] and not material['missing_sections']
            for field in ['raw','display','lower','upper','coverage']:
                assert record['score'][field] == want[field], (key, field)
        records.append(record)
        requests.extend({'paper_key':key,'request':q} for q in record['gap']['unresolved'])
    # Small negative fixtures verify reused checker rejects invalid rating/RS parent states.
    bad = json.loads(json.dumps(records[0]))
    bad['ratings']['G']['rating'] = 9
    assert V['check_record'](bad, IDS)
    bad = json.loads(json.dumps(records[0]))
    bad['rs_pattern']['matches'][0]['sub_id'] = 'C99'
    assert V['check_record'](bad, IDS)
    report = dict(run_id=MAN['run_id'],batch_id='r01b',attempt_id='a1',seat='sol',
                  assigned=len(records),schema_errors=0,model_type='sol(gpt-6.1-sol)',
                  actual_model='gpt-6.1-sol',session_ref=None,
                  outside_taxonomy=sum(r['rs_pattern']['outside_taxonomy'] for r in records))
    for status in ['reviewed','needs_fulltext','needs_evidence','out_of_scope']:
        report[status] = sum(r['status'] == status for r in records)
    report['notes'] = [
        'All supplied fixed texts read in full. 2407.08937 Appendix E explicitly points to missing external continuation; manifest complete=true overridden. No external fetching performed.',
        'All fixed input, file assets, RS MANIFEST members, rubric, directory aggregate hashes, paper material hashes, continuous quotes, nested evidence references, IDs, rating states and arithmetic checked locally. Directory aggregate recipe: sorted repository-relative Markdown paths concatenated with raw content bytes.',
        'Only own sol/a1 records read. Reused pure rv2 check_record/compute_score helpers, never seats/aggregate CLI; no cross-seat content, shared outputs, git operations or paper-code execution.',
        'Mechanical validation does not establish semantic truth or reproduction. Neighbor originals requested for shared package; these are gap uncertainties, not missing fulltext of the other four papers.',
        'Actual model supplied by invocation environment. No additional routing probe, session identifier or receipt available.'
    ]
    report['shared_material_requests'] = requests
    target = OUT / 'batch-report.json'
    tmp = target.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    os.replace(tmp,target)
    print(json.dumps({k:report[k] for k in ['assigned','reviewed','needs_fulltext','needs_evidence','out_of_scope','outside_taxonomy','schema_errors']}))


if __name__ == '__main__':
    main()
