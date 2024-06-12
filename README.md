# Тестовое задание на позицию стажёра в IT-Solutuions
Вакансия: https://career.habr.com/vacancies/1000143441

---
## Аккаунт суперюзера:
#### username: admin
#### password: admin
#### access токен JWT:
```
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIwNzkxNzcwLCJqdGkiOiI3Y2RmOTU5Y2YzNjA0NGE3OWU1YWZkZWQwNTQ2ZDkzNyIsInVzZXJfaWQiOjF9.G5UQ9cCBXDZcxlj5ilhytTtxuhPWVcucsjpUB0ngKOs
```
---
## Запуск проекта:
Клонируйте репозиторий:
```
git clone git@github.com:We1der/api_farpost.git
```

Создайте и запустите виртуальное окружение, а затем установите нужные модули и библиотеки:
```
python -m venv venv
source venv/Scripts/activate
pip install requirements.txt
```

Перейдите в папку api_farpost и запустите проект:
```
cd api_farpost
python manage.py runserver
```
---
## Для аутентификации в Headers запроса нужно передать токен доступа:
```
Authorization: Bearer <acces token>
```
---
## Доступные endpoints:
- http://127.0.0.1:8000/auth/users/ - [POST] создаёт нового пользователя, в заголовки нужно передать username и password;
- http://127.0.0.1:8000/auth/jwt/create - [POST] создаёт JWT токен для аутентификации;
- http://127.0.0.1:8000/announcements/ - [GET, POST] возвращает коллекцию объявлений или создаёт новое;
- http://127.0.0.1:8000/announcements/<id> - [GET, PUT, PATCH, DELETE] возвращает, обновляет или удаляет объявления по одному;
- http://127.0.0.1:8000/authors/ - [GET] возвращает коллекцию авторов/пользователей;
- http://127.0.0.1:8000/authors/<id> - [GET] возвращает конкретного автора/пользователя.
