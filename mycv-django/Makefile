run:
	python manage.py runserver

install:
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

migrate:
	python manage.py migrate

makemigrations:
	python manage.py makemigrations

test:
	coverage run manage.py test
	coverage report
