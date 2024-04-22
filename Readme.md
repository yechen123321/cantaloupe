1. `npm i`

2. npm run serve
-------------------------------------------
1. python==3.12.3, pip==24.0

2. pip install -r requirements.txt

3. 在 mysql 查询控制台中运行 /SuYuanData.sql 

4. core/setting.py: 
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'suyuan',
        'USER': 'your_database_name',
        'PASSWORD': 'your_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

5. python manage.py makemigrations

6. python manage.py migrate

7. python manage.py runserver localhost:8085
