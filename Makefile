.PHONY: bootstrap smoke smoke-fallback

VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
PYTEST := $(VENV)/bin/pytest

bootstrap:
	@if [ ! -x "$(PYTHON)" ]; then \
		python3 -m venv $(VENV); \
	fi
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

smoke:
	@if [ -x "$(PYTEST)" ]; then \
		PYTHONPATH=. $(PYTEST) -q tests/test_analyze.py tests/test_openrouter_parser.py; \
	else \
		echo "pytest not available in $(VENV); running compile fallback"; \
		$(MAKE) smoke-fallback; \
	fi

smoke-fallback:
	python3 -m compileall app tests
