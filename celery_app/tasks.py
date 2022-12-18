import time

from celery import Task
from celery.result import AsyncResult
from fastapi import HTTPException
from fastapi.responses import JSONResponse

from celery_app.prime import find_primes
from celery_app.worker import app


@app.task(bind=True, name="primes", base=Task, max_retries=3, default_retry_delay=5)
def primes(self, inputs):
    """
    This function is the task that will be executed asynchronously.
    """
    result = find_primes(inputs)
    return result


# Create a helper function to retrieve the prediction result from the database
def get_primes_result(task_id: str):
    """
    Get task status.
    1. PENDING (waiting for execution or unknown task id)
    2. STARTED (task has been started)
    3. SUCCESS (task executed successfully)
    4. FAILURE (task execution resulted in exception)
    5. RETRY (task is being retried)
    6. REVOKED (task has been revoked)
    """
    task = AsyncResult(task_id)

    print("Task state: ", task.state)
    print("Task result: ", task.result)

    if task.state == "PENDING" or task.state == "STARTED":
        raise HTTPException(status_code=202, detail={"state": task.state})
    elif task.state == "FAILURE" or task.state == "RETRY" or task.state == "REVOKED":
        raise HTTPException(status_code=500, detail={"state": task.state})
    elif task.state == "SUCCESS":
        return JSONResponse(
            status_code=200, content={"state": task.state, "primes": task.result}
        )
    else:
        raise HTTPException(status_code=503, detail={"state": task.state})
