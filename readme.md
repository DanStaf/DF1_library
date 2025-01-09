# DF1 / API для управления библиотекой


### Описание задачи:

Необходимо разработать REST API для управления библиотекой. API должно предоставлять возможности для управления книгами, авторами и пользователями, а также для отслеживания выдачи книг пользователям. Для реализации API использовать Django Rest Framework (DRF).


### Задача:

1. Реализовать API для управления библиотекой.
2. Обеспечить аутентификацию и авторизацию пользователей с использованием JWT токенов.
3. Обеспечить возможности для управления книгами и авторами.
4. Реализовать функционал для отслеживания выдачи книг.


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
4. **Выдача книг**: 
   - Запись информации о выдаче книги пользователю.
   - Отслеживание статуса возврата книги.

    
### Технические требования:

1. **Фреймворк**: 
   - Использовать фреймворк Django и Django Rest Framework (DRF) для реализации проекта.
2. **База данных**: 
   - Использовать PostgreSQL для хранения данных.
3. **Контейнеризация**: 
   - Использовать Docker и Docker Compose для контейнеризации приложения.
4. **Документация**: 
   - В корне проекта должен быть файл README.md с описанием структуры проекта и инструкциями по установке и запуску.\\
   - Реализовать автогенерируемую документацию API по стандарту OpenAPI
5. **Качество кода**: 
   - Соблюдать стандарты PEP8.
   - Весь код должен храниться в удаленном Git репозитории.





Реализована авторизация с использованием JSON Web Token для защиты API и управления сеансами пользователей

В проекте произведено разделение прав доступа /введены роли пользователей



    
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
- urls
- views
- csu `python manage.py csu`

3. setup Habit model
- models
- admin

4. setup Habit endpoints
- paginators
- serializers
- urls
- views (CRUD)

5. setup public habits
- urls
- views

6. Валидаторы
- validators
- serializers

7. Телеграм
- poetry add celery django-celery-beat redis eventlet
- config: settings, celery.py, tasks, services / migrate
- https://t.me/BotFather
- https://core.telegram.org/bots/api
- poetry add telebot
- add tg_id to user model
- config: env, settings, tasks, services

8. Другое
`poetry add django-cors-headers drf-yasg coverage flake8`
- CORS 
- Документация
- Тесты
- Flake8
- fixtures
`python -Xutf8 manage.py dumpdata spa > fixtures/spa_data.json --indent=4`
`python -Xutf8 manage.py dumpdata auth > fixtures/auth_data.json --indent=4`
`python -Xutf8 manage.py dumpdata users > fixtures/users_data.json --indent=4`

9. Docker
- Dockerfile and docker-compose.yaml
- .env and .env.sample and settings
- `pip freeze > requirements.txt`
- readme.md
