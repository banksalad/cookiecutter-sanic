.PHONY: init check format test coverage htmlcov requirements

init:
	pip install pipenv
	pipenv sync --dev

check:
	isort --recursive --check-only {{ cookiecutter.package_name }} tests
	black -S -l 79 --check {{ cookiecutter.package_name }} tests
	pylint {{ cookiecutter.package_name }}

format:
	isort -rc -y {{ cookiecutter.package_name }} tests
	black -S -l 79 {{ cookiecutter.package_name }} tests

test:
	python -m pytest

coverage:
	python -m pytest --cov {{ cookiecutter.package_name }} --cov-report term --cov-report xml

htmlcov:
	python -m pytest --cov {{ cookiecutter.package_name }} --cov-report html
	rm -rf /tmp/htmlcov && mv htmlcov /tmp/
	open /tmp/htmlcov/index.html

requirements:
	pipenv lock -r > requirements.txt
	pipenv lock -dr > requirements-dev.txt
