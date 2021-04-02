# TLIxHypatia - Hypatia Summary Page Web App!

Creating a web application interface for elementary students to learn math. 

Stack: Django, Django REST, React, Redux

Used: bootswatch(customized bootstrap), bootstrap

Here is a video of a presentation/demo of our project: https://youtu.be/BpQ55klMCz4

# Pre-Run Installations:

### SocketIO ###
1. For the Hypatia Python Server:
- cd tlixhypatia
- cd checkmath_api

and then,

- pip install eventlet
- pip install python-socketio
- pip install requests
- download the json package for your IDE
  
Finally, to run it in the terminal shell, start your virtual environment, and enter,

- python server.py

### Companion Application ####
2. The Companion Application:
  - pip install pipenv => the virtual environment
  (if using pipenv, the commands starting with pip in the next lines will be replaced with pipenv)
  - pip install markdown
  - pip install django, djangorestframework, django-rest-knox
  - pip install django-filter
  - install node.js here: https://nodejs.org/en/
  - npm init -y => to create your package.json file 
  - npm i -D webpack webpack-cli => installing webpack,webpack cli as a dev dependency
  - npm i -D @babel/core babel-loader @babel/preset-env @babel/preset-react babel-plugin-transform-class-properties => babel transpiles react to js
  - npm i react react-dom prop-types => react for frontend
  - npm i redux react-redux redux-thunk redux-devtools-extension
  - npm i axios
  - npm install react-bootstrap bootstrap
  - pip install Django-crispy-forms
  
# Essentials needed to know to use our application

### Models & Migrations ###

everytime you make a new model, or if you're running this for the first time, run these commands in your terminal when you are in the hypatia folder:

1. python3 manage.py makemigrations
2. python3 manage.py migrate

### How to start react ###

- On one terminal: npm run dev & another separate terminal window: python3 manage.py runserver
- npm run dev => compile react application for development so we can view in the browser
- npm run build => to deploy

### Question Standard ###
We must receive questions from the hypatia application with document names that have the following format:
- <topic_type>-<question_prompt>.etz

### Topic Standard ###
We used the 4 topic below for our demo and made this our standard for consistency:
1. Addition
2. Subtraction
3. Multipliation
4. Division

### Score Standard ###
- If the value of the question has a type of correct, then the score is 100
- Otherwise, the score is 0 (whether it be math-error, parser-error, etc...)
- NO other score is accepted from 0 to 100 exclusive

### Admin Info ###

username: admin
password: password
email: admin@example.com


# Links

### Main Pages ###

1. local host page: http://127.0.0.1:8000/

2. topic page (this is our main page): http://127.0.0.1:8000/summary/

3. topic summary page: http://127.0.0.1:8000/summary/<topic_id> (Need to have topic id already in topicAPI)

### APIs Links ###

1. questionapi: http://127.0.0.1:8000/questionapi/question/

2. suggested practice questions api: http://127.0.0.1:8000/suggestedpracticeapi/suggestedpractice/

3. topicapi: http://127.0.0.1:8000/topicapi/topic

4. notesapi: http://127.0.0.1:8000/noteapi/notes
