# SuYuan）溯源 v2.1

##  Project Introduction

对溯源——全国能源可视化平台提供的基于 Django + Django REST framework + MySQL 的后端技术支持。

##  Project Description

溯源的后端基于 Django + Django REST framework + MySQL 构建。它为前端提供了一种简单、直观的方式来管理和展示各种能源资源的数据。

##  Technologies Used

- Django
- Django Bootstrap
- Django Admin Argon Dashboard
- Django REST framework
- Coreapi
- MySQL
...

##  Features

1. **用户管理**：用户可以注册、登录和注销，以及查看和管理他们的个人信息。
2. **资源管理**：用户可以上传、编辑和删除各种自然资源的数据。
3. **数据分析**：提供各种数据分析工具，帮助用户理解和利用数据。
4. **报告生成**：根据用户的选择和输入，自动生成各种报告。

##  Future Work

我们计划在未来的版本中添加更多的功能，如实时数据更新、更复杂的数据分析工具、更多的报告模板等。同时，我们也将继续优化我们的代码，提高其性能和稳定性。



##  Installation dependencies and startup steps

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