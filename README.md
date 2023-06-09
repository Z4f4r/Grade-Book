# Django REST API

Это проект Django, предоставляющий REST API для управления курсами, студентами и оценками.

## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone <repository-url>
   ```

2. Установите необходимые зависимости:

   ```bash
   pip install -r requirements.txt
   ```

3. Настройте базу данных:

   ```bash
   python manage.py migrate
   ```

4. Запустите сервер разработки:

   ```bash
   python manage.py runserver
   ```

## Конечные точки API

- `GET /v1/course/` - Получить список всех курсов.
- `GET /v1/course/{id}/` - Получить детали определенного курса.
- `POST /v1/course/` - Создать новый курс.
- `PUT /v1/course/{id}/` - Обновить детали определенного курса.
- `DELETE /v1/course/{id}/` - Удалить определенный курс.

- `GET /v1/student/` - Получить список всех студентов.
- `GET /v1/student/{id}/` - Получить детали определенного студента.
- `POST /v1/student/` - Создать нового студента.
- `PUT /v1/student/{id}/` - Обновить детали определенного студента.
- `DELETE /v1/student/{id}/` - Удалить определенного студента.

- `GET /v1/grade/` - Получить список всех оценок.
- `GET /v1/grade/{id}/` - Получить детали определенной оценки.
- `POST /v1/grade/` - Создать новую оценку.
- `PUT /v1/grade/{id}/` - Обновить детали определенной оценки.
- `DELETE /v1/grade/{id}/` - Удалить определенную оценку.

- `GET /v1/filter/course/title/{title}/` - Фильтровать курсы по названию.
- `GET /v1/filter/grade/value/{value}/` - Фильтровать оценки по значению.
- `GET /v1/filter/grade/date/` - Фильтровать оценки по дате.
- `GET /v1/filter/student/first-name/{name}/` - Фильтровать студентов по имени.
- `GET /v1/search/student/{name}/` - Поиск студентов по имени.
- `GET /v1/search/course/{title}/` - Поиск курсов по названию.

## Внесение вклада

Ваши вклады приветствуются! Если вы обнаружили какие-либо проблемы или хотите добавить новые функции, пожалуйста, откройте issue или отправьте pull request.

## Требования

- Python 3.7 и выше
- Django 3.2 и выше
- Django Rest Framework 3.12 и выше