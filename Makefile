.PHONY: setup train eval deploy
setup:
	pip install -r requirements.lock -e .
train eval deploy:
	@echo "not implemented: $@"; exit 1
