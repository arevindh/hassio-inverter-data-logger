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
RUN git clone https://github.com/XtheOne/Inverter-Data-Logger.git && \
    cd Inverter-Data-Logger && \
    git checkout aca616931090ee9de4ae69076c6ec56bc42c4e38 && \
    rm -rf .git
RUN apk del git

# TODO: Fix properly upstream
RUN apk add --no-cache sed
RUN sed -i  's/(now.minute % 5) == 0/True/' /Inverter-Data-Logger/outputs/PVoutputOutput.py
RUN apk del sed

# Add scripts
COPY write_config.py /Inverter-Data-Logger/write_config.py
COPY run.sh /Inverter-Data-Logger/run.sh

WORKDIR /Inverter-Data-Logger
CMD [ "./run.sh" ]
