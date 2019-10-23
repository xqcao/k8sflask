FROM python:alpine3.7

WORKDIR /helloapp

COPY .  /helloapp

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python","app.py"]