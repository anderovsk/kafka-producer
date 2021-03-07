FROM python:3.7.10-alpine3.12
WORKDIR /app
ADD app.py /app/app.py
ADD requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt
ENTRYPOINT [ "python3", "/app/app.py" ]