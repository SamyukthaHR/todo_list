# TODO LIST APPLICATION
A basic todo list application which offers adding, editing, deleting and viewing of tasks.
## APIs
- GET /tasks: Retrieve a list of all tasks.
- POST /tasks: Create a new task.
- GET /tasks/{id}/0: Retrieve a specific task by its ID.
- PUT /tasks/{id}/1: Update a specific task.
- DELETE /tasks/{id}/2: Delete a specific task.
- GET /tasks/data?page={page_number}
            
Installation

To install the required packages, run the following command in the project directory:

    pip install -r requirements.txt
    
Usage

To create tables and make migrations, run the below commands:

        python manage.py makemigrations
        python manage.py migrate

To start the server, run the below command:

    python mange.py runserver
  
  The local server starts running on http://127.0.0.1:8000
  
  (Example url: http://127.0.0.1:8000/{end_point})

