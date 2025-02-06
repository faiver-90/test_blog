# Запуск проекта

## Запуск с Docker с нуля
1. Убедитесь, что установлены Docker и Docker Compose.
2. Клонируйте репозиторий и перейдите в папку проекта:
   ```bash
   git clone https://github.com/faiver-90/test_blog.git my_project
   cd my_project
   ```
3. Создайте `.env` файл с параметрами базы данных. Пример `.env_sample`.
4. Соберите и запустите контейнеры:
   ```bash
   docker-compose up --build -d
   ```
5. Примените миграции вручную (если не выполняются автоматически):
   ```bash
   docker-compose exec django python manage.py migrate
   ```
6. Создайте суперпользователя (если он не был создан автоматически):
   ```bash
   docker-compose exec django python manage.py createsuperuser
   ```
7. Проверьте, что сервер запущен на `http://localhost:8000`

8. Остановка контейнеров:
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
5. Создайте `.env` файл с параметрами базы данных. Пример `.env_sample`.
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

## Данные суперпользователя для админки
- `user_name = admin`
- `password = 1234`