FROM python:3-onbuild
COPY . /usr/src/alertmanager
WORKDIR /usr/src/alertmanager
RUN pip3 install -r requirements.txt
CMD ["python3", "alerting.py"]