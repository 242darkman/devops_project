FROM postman/newman:5.3.1-alpine

WORKDIR /etc/newman

COPY collections/iterator-test-nrg.json /etc/newman/
COPY environments/int.postman_environment.json /etc/newman/

CMD ["run", "iterator-test-nrg.json", "-k", "-e", "int.postman_environment.json", "-r", "cli,json", "--reporter-json-export=collections/iterator-test.ng"]