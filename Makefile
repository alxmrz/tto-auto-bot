init:
	cp -n .env.example .env

install:
	pip install -e ".[dev]"

run:
	python3 main.py

test:
	PYTHONPATH=. .venv/bin/python -m pytest tests/ -v