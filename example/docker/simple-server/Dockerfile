FROM python:3
#FROM balenalib/raspberry-pi-python

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3-pip \
        python3-setuptools \
        locales locales-all 

# set timezone to Europ/Berlin
RUN ln -fs /usr/share/zoneinfo/Europe/Berlin /etc/localtime
RUN dpkg-reconfigure -f noninteractive tzdata

RUN pip3 install --upgrade pip
#RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3

RUN pip3 install fastapi uvicorn aiofiles

WORKDIR /app
COPY server.py server.py

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80"]




