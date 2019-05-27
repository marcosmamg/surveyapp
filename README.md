# surveyapp
Apply migrations on firt run to create database structure
    docker exec -it surveyapp_django_1 python manage.py migrate

Create superuser to access admin module:
    docker exec -it surveyapp_django_1 python manage.py createsuperuser
