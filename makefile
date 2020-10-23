init:
    pip install wikipedia

test:
    py.test tests

.PHONY: init test