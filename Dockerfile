FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /workplace
WORKDIR /workplace
ADD requirements.txt /workplace/
RUN pip3 install pip
RUN pip3 install -r requirements.txt
ADD ./ /workplace/


