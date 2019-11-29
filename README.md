### Django-React Learning
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
