FROM python:3.10

WORKDIR ./code

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./source .

CMD python manage.py runserver 0.0.0.0:8000 & python tg_bot/tg_bot.py
