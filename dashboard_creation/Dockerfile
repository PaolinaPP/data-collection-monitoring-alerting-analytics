FROM python:3-onbuild
COPY . /usr/src/dashboard_creation
WORKDIR /usr/src/dashboard_creation
RUN pip3 install -r requirements.txt
CMD ["python3", "create_dashboards.py"]