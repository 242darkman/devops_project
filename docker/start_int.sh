# create network of instruction
docker network create --subnet=172.22.0.0/16 intNetwork 

# add mysql to the network integration
docker run --net intNetwork --ip 172.22.0.2 -dti --name mysqlIntContainer iterator/mysql:latest

# add python API to the network integration
docker run --net intNetwork --ip 172.22.0.3 -dti --name pythonContainer iterator/python:latest

# add nginx to the network integration
docker run --net intNetwork --ip 172.22.0.4 -dti --name nginxContainer iterator/nginx:latest

# add newman to the network integration
docker run --net intNetwork --ip  172.22.0.5 -dti --name newmanContainer iterator/newman:latest