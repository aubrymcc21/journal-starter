.PHONY: help
help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "Targets:"
	@fgrep "##" Makefile | fgrep -v fgrep

.PHONY: run
run:
	uvicorn api.main:app --reload --host 0.0.0.0 --port 8000

.PHONY: install
install:
	pip install -r api/requirements.txt
