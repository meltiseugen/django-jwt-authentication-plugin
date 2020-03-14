## Description

This is an JWT authentication plugin for Django REST Framework.
It uses ```simplejwt``` to provide the basic url routes. Also it makes use of 
custom ```CustomTokenObtainPairSerializer``` in order to customize the ```login``` response 
and ```CustomTokenObtainPairView``` to override the default ```TokenObtainPairView``` of ```simplejwt```

Available URL routes are:
* ```auth/login``` - used to obtain the token and refresh token values together with other custom fields. - refer to simplejwt docs for more information
* ```auth/token/refresh``` - used to refresh to refresh the token. - refer to simplejwt docs for more information
* ```auth/users/register``` - used to create a new user.

## Installation

1. Clone the project along side your existing apps.

```git clone https://github.com/meltiseugen/django-jwt-authentication-plugin.git```

2. Install the django-jwt-authentication-plugin requirements.

```pip install -r authentication/requirements.txt```

3. Add the ```authentication``` app to ```INSTALLED_APPS``` of ```settings.py```

4. Add the URL routes to the main url.py of your project.

```
urlpatterns = [
    ...
    path('api/', include('authentication.urls')),
    ...
]
```

4. Migrate your project in order to create the necessary models in the database.

```python manage.py makemigrations && python manage.py migrate```

5. You can now modify the authentication app in order to further customize it for your needs.
Commit it along side your project and update it when new updates are available.