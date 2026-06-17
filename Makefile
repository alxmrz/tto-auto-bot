init:
	cp -n .env.example .env

install:
	pip install -r requirements.txt

run:
	PYTHONPATH=. .venv/bin/python main.py

test:
	PYTHONPATH=. .venv/bin/python -m pytest tests/ -v