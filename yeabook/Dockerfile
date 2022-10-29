FROM python:3.11

WORKDIR /opt/yeabook
COPY . .
RUN chmod 777 /opt/yeabook/entrypoint.sh

RUN apt -y update \
    && apt -y install netcat

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip \
     && pip install -r requirements.txt

ENTRYPOINT ["/opt/yeabook/entrypoint.sh"]
