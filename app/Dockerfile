FROM python:3.10-slim

RUN mkdir /usr/src/app
COPY . /usr/src/app
RUN pip install -r /usr/src/app/requirements.txt

RUN pip install https://github.com/napakalas/fc-pmr-search/releases/download/v0.0.1-alpha/pmrsearch-0.0.1-py3-none-any.whl
