FROM python:3.14.10-slim-bookworm

WORKDIR /usr/src/app

# set environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
    && apt-get -y install netcat-traditional gcc postgresql \
    && apt-get clean

# install python sependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .

# add entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod +x /usr/src/app/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]
