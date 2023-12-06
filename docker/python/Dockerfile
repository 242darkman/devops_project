FROM python:3-alpine

WORKDIR /usr/src/app

COPY backend/ ./

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pymysql sqlalchemy && \
    pip install --no-cache-dir uvicorn