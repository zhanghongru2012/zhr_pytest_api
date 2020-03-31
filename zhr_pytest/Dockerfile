FROM python:3.7

RUN mkdir /root/.pip/
COPY pip.conf /root/.pip
RUN pip install requests
RUN pip install pytest
RUN pip install pytest-html
RUN pip install pytest-sugar
RUN pip install pytest-rerunfailures
RUN pip install allure-pytest
RUN pip install coverage
RUN pip install pytest-cov


WORKDIR /usr/src/app
