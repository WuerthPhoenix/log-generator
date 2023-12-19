FROM python:3.11-bookworm

COPY . /log-generator
RUN cd /log-generator &&\
    python setup.py install

ENTRYPOINT [ "rlog-generator"]