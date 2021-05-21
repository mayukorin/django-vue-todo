FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /todo-docker
WORKDIR /todo-docker
COPY requirements.txt /todo-docker/
RUN pip install -r requirements.txt
COPY . /todo-docker/ 