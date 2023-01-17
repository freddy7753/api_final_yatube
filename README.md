# Описание проекта
## api_final_yatube 
#### Учебный проект сайта разрабатываемая в Django_rest_framework.
#### Здесь присутствует такие возможности сайта как: 
> - Создаине и редактирование поста, комментария к постам
> - Возможность аутентификации и подписки на автора поста
#### Все реализованно с помощью API

# Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/api_final_yatube
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

# Примеры запросов к API

Получение постов:
```
http://127.0.0.1:8000/api/v1/posts/
```
Список сообществ:
```
http://127.0.0.1:8000/api/v1/groups/
```
Подписка:
```
http://127.0.0.1:8000/api/v1/follow/
```
Получение токена:
```
http://127.0.0.1:8000/api/v1/jwt/create/
```




