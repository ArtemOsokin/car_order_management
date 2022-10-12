## Проект тестового задания Car Order Managment
Проект написан с использованием:
- Django REST-framework
- PostgreSQL

Запуск производиться через:
- Docker Compose
- nginx

С документацией можно ознакомиться по 
[ссылке](./Osokin.Art-Cars-1.0.0-swagger.yaml)
([SwaggerHub](https://app.swaggerhub.com/apis/Osokin.Art/Cars/1.0.0))


### Запуск проекта

Осуществляется с помощью docker-compose. 

**`docker-compose up -d --build`**

После первой сборки требуется выполнить поочерёдно несколько команд:

1. Выполнить миграции
- `docker-compose exec web python manage.py makemigrations`
- `docker-compose exec web python manage.py migrate`

2. Выкатить статику проекта:

`docker-compose exec web python manage.py collectstatic  --noinput`
