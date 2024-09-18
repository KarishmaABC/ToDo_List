To-Do List API and Web Application Documentation
1. Project Overview
This project is a full-stack To-Do List application, comprising a backend API and a frontend web application that interact seamlessly. The backend is built using Django and Django REST Framework (DRF) to manage to-do items, while the frontend is a simple HTML, CSS, and JavaScript web interface to interact with the API.

2. Backend: To-Do List API
2.1 Overview
The API provides basic CRUD operations to manage to-do tasks:
Create: Add a new to-do task.
Read: View all tasks or a specific task.
Update: Modify an existing task (e.g., mark as completed).
Delete: Remove a task.

2.2 Requirements
Python 3.12 (or later)
Django 4.x
Django REST Framework
SQLite Database (default for Django)
 Installation and Setup
Install Dependencies:


pip install django djangorestframework
Create the Django Project:
django-admin startproject todoList
Create the To-Do App:
cd todoList
python manage.py startapp mainApp
Add the App to Django Settings: In settings.py, add 'mainApp' to the INSTALLED_APPS list:


INSTALLED_APPS = [
    # other apps
    'mainApp',
    'rest_framework',  # Django REST Framework
]
Define the To-Do Model in mainApp/models.py:


from django.db import models

class ToDo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
Create Serializer in mainApp/serializers.py:


from rest_framework import serializers
from .models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
Create Views in mainApp/views.py:

from rest_framework import viewsets
from .models import ToDo
from .serializers import ToDoSerializer

class ToDoViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
Define API URLs in mainApp/urls.py:


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ToDoViewSet

router = DefaultRouter()
router.register(r'todos', ToDoViewSet, basename='todo')

urlpatterns = [
    path('api/', include(router.urls)),
]
Apply Migrations:


python manage.py makemigrations
python manage.py migrate
2.4 Running the Backend Server
To start the Django development server, use:


python manage.py runserver
2.5 API Endpoints
GET /api/todos/: Retrieve all tasks.
POST /api/todos/: Create a new task.
GET /api/todos/{id}/: Retrieve a single task by ID.
PUT /api/todos/{id}/: Update a task by ID.
DELETE /api/todos/{id}/: Delete a task by ID.
2.6 Sample API Response
GET /api/todos/:

[
    {
        "id": 1,
        "title": "Complete Django project",
        "description": "Finish the backend API",
        "completed": false,
        "created_at": "2024-09-18T12:34:56Z"
    },
    {
        "id": 2,
        "title": "Buy groceries",
        "description": "Milk, Eggs, Bread",
        "completed": true,
        "created_at": "2024-09-18T12:40:12Z"
    }
]
2.7 Testing the API
Use tools like Postman or curl to interact with the API or visit http://127.0.0.1:8000/api/todos/ in your browser for a list of tasks.
Frontend: To-Do List Web Application
3.1 Overview
The web frontend interacts with the backend API to allow users to view, add, and manage their to-do tasks. This web application uses basic HTML, CSS, and JavaScript for structure, styling, and functionality.

3.2 Requirements
Django Static Files: Serve the static assets (CSS, JavaScript).
HTML/CSS/JavaScript: For the front-end interface.
3.3 Setup and Structure
Create a folder named todo_web_app for the frontend inside your Django project:


C:\Django\todo\todoList\todo_web_app\
    └── static\
        └── css\ (for stylesheets)
        └── js\ (for JavaScript files)
    └── templates\
        └── index.html (main webpage)
3.4 Frontend Files
HTML (index.html):


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>To-Do List App</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
    <div id="app">
        <h1>To-Do List</h1>
        <ul id="todo-list"></ul>
        <input type="text" id="new-task" placeholder="Add new task">
        <button onclick="addTask()">Add Task</button>
    </div>

    <script src="{% static 'js/app.js' %}"></script>
</body>
</html>
CSS (styles.css):

css
Copy code
body {
    font-family: Arial, sans-serif;
    margin: 20px;
}

#app {
    max-width: 600px;
    margin: 0 auto;
}

ul {
    list-style: none;
    padding: 0;
}

li {
    background-color: #f9f9f9;
    padding: 10px;
    border: 1px solid #ddd;
    margin-bottom: 5px;
}
JavaScript (app.js):

javascript
Copy code
const API_URL = "/api/todos/";

function getTasks() {
    fetch(API_URL)
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById('todo-list');
            list.innerHTML = '';
            data.forEach(task => {
                const li = document.createElement('li');
                li.innerText = task.title;
                list.appendChild(li);
            });
        });
}

function addTask() {
    const newTask = document.getElementById('new-task').value;
    fetch(API_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ title: newTask, completed: false })
    })
    .then(response => response.json())
    .then(() => {
        document.getElementById('new-task').value = '';
        getTasks();
    });
}

window.onload = getTasks;
3.5 Django Static and Template Configuration
In settings.py, add the paths for static files and templates:


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

TEMPLATES = [
    {
        'DIRS': [BASE_DIR / 'templates'],
    },
]
3.6 Adding URL for Frontend
Add a route for the frontend in urls.py:


from django.views.generic import TemplateView

urlpatterns = [
    path('todo-web/', TemplateView.as_view(template_name="index.html")),
]
3.7 Running the Frontend
Once the Django server is running, you can access the web application at:


http://127.0.0.1:8000/todo-web/
4. Running the Full Application
Start the Django Server:


python manage.py runserver
Access the API: Visit the API at http://127.0.0.1:8000/api/todos/ to test with raw data.

Access the Web App: Visit the web app at http://127.0.0.1:8000/todo-web/ to use the frontend interface for managing
