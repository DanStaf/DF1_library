# DF1 / API для управления библиотекой

### Описание API:

API для управления библиотекой. API предоставляет возможности для управления книгами, авторами и пользователями, а также для отслеживания выдачи книг пользователям. Для реализации API используется Django Rest Framework (DRF).

### Функционал API:

1. **Управление книгами**: 
   - Создание, редактирование и удаление книг.
   - Получение списка всех книг.
   - Поиск книг по различным критериям (название, автор, жанр и т.д.).
2. **Управление авторами**: 
   - Создание, редактирование и удаление авторов.
   - Получение списка всех авторов.
3. **Управление пользователями**: 
   - Регистрация и авторизация пользователей.
   - Получение информации о пользователях.
   - Реализована авторизация с использованием JSON Web Token для защиты API и управления сеансами пользователей 
   - В проекте произведено разделение прав доступа, введены роли пользователей (менеджер, читатель)
4. **Выдача книг**: 
   - Запись информации о выдаче книги пользователю.
   - Отслеживание статуса возврата книги.
    
### ИНСТРУКЦИЯ ПО ЗАПУСКУ:

### Структура проекта:

1. **Фреймворк**: 
   - Для реализации проекта используется фреймворк Django и Django Rest Framework (DRF).
2. **База данных**: 
   - PostgreSQL используется для хранения данных.
3. **Контейнеризация**: 
   - Для контейнеризации приложения используется Docker и Docker Compose.
4. **Доступные urls**:
   
Административная панель:
   - /admin/
   
Приложение "libr" (библиотека):
   - /authors/
   - /books/
   - /readings/
   
Приложение "users" (пользователи):
   - /users/
   - /users/login/
   - /users/token/refresh/
   - /users/email_confirm/

Автогенерируемая документация API по стандарту OpenAPI:
   - /swagger/
   - /redoc/
   





    
---

---

---

## Developing Steps

1. add .gitignore, .env, readme
2. setup Poetry, DB and Django
```
/settings/Python interpreter/Add interpreter/Poetry environment 
create DB "library"
poetry add django==4.2 python-dotenv psycopg2
django-admin startproject config .
python manage.py startapp libr
python manage.py startapp users

setup settings.py
```
3. setup User
```
poetry add djangorestframework djangorestframework-simplejwt django-filter
```
- config.settings.py
- config.urls
- models
- admin
- permissions
- serializers
- csu `python manage.py csu`
- urls
- views

3. setup models / book, author, reading
- models
- admin

4. setup simple endpoints
- serializers
- urls
- views (CRUD)

5. setup custom endpoints (filter books, book status)
- urls
- views
- (serializers)

---


9. Другое

- readme
- Документация
`poetry add drf-yasg`

- fixtures
`python -Xutf8 manage.py dumpdata libr > fixtures/libr_data.json --indent=4`
`python -Xutf8 manage.py dumpdata auth > fixtures/auth_data.json --indent=4`
`python -Xutf8 manage.py dumpdata users > fixtures/users_data.json --indent=4`

9. Docker
- Dockerfile and docker-compose.yaml
- .env and .env.sample and settings
- `pip freeze > requirements.txt`
- readme.md
