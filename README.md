# DRFtask
Дипломный проект по теме: Дипломный проект по теме: Сравнение различных подходов к реализации REST API: Django Rest Framework, FastAPI и Flask-RESTful.

>Этот проект представляет собой менеджер задач , разработанный с использованием Django Rest Framework и подключением PostgreSQL. Ниже приведена структура проекта и инструкции по его использованию.

## Структура проекта
<pre>
DRFtask/
├──myapp
│   ├──frontand
│   │   ├── migrations
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── views.py
│   ├──myapp
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   ├──templates
│   │   ├── task_list.html
│   ├──manage.py
│   ├──requirements.txt


Использование:
создаём супер юзера с помощью команды python manage.py createsuperuser
запускаем сервер с помощью команды python manage.py runserver
перходим по адрессу http://127.0.0.1:8000/admin/
и можем создавать задачи которые после создания выведутся в html файл 

pip install -r requirements.txt Настройка Перед использованием проекта, убедитесь, что вы настроили переменные окружения в файле .env. Подставьте свои настройки базы данных, секретный ключ и другие конфигурации.

