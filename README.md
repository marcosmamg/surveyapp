# Django Survey App

## Services

* Django, MySQL and PHPMyAdmin

## Getting Started

### Step 1: Setting up environment

#### Run the project with docker container

* Download Docker https://www.docker.com/community-edition
* Download Docker compose https://docs.docker.com/compose/install/
* Clone this project repo on any working folder.
* Create .env file to specifiy credentials and some other info. Refer to env.example file, leave as is and django will connect automatically, otherwise update `settings.py`
* Open the OS terminal and enter the Project path.
* Write `docker-compose up -d` in your terminal.
* Run the following commands to execute migrations and create superuser: 
    * `docker exec -it django python manage.py migrate`
    * `docker exec -it django python manage.py createsuperuser`
* Now you can open `http://localhost:8000` in your web browser.

Notes: In case the site is not loading, it is because django container has not connected to MySQL properly.
* To solve it, just restart the django container: 
    * `docker restart django`

### Services:
* Django: `http://localhost:8000`
* PHPMyAdmin: `http://localhost:8082`
    * Default Credentials as per env.example:
        * Server: mysql
        * User: root
        * Password: abc123
