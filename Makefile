run-dev:
	poetry run python manage.py runserver
migrate:
	poetry run python manage.py makemigrations && poetry run python manage.py migrate
dumpdata:
	poetry run python -Xutf8 manage.py dumpdata --indent=2 dishes.TypeDish -o fixtures/type_dish.json
	poetry run python -Xutf8 manage.py dumpdata --indent=2 dishes.Dish -o fixtures/dish.json
loaddata:
	poetry run python -Xutf8 manage.py loaddata fixtures/*.json
tests:
	poetry run python manage.py test .
createsuperuser:
	poetry run python manage.py createsuperuser
