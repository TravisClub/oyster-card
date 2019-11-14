venv:
	virtualenv -p python3.6 venv

init:
	pip install -r requirements.txt

run:
	python oyster/oyster_card.py

.PHONY: init run venv
