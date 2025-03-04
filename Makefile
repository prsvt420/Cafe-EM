run-dev:
	poetry run python manage.py runserver
run-prod:
	poetry run gunicorn CafeEM.wsgi:application --bind 0.0.0.0:8000
migrate:
	poetry run python manage.py makemigrations && poetry run python manage.py migrate
dumpdata:
	poetry run python manage.py dumpdata --indent=2 ...
loaddata:
	poetry run python -Xutf8 manage.py loaddata fixtures/*.json
tests:
	poetry run python manage.py test .
createsuperuser:
	poetry run python manage.py createsuperuser
collectstatic:
	poetry run python manage.py collectstatic --no-input
