# 📝 Django Ninja Blog

Этот проект представляет собой блог, реализованный на Django Ninja, с поддержкой JWT-аутентификации, управления пользователями, статьями и комментариями. Он предназначен для демонстрации навыков работы с Django, Ninja API и контейнеризацией через Docker.

## 🚀 Возможности

### Аутентификация
- **POST /auth/token/** – Получение токена доступа.
- **POST /auth/token/refresh/** – Обновление токена.
- **GET /auth/validate/** – Проверка валидности токена.

### Управление пользователями
- **POST /user/create_user/** – Создание нового пользователя.
- **PUT /user/update_user/** – Обновление информации о пользователе.
- **POST /user/get_user_by_token/** – Получение данных о пользователе по токену.
- **DELETE /user/delete_user/{user_id}** – Удаление пользователя.

### Статьи
- **POST /article/create_article/** – Создание статьи.
- **PUT /article/update_article/{article_id}** – Обновление статьи.
- **DELETE /article/delete_article/{article_id}** – Удаление статьи.
- **GET /article/get_article/{article_id}** – Получение статьи по ID.

### Комментарии
- **POST /comments/add_comment/** – Добавление комментария к статье.
- **DELETE /comments/delete_comment/{comment_id}** – Удаление комментария.

## 📦 Установка и запуск

### 1. Клонирование репозитория
```bash
git clone https://github.com/faiver-90/test_blog.git .
```

### 2. Установка зависимостей
```bash
python -m venv venv
source venv/bin/activate  # для Linux/MacOS
venv\Scripts\activate  # для Windows
pip install -r requirements.txt
```

### 3. Запуск сервера
```bash
python manage.py migrate
python manage.py runserver
```

Сервис будет доступен по адресу: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### 4. Запуск через Docker

Создайте `.env` файл с переменными окружения по образцу .env_sample

Запустите проект через Docker Compose:
```bash
docker-compose up --build -d
```

## 📚 Технологии
- **Django** – Основной бэкенд
- **Django Ninja** – Оптимизированный API-интерфейс
- **JWT** – Аутентификация
- **PostgreSQL** – База данных
- **Docker** – Контейнеризация
