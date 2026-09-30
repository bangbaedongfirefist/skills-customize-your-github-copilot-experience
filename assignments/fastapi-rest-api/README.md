# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to practice defining routes, validating request data, and handling CRUD operations. You will use an in-memory task list, so no database setup is needed.

## 📝 Tasks

### 🛠️ Create and List Tasks

#### Description
Use the provided starter code to build the API and add endpoints for creating tasks and listing all tasks.

#### Requirements
Completed program should:

- Create a FastAPI application and a Pydantic model for a task with a title and completion status
- Assign each new task a unique integer ID and default its completion status to `false`
- Return all tasks from `GET /tasks` as JSON
- Create a task from a JSON request body with `POST /tasks` and return the created task


### 🛠️ Retrieve and Update Tasks

#### Description
Add endpoints to look up a task by its ID and update its title or completion status.

#### Requirements
Completed program should:

- Return a task from `GET /tasks/{task_id}` when it exists
- Update a task with `PUT /tasks/{task_id}` using validated JSON data
- Return HTTP 404 when the requested task ID does not exist
- Keep the task's ID unchanged when its other fields are updated


### 🛠️ Delete and Test Tasks

#### Description
Install FastAPI and Uvicorn with `python -m pip install fastapi uvicorn`, complete the CRUD API by adding a delete endpoint, then use FastAPI's interactive documentation to test the routes.

#### Requirements
Completed program should:

- Delete a task with `DELETE /tasks/{task_id}` and return a clear success response
- Return HTTP 404 when asked to delete a task that does not exist
- Run the app with `uvicorn main:app --reload`
- Use `http://127.0.0.1:8000/docs` to create, list, retrieve, update, and delete a task