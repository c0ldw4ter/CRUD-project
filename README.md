# Сайт написан на Python\Django + БД PostgreSQL
## Для запуска:
- Скланировать репозиторий и перейти в директорию проекта
- python -m venv venv
- . ./venv/bin/activate
- pip install -r requirements.txt
- Нужно создать базу данных django, пользователя django_admin, с паралоем django
- Затем нужно совержить миграцию для базы данных sqlite3
- Затем создаём дамп базы данных(python -Xutf8 manage.py dumpdata -o data.json)
- Подключаем PostgreSQL и синхранизируем её (python manage.py migrate --run-syncdb)
- Загружаем дамп в новую базу(python manage.py loaddata data.json)
### Теперь можно запускать
-  cd visited_city
- python manage.py runserver
