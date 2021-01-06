# Run Backend

## Command to install

Clone the project

>- ```SSH Key : git@github.com:EpitechIT2020/T-WEB-501-MPL-5-1-jobboard-rudy.gonzalez.git```

After clone the project, go to root of project

>- ```cd Step01 ```
>- ```cd backend ```
>- ```cd jobAria ```

In your Terminal create a Virtual Environment Python with the command

>- ```python -m venv```

After that, activate your venv interpreter if necessary.

And run this commands

>- ```pip install -r requirements.txt```
            
##            OR

>- ```pip install django```
>- ```pip install ariadne```
>- ```pip install python-dateutil```
>- ```pip install psycopg2-binary```
>- ```pip install django[argon2]```

### Doc [Django][1] | Doc [Ariadne][2]

[1]: https://docs.djangoproject.com/fr/3.1/
[2]: https://ariadnegraphql.org/docs/intro.html


After, install PostgresSQL 
Create your account and database with settings below

>```
>DATABASES = {
>    'default': {
>        'ENGINE': 'django.db.backends.postgresql_psycopg2',
>        'NAME': 'YOUR_DATABASE_NAME',
>        'USER': 'YOUR_DATABASE_NAME',
>        'PASSWORD': 'YOUR_DATABASE_PASSWORD',
>        'HOST': '127.0.0.1',
>        'PORT': '5432',
>    }
>}
>```

Then, run the last command

>- ```python manage.py makemigrations```
>- ```python manage.py migrate```
>- ```python manage.py runserver```

Then go to the your Web browser and in your URL write 

>- ```http://127.0.0.1:8000/api/```

Requests Examples :

>- ```mutation{createUser(email: "guillaume@epitech.eu", password:"@Zertyu34"){success, error}}```
>- ```mutation{updateUser(user_id:60 email: "guillaume@epitech1.eu", password:"@Zertyu34"){success, error}}```
>- ```mutation{deleteUser(user_id:60){success, error}}```
>- ```query{user(user_id: 25){success{id,email}, error}}```
>- ```query{users{id, email}}```




