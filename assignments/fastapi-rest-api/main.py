from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Task API")


class Task(BaseModel):
    title: str
    completed: bool = False


tasks: dict[int, Task] = {}
next_task_id = 1


@app.get("/tasks")
def list_tasks():
    # TODO: Return all tasks.
    pass


@app.post("/tasks")
def create_task(task: Task):
    # TODO: Assign an ID, store the task, and return it.
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # TODO: Return the task or raise HTTPException with status code 404.
    pass


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    # TODO: Replace the task fields without changing its ID.
    pass


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    # TODO: Delete the task or raise HTTPException with status code 404.
    pass