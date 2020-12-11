FROM python:3
LABEL author="Isilindil <isilindil@hydraa.be>"

RUN apt-get update \
    && apt-get install -y vim git \
    && mkdir /Data

#RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /opt/adventofcode/

VOLUME /Data

CMD [ "/bin/bash" ]
