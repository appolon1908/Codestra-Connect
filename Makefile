.PHONY: validate test
validate:
	@python3 scripts/validate_foundation.py
test: validate
