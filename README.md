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
* For Dev instances run:
    * `make up_dev`
* For production run:
    * `make up_prod`
* For migrations run:
    * `make migrate`
* Run the following command to create superuser and make sure to pass values to the parameters with no spaces: 
    * `make createsuperuser username= email= password=`
* Now you can open `http://localhost` in your web browser.
* To simulate a new user, click the button `New Session` and it will show all questions again as it will be a new session (User)

### Services:
* Django: `http://localhost`

### To run unit tests:
* `make pytest`
