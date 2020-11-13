# tlixhypatia

Currently: attempting to use React in its own "frontend" Django app: load a single HTML template and let React manage the frontend.

How to start react: npm run dev
python3 manage.py runserver

username: admin
password: password
email: admin@example.com

hypatia summary page web app


Creating a web application interface for elementary students to learn math. 


Stack: Django, Django REST, React, Redux

Used: bootswatch(customized bootstrap), bootstrap

npm run dev => compile react application for development so we can view in the browser

npm run build => to deploy

questionapi: http://127.0.0.1:8000/questionapi/question/


libraries to install:
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support

everytime you make a new model, run these commands in your terminal when you are in the hypatia folder:
python3 manage.py makemigrations
 python3 manage.py migrate
