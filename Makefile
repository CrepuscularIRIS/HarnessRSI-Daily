.PHONY: all check help score board check-log
all: check
check:
	python3 test_check_cards.py
	python3 check_cards.py
	python3 -m py_compile research/*.py
help:
	@echo "make check: offline checks (cards + py syntax); digest tooling archived 2026-10-22; scoring method change pending"
score board:
	@echo "Legacy scoring/board retired. v2 is draft_uncalibrated; read research/SCORE_SPEC.md." >&2
	@exit 2
check-log:
	uv run python check_log.py
