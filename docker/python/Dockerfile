FROM python:3-alpine

WORKDIR /usr/src/app

COPY backend/ ./

RUN pip install mysql-connector-python

EXPOSE 8000

# run the project
CMD ["python", "main.py"]
