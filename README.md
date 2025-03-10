# Cafe EM

**Cafe EM** - это веб-приложение для управления заказами в кафе.

![orders.png](readme_images/orders.png)

# Содержание

- **[Технологии и инструменты](#технологии-и-инструменты)**
- **[Функциональсть](#функциональность)**
- **[API](#api)**
- **[Установка и запуск](#установка-и-запуск)**

## Технологии и инструменты

### Языки программирования и фреймворки

- **Python 3.11**
- **Django 5**

### Инструменты разработки
- **Mypy**
- **Flake8**
- **Black**
- **Isort**
- **Pre-commit**
- **Poetry**
- **Git**
- **GitHub**

### Базы данных
- **PostgreSQL**

### Web технологии
- **HTML**
- **CSS**
- **JavaScript**
- **JQuery**

### Серверные технологии и безопасность
- **CSP**

## Функциональность
- ### Просмотр заказов - страница с общей таблицей всех заказов ```orders/```

![orders.png](readme_images/orders.png)

Каждая запись кликабельна и ведет на адрес ```orders/<int:pk>/update/```.

На странице работает поиск по № стола и статусу заказа.

Также на странице есть автоматический расчет выручки по заказам со статусом «Оплачено».

- ### Добавление заказа - страница с формой добавления заказа ```orders/create/```

![create_order.png](readme_images/create_order.png)

- ### Редактирование заказа - страница с формой изменения заказа ```orders/<int:pk>/update/```

![update_order.png](readme_images/update_order.png)

- ### Удаление заказа - страница с формой удаления заказа ```orders/<int:pk>/delete/```

![delete_order.png](readme_images/delete_order.png)

## API

OpenAPI - ```/api/redoc/```

![open_api.png](readme_images/open_api.png)

## Установка и запуск

### 1. Создайте .env в корневом каталоге проекта или запустите файл init_env.py:

- **Запустите файл init_env.py:**

```
python init_env.py
```

- **Создайте .env в корневом каталоге проекта:**

```dotenv
# .env

# DJANGO SECRET KEY
SECRET_KEY=...

# DJANGO DEBUG
DEBUG=True

# DATABASE CONNECT SETTINGS
POSTGRES_DB=...
POSTGRES_USER=...
POSTGRES_PASSWORD=...
```

### 2. Установите зависимости проекта:

```shell
poetry install
```

***Подробнее о poetry***: https://python-poetry.org

### 3. Запустите проект:

- **Через Make** ```make run-dev```
- **Через консоль** ```poetry python manage.py runserver```
