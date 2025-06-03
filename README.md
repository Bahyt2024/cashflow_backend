# cashflow_backend
## Настройка окружения

Для корректной работы проекта необходимо создать файл `.env` в корне проекта с такими переменными окружения:

```env
DEBUG=True
SECRET_KEY=django-insecure-=$4yzv=ow$&%6zsqic*q(r-!2ljf0_+q8%#a$%%7hm=yisf^ya

DB_NAME=dds
DB_USER=postgres
DB_PASSWORD=1234
DB_HOST=localhost
DB_PORT=5432

EMAIL_HOST_USER=example@gmail.com
EMAIL_HOST_PASSWORD=your-email-password(Нужен пароль приложений)


pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

