# Asynchronous Processing using FastAPI, Celery, Redis and Postgres

![Celery Exceution Flow](https://imgur.com/8ORAot6.png)

This is a simple example of how to use FastAPI, Celery, Redis and Postgres to process asynchronous tasks.
* FastAPI is used to create the API endpoints.
* Celery is used to process the tasks asynchronously.
* Redis is used as a message broker.
* Postgres is used to store the task results.

## How to run the project
1. Clone the project

```bash
git clone git@github.com:adimyth/async-process-using-celery-redis-postgres/.git
```

2. Modify environment variables
```bash
cp .env.example .env
```
.env
```bash
COMPOSE_PROJECT_NAME=ml_model_deployment

ENVIRONMENT=dev # dev or prod. In case of dev, we run postgres container locally, otherwise we use a remote postgres instance.

# Postgres Credentials
DB_HOST=""
DB_PORT=5432
DB_USER=""
DB_PASSWORD=""
DB_NAME=""

# Set basic flower auth
FLOWER_USER=""
FLOWER_PASSWORD=""
```

3. Run the setup
```bash
./deploy/start
```

