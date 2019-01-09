FROM python:stretch

RUN pip install flask

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN ./bootstrap_transcode_server.sh

EXPOSE 8080

ENTRYPOINT ["python"]
CMD ["app.py"]
