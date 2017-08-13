serve: clean
		python manage.py runserver

clean:
		find . -name "*.pyc" -delete
		find . -name "*.pyo" -delete
		rm -f .coverage

test: clean
	python manage.py test apps

