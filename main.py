from fastapi import FastAPI

import celery_app.tasks as tasks
from schemas.request import ModelRequest
from schemas.response import ModelResponse

app = FastAPI()


@app.post("/task")
def calculate_async(request: ModelRequest):
    # Add the task to the queue
    task = tasks.primes.delay(request.num)
    return {"task_id": task.id}


@app.get("/task/{task_id}", response_model=ModelResponse)
def get_task_result(task_id: str):
    # Get the result from the database
    result = tasks.get_primes_result(task_id)
    return result
