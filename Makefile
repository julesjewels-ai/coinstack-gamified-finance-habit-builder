.PHONY: install run test clean help

VENV_DIR = .venv
PYTHON = $(VENV_DIR)/bin/python3
PIP = $(VENV_DIR)/bin/pip

help:
	@echo "Available targets:"
	@echo "  install    - Create a virtual environment and install dependencies."
	@echo "  run        - Activate the virtual environment and run the main application."
	@echo "  test       - Activate the virtual environment and run tests with pytest."
	@echo "  clean      - Remove virtual environment, cache files, and build artifacts."

install: $(VENV_DIR)/bin/activate
	@echo "Installing dependencies..."
	$(PIP) install -r requirements.txt
	@echo "Installation complete. Run 'make run' to start the application."

$(VENV_DIR)/bin/activate:
	@echo "Creating virtual environment at $(VENV_DIR)..."
	python3 -m venv $(VENV_DIR)

run: install
	@echo "Running Coinstack application..."
	$(PYTHON) main.py

test: install
	@echo "Running tests..."
	$(PYTHON) -m pytest tests/

clean:
	@echo "Cleaning up..."
	rm -rf $(VENV_DIR)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -f .pytest_cache/*
	rm -rf .pytest_cache
	@echo "Cleanup complete."
