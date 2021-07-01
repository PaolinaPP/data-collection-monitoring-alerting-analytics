FROM python:3-onbuild
COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip3 install -r requirements.txt
CMD ["python3", "log-restapi.py"]