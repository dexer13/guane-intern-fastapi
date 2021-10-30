# guane-intern-fastapi:
Rest services to manage dogs and adoptions.
***
## Índice
1. [Features](#features)
2. [Stack](#stack)
3. [Architecture](#architecture)
4. [File Structure](#file-structure)
5. [IDE](#ide)
6. [requirements](#requirements)
7. [Deployment](#deployment)
8. [Services](#services)
9. [Author](#author)
***

## Features

  - REST services
  - Asynchronous tasks
  - Task monitoring
  - Authentication with JWT
  - Portability, lightness and self-sufficiency

***
## Stack

  - [FastApi](https://fastapi.tiangolo.com/)
  - [Tortoise](https://tortoise-orm.readthedocs.io/en/latest/) + [Postgresql](https://www.postgresql.org/)
  - [Poetry](https://python-poetry.org/)
  - [celery](https://docs.celeryproject.org/en/stable/getting-started/introduction.html)
  - [Docker](https://www.docker.com/)
  - [redis](https://redis.io/)
  - [flower](https://flower.readthedocs.io/en/latest/)
  
***
## Architecture
put here architecture image
***
## File Structure
```shell script
.
├── app
│   ├── worker
│   │   ├── worker.py
│   │   └── __init__.py
│   ├── tests
│   │   ├── test_routers
│   │   │   ├── test_user.py
│   │   │   ├── test_security.py
│   │   │   ├── test_animals.py
│   │   │   └── __init__.py
│   │   ├── load_data.py
│   │   └── __init__.py
│   ├── migrations
│   │   └── models
│   ├── logs
│   ├── core
│   │   ├── utils
│   │   │   ├── jwt_token.py
│   │   │   ├── __init__.py
│   │   │   └── hashing.py
│   │   ├── schemas
│   │   │   ├── user.py
│   │   │   ├── security.py
│   │   │   ├── __init__.py
│   │   │   └── animals.py
│   │   ├── routers
│   │   │   ├── users.py
│   │   │   ├── security.py
│   │   │   ├── __init__.py
│   │   │   └── animals.py
│   │   ├── models
│   │   │   ├── __init__.py
│   │   │   ├── auth.py
│   │   │   └── animals.py
│   │   ├── dependencies
│   │   │   ├── oauth2.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── config
│   │   ├── database
│   │   │   ├── pg.py
│   │   │   └── __init__.py
│   │   ├── parameters.py
│   │   └── __init__.py
│   ├── requirements.txt
│   ├── pyproject.toml
│   ├── poetry.lock
│   ├── main.py
│   ├── __init__.py
│   ├── Dockerfile
│   ├── conftest.py
│   └── aerich.ini
├── README.md
├── docker-compose.yml
├── commands.txt
└── aerich.ini

```
***
## IDE
  - The project was developed with [PyCharm](https://www.jetbrains.com/es-es/pycharm/) con [licencia de estudiante](https://www.jetbrains.com/es-es/community/education/#students)
  
***
## Requirements
- Install **docker** and **docker-compose**
## Deployment
- Clone repository from GitHub
```shell script
git clone https://github.com/dexer13/guane-intern-fastapi.git project
cd project
```
- Build project with docker compose
```shell script
sudo docker-compose up --build
```
### First time
- Initialize the config file and migrations location
```shell script
sudo docker-compose exec server aerich init -t app.config.database.pg.TORTOISE_ORM
```
- Init database
```shell script
sudo docker-compose exec server aerich init-db
```
- Migrate and update database
```shell script
sudo docker-compose exec server aerich migrate
sudo docker-compose exec server aerich upgrade
```
- Load default data to database. This script create a default user with username **admin** and password **123**
```shell script
sudo docker-compose exec server python load_data.py
```

***
## Tests
Run tests
```shell script
sudo docker-compose exec server pytest
```
***
### Servicios
Go to [http://localhost:8000/docs](http://localhost:8000/docs) to see all services
***
### Autor
The project was developed by:
 - Denis González [GitHub](https://github.com/dexer13) [LinkedIn](https://www.linkedin.com/in/denis-eduardo-isidro-gonzalez-428a51210/)

***