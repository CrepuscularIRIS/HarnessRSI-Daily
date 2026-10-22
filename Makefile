.PHONY: all check help score board check-log
all: check
check:
	python3 test_check_cards.py
	python3 check_cards.py
	python3 -m py_compile research/*.py
help:
	@echo "make check: offline checks; current scoring contract: research/scoring/README.md; old results withdrawn"
score board:
	@echo "Legacy scoring/board retired. read research/scoring/README.md; old results withdrawn." >&2
	@exit 2
check-log:
	uv run python check_log.py
