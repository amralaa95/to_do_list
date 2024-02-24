Stack Used: Python / Django / HTML / CSS / JavaScript / Bootstrap / MySQL
1-Create .env file and copy the keys from .env_example
2-Build the app using this command: docker-compose up --build
tun

# TODO App

Application for making todo lists and tasks

## Building local
Create .env file and copy the content from .env_example file

```bash
change DB_HOST ENV to localhost
```

```bash
virtualenv -p python3 .venv
source .venv/bin/activate
pip install -r requirements
python manage.py migrate
python manage.py runserver
```
## Building Docker

we use Docker compose, this will install Mysql and seed it with some data then wait to see logs of launch app
Create .env file and copy the content from .env_example file

```bash
sudo docker-compose up --build
```

You might need to run the following command if docker has problem with permission then run above command again.
```shell
chmod +x ./run.sh
```

You can access the app through http://127.0.0.1:8000/