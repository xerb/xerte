FROM ubuntu:18.04

COPY . /app
WORKDIR /app

RUN apt-get update -qq && apt-get install -y \
  python3-pip \
  wget

RUN pip3 install flask && pip3 install -r requirements.txt

RUN pip3 install -r requirements.txt

RUN apt-get install -y ffmpeg

RUN ./set_up_mp4box.sh

EXPOSE 8080

ENTRYPOINT ["python3"]
CMD ["app.py"]
