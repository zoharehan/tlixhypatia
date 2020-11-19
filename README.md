# tlixhypatia
Pre-Run Installations:
1. For the Hypatia Python Server:
  - pip install eventlet
  - pip install python-socketio
  - download the json package for your IDE
2. The Companion Application:
  - pip install pipenv => the virtual environment
  (if using pipenv, the commands starting with pip in the next lines will be replaced with pipenv)
  - pip install django, djangorestframework, django-rest-knox
  - install node.js here: https://nodejs.org/en/
  - npm init -y => to create your package.json file 
  - npm i -D webpack webpack-cli => installing webpack,webpack cli as a dev dependency
  - npm i -D @babel/core babel-loader @babel/preset-env @babel/preset-react babel-plugin-transform-class-properties => babel transpiles react to js
  - npm i react react-dom prop-types => react for frontend


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

suggested practice questions api: http://127.0.0.1:8000/suggestedpracticeapi/suggestedpractice/


libraries to install:
<br />
  pip install djangorestframework
<br />
  pip install markdown       # Markdown support for the browsable API.
<br />
  pip install django-filter  # Filtering support

everytime you make a new model, run these commands in your terminal when you are in the hypatia folder:


python3 manage.py makemigrations


 python3 manage.py migrate
