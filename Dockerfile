FROM python:3.8

WORKDIR "/srv/web/three"

RUN apt-get update && apt-get install -y nano default-mysql-client

RUN pip install gunicorn

RUN echo 'alias l="ls -al"' >> ~/.bashrc
RUN echo 'alias pm="python manage.py"' >> ~/.bashrc
RUN echo 'alias pmr="python manage.py runserver 0.0.0.0:8000"' >> ~/.bashrc
RUN echo 'alias pvb="python manage.py varnish-ban "' >> ~/.bashrc

ADD requirements.txt /srv/web/three

RUN pip install -r /srv/web/three/requirements.txt --upgrade

CMD ["/bin/bash"]
