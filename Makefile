up:
	docker-compose up -d --build
migrate:
	docker-compose exec web python manage.py makemigrations
	docker-compose exec web python manage.py migrate
static:
	docker-compose exec web python manage.py collectstatic --noinput

migstat:
	docker-compose exec web python manage.py makemigrations
	docker-compose exec web python manage.py migrate
	docker-compose exec web python manage.py collectstatic --noinput
down:
	docker-compose down -v
