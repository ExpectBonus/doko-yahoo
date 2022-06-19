FROM python:3.7
ENV PYTHONUNBUFFERED 1

WORKDIR /server
ADD . /server/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# RUN flask db init
# RUN flask db migrate -m "run flask db migrate"
# RUN flask db upgrade
