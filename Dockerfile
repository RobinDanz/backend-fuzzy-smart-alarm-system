FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /api/

COPY . ./

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000



