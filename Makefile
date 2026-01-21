PYTHON = .venv/bin/python3
PIP = .venv/bin/pip

# Phony targets. Check https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html
.PHONY: setup install run test clean

setup:
	python3 -m venv .venv
	$(PIP) install --upgrade pip
	$(PIP) install -e .
	$(PIP) install pytest

run:
	$(PYTHON) main.py

test:
	$(PYTHON) -m pytest tests/

reset-db:
	rm -f maini.db
	rm -rf __pycache__
	@echo "Database deleted. Run 'make run' to initialize a fresh one."

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
