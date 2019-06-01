.PHONY: setup

#start the whole project
up_dev:
	docker-compose -f docker-compose.dev.yml up -d

up_prod:
	docker-compose -f docker-compose.yml up -d

# stop containers
stop:
	docker-compose stop

# stop and remove containers
down:
	docker-compose down

# restart containers
restart:
	docker-compose restart

#access to container bash
bash:
	docker exec -it django bash

#make createsuperuser username= email= password=
createsuperuser:
	docker exec django python manage.py shell -c 'from django.contrib.auth.models import User; User.objects.create_superuser("$(username)", "$(email)", "$(password)")'

removedb:
	rm -rf ./mysql

migrate:
	docker exec django python manage.py migrate

test:
	docker exec django pytest

makemigrations:
	docker exec django makemigrations

logs:
	docker logs -f django