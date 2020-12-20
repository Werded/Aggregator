.PHONY: all fixtures static locale

all: clean lint

lint:
	mkdir -p reports
	touch reports/bandit.json;
	touch reports/pylint.txt;
	chmod -R 777 reports/
	black exchange_rate_aggregator --check
	flake8
	isort -c .
	bandit -s B101 -r -f json -o reports/bandit.json exchange_rate_aggregator
	pylint exchange_rate_aggregator | tee reports/pylint.txt
	mypy exchange_rate_aggregator --txt-report reports
	chmod -R 777 reports

static:
	python3 manage.py collectstatic --noinput

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	isort .
	black .
