.PHONY: check
check:
	uv run ruff check .
	uv run deptry .
	uv run pyright .
