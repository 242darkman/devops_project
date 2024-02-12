FROM postman/newman:5.3.1-alpine

WORKDIR /etc/newman

RUN npm install -g newman-reporter-htmlextra

ENTRYPOINT ["newman"]