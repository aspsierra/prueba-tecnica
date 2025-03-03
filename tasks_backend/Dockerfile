FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache -r requirements.txt

COPY . /app/

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py db_seeder && python manage.py createsuperuser && python manage.py runserver 0.0.0.0:8000"]
