FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /instagram_django
COPY requirements.txt /instagram_django/requirements.txt
RUN pip install -r requirements.txt
COPY . /instagram_django