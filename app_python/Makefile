#* Variables
SHELL := /usr/bin/env bash
PYTHON := python

#* Docker variables
IMAGE := a1d4r/devops-python-app
VERSION := latest

CODE = app tests
TESTS = tests

#* Poetry
.PHONY: poetry-download
poetry-download:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | $(PYTHON) -

.PHONY: poetry-remove
poetry-remove:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | $(PYTHON) - --uninstall

#* Installation
.PHONY: install
install:
	poetry lock -n && poetry export --without-hashes > requirements.txt
	poetry install -n
	poetry run mypy --install-types --namespace-packages --explicit-package-bases --non-interactive $(CODE)

.PHONY: pre-commit-install
pre-commit-install:
	poetry run pre-commit install

#* Run web application (dev server)
.PHONY: up
up:
	poetry run uvicorn app.main:app --reload

#* Formatters
.PHONY: codestyle
codestyle:
	poetry run pyupgrade --exit-zero-even-if-changed --py39-plus **/*.py
	poetry run isort --settings-path pyproject.toml $(CODE)
	poetry run black --config pyproject.toml $(CODE)

.PHONY: formatting
formatting: codestyle

#* Linting
.PHONY: test
test:
	poetry run python -m pytest --cov=app $(TESTS)

.PHONY: check-codestyle
check-codestyle:
	poetry run isort --diff --check-only --settings-path pyproject.toml $(CODE)
	poetry run black --diff --check --config pyproject.toml $(CODE)
	poetry run darglint --verbosity 2 $(CODE)

.PHONY: linting
linting:
	poetry run pylint --rcfile=.pylintrc $(CODE)
	poetry run mypy --config-file pyproject.toml --namespace-packages --explicit-package-bases $(CODE)

.PHONY: check-safety
check-safety:
	poetry check 
	poetry run safety check --full-report
	poetry run bandit -s B101 --recursive $(CODE)

.PHONY: lint
lint: check-codestyle linting check-safety

#* Docker
# Example: make docker VERSION=latest
# Example: make docker IMAGE=some_name VERSION=0.1.0
.PHONY: docker-build
docker-build:
	@echo Building docker $(IMAGE):$(VERSION) ...
	docker build \
		-t $(IMAGE):$(VERSION) . \
		-f ./docker/Dockerfile

# Example: make clean_docker VERSION=latest
# Example: make clean_docker IMAGE=some_name VERSION=0.1.0
.PHONY: docker-remove
docker-remove:
	@echo Removing docker $(IMAGE):$(VERSION) ...
	docker rmi -f $(IMAGE):$(VERSION)

#* Cleaning
.PHONY: pycache-remove
pycache-remove:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

.PHONY: build-remove
build-remove:
	rm -rf build/

.PHONY: clean-all
clean-all: pycache-remove build-remove docker-remove
