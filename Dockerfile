FROM python:2.7-stretch

RUN mkdir /work
ADD . /work/

ADD .docker-compose/script.sh /work/

WORKDIR /work/

CMD /work/script.sh