

venv:
	virtualenv -p /usr/bin/python3.7 .venv

init:
	pip install -r requirements.txt