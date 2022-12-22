# Asynchronous Processing using FastAPI, Celery, Redis and Postgres

![Celery Exceution Flow](https://imgur.com/8ORAot6.png)

This is a simple example of how to use FastAPI, Celery, Redis and Postgres to process asynchronous tasks.

- FastAPI is used to create the API endpoints.
- Celery is used to process the tasks asynchronously.
- Redis is used as a message broker.
- Postgres is used to store the task results.
- Flower is used to monitor the tasks.

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

## API Endpoints

We have a basic task. The task is to find all the prime numbers between 1 and a given number.

1️⃣ Add a new task

_URL_: http://localhost:8000/task

_Request Body_

```json
{
  "num": 10
}
```

_Response Body_

```json
{
  "task_id": "15b7d3b4-ef87-4be1-9f79-eb0c8ae829e0"
}
```

---

2️⃣ Get the task status and result

_URL_: http://localhost:8000/task/{TASK-ID-FROM-PREVIOUS-STEP}

_Response Body_

```json
{
  "state": "SUCCESS",
  "primes": [2, 3, 5, 7]
}
```

Note that state can be one of the following:

1. PENDING (waiting for execution or unknown task id)
2. STARTED (task has been started)
3. SUCCESS (task executed successfully)
4. FAILURE (task execution resulted in exception)
5. RETRY (task is being retried)
6. REVOKED (task has been revoked)

---

3️⃣ Monitoring the tasks using flower

**URL**: http://localhost:5555
