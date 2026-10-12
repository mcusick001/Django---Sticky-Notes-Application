----------------------------------------
    Django Sticky Notes Application
----------------------------------------

A clean, responsive Sticky Notes web
application built with Django and Bootstrap
5, featuring complete CRUD (Create, Read, 
Update, Delete) functionality, an individual
detail view, and standardized hyphenated URL
routing conventions.

--------------------
PROJECT STRUCTURE
--------------------
sticky_notes_task_manager/
|
|---sticky_notes_project/
|     |--sticky_notes/
|     |    |--- migrations/
|     |    |--- templates/sticky_notes/
|     |    |--- __init__.py
|     |    |--- admin.py
|     |    |--- apps.py
|     |    |--- forms.py
|     |    |--- models.py
|     |    |--- tests.py
|     |    |--- urls.py
|     |    |--- views.py
|     |    
|     |--sticky_notes_project/
|     |    |--- __init__.py
|     |    |--- asgi.py
|     |    |--- settings.py
|     |    |--- urls.py
|     |    |--- wsgi.py
|     |
|     |--manage.py
|     |--requirements.txt
|
|---designs/
|     |--- use_case_diagram.jpg
|     |--- sequence_diagram.jpg
|     |--- class_diagram.jpg
|
|--- .gitignore
|--- README.md
|--- sticky_github.txt

--------------------
SETUP & INSTALLATION
--------------------
1. Clone or Unzip the project
Navigate into the root project directory in
your terminal:
bash

cd sticky_notes_project

2. Create and Activate virtual environment
bash

python -m venv venv

venv\Scripts\Activate.ps1

3. Install Dependencies
Install the required packages using the
provided requirements file:
bash

pip install -r requirements.txt

4. Run Database Migrations
bash

python manage.py makemigrations sticky_notes

python manage.py migrate

5. Run Tests
bash

python manage.py test

6. Start the Development Server
bash

python manage.py runserver