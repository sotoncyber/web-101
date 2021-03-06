.DEFAULT_GOAL := run
.PHONY: clean, clean-db, init-db, venv, run

clean: # Clean build files
	rm -rf *.pyc
	rm -rf __pycache__/
	rm -rf **/__pycache__/

clean-db: # Delete database
	rm -rf *.db

init-db: # Create database
	flask/bin/python3 -c 'from challenge.db import init_db; init_db()'

venv: # Setup virtual environment
	virtualenv -p python3 flask
	flask/bin/pip3 install flask flask_wtf

run: # Run app
	flask/bin/python3 run.py
