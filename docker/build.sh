# build mysql
docker build -t iterator/mysql:latest ./mysql

# build python
docker build -t iterator/python:latest ./python

# build nginx
docker build -t iterator/nginx:latest ./nginx

# build newman
docker build -t iterator/newman:latest ./newman