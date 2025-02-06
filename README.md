# Запуск проекта

## Запуск с Docker
1. Убедитесь, что установлены Docker и Docker Compose.
2. Создайте `.env` файл с параметрами базы данных. Пример `.env_sample`
3. Запустите команду:
   ```bash
   docker-compose up --build - d
   ```
4. Остановка контейнеров:
   ```bash
   docker-compose down
   ```

## Запуск без Docker
1. Создайте и перейдите в новую папку проекта:
   ```bash
   mkdir my_project && cd my_project
   ```
2. Клонируйте репозиторий и перейдите в него:
   ```bash
   git clone https://github.com/faiver-90/test_blog.git .
   ```
3. Создайте виртуальное окружение и активируйте его:
   ```bash
   python -m venv env
   source env/bin/activate  # Для macOS/Linux
   env\Scripts\activate  # Для Windows
   ```
4. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
5. Создайте `.env` файл с параметрами базы данных. Пример `.env_sample`
6. Примените миграции:
   ```bash
   python manage.py migrate
   ```
7. Создайте суперпользователя:
   ```bash
   python manage.py createsuperuser
   ```
8. Запустите сервер:
   ```bash
   python manage.py runserver
   ```
   
## Данные супер-пользователя для админки
```bash
   user_name = admin
   password = 1234
```

