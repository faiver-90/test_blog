# Запуск проекта

## Запуск с Docker
1. Убедитесь, что установлены Docker и Docker Compose.
2. Создайте `.env` файл с параметрами базы данных. Пример `.env_sample`
3. Запустите команду:
   ```bash
   docker-compose up --build -d
   ```
4. Остановка контейнеров:
   ```bash
   docker-compose down
   ```

## Запуск без Docker
1. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
2. Настройте базу данных PostgreSQL и создайте `.env` файл.
3. Примените миграции:
   ```bash
   python manage.py migrate
   ```
4. Запустите сервер:
   ```bash
   python manage.py runserver
   ```

## Данные супер-пользователя для админки
```bash
user_name = admin
password = 1234
```
