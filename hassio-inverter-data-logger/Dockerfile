ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Install python and required plugins
RUN apk add --no-cache python3 && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi
RUN pip install --no-cache six pytz

# Clone Inverter-Data-Logger
RUN apk add --no-cache git
WORKDIR /
RUN git clone https://github.com/silvester747/Inverter-Data-Logger.git && \
    cd Inverter-Data-Logger && \
    git checkout 519f49c86cd5f1474c8fe40ec51a0edc17062cab && \
    rm -rf .git
RUN apk del git

# Add scripts
COPY write_config.py /Inverter-Data-Logger/write_config.py
COPY run.sh /Inverter-Data-Logger/run.sh

WORKDIR /Inverter-Data-Logger
CMD [ "./run.sh" ]
