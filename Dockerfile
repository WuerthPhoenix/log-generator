FROM python:3.12-alpine

COPY . /log-generator
RUN cd /log-generator &&\
    python setup.py install

ENTRYPOINT [ "rlog-generator"]