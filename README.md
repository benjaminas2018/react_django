### Django-React Learning, details refer to : https://www.valentinog.com/blog/drf/#Django_REST_with_React_Django_and%20React_together
- *react_django*
Self_learning_for_react_django, steps are learn from https://www.youtube.com/watch?v=Uyei2iDA4Hs

- *install the django modules*
```Bash
pip install django djangorestframework django-rest-knox
```

- *Create Django project*
```Bash
django-admin startproject leadmanager
```

- *change the directory to leadmanager/*
```Bash
python3 manage.py startapp leads
```
- *go to leadmanager/leadmanager/settings.py*
```python
- *add new app into INSTALLED_APPS in the settings.py file*
 INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'leads',
    'rest_framework'
]
```
- *the sqlites is using for the learning, change according to the real database, you can use mysql etc.*

- *after APP created, you should define the app models for database:leadmanager/leads/models.py*
```python
class Lead(models.Model) : name = models.CharField(max_length = 100)
    # Avoid multiple emails,
    # so the unique set to True
    email = models.EmailField(max_length = 100, unique = True)
    # enable the message could be empty,
    # set the blank = True
    message = models.CharField(max_length = 500, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)
```
- *after the modes.py changed, you should run the below commands to create database*
```Bash
python3 manage.py makemigrations leads
python3 manage.py migrate leads
```

- *The output should be like:*
```Bash
Operations to perform:
  Apply all migrations: leads
Running migrations:
  Applying leads.0001_initial... OK
```

- *Create the serializers under the app: leads folder, please refer to https//www.django-rest-framework.org/api-guide/serializers/*
```python
from rest_framework import serializers
from leads.models import Lead

# Lead Serializers
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        # __all__ stands for all fields we defined in leads/models.py
        fields = '__all__'
```

- *Create api.py under the app: leads*
```python
from leads.models import Lead
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer

# Lead Viewset
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny #could be changed according real requirements
    ]
    serializer_class = LeadSerializer
```

- *go to the leadmanager folder , change urls.py*
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('leads.urls')),
]
```

- *create urls.py under the app: leads*
```python
from  rest_framework import routers
from .api import LeadViewSet

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, "leads")

urlpatterns = router.urls
```

- *then start the django website*
```
python3 manage.py runserver
```

- *Check if your django web is works via http://localhost:8000/api/leads/*
- *you can debug api via "postman" software or chrome's extention "ApiDebug-Http"*


### Start the React Part
npm init -y
npm i webpack webpack-cli --save-dev

- * Now open up package.json and configure the scripts:
```
"scripts": {
  "dev": "webpack --mode development ./project/frontend/src/index.js --output ./project/frontend/static/frontend/main.js",
  "build": "webpack --mode production ./project/frontend/src/index.js --output ./project/frontend/static/frontend/main.js"
```
```
npm i @babel/core babel-loader @babel/preset-env @babel/preset-react babel-plugin-transform-class-properties --save-dev
npm i react react-dom prop-types --save-dev
```
```
npm i redux react-redux redux-thunk redux-devtools-extension
npm i axios
```

- * Problem when run npm install
```
sudo npm cache clean --force
sudo rm rf node_modules
sudo npm install
```

* - Authentication Steps
```
npm i react-router-dom
```

* create Regester.js and Login.js under components/accounts, the accounts folder is created first