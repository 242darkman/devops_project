# stop all docker
docker stop $(docker ps -q)

# remove the docker network
docker network rm $(docker network ls -q)

# remove docker container
docker rm $(docker ps -a -q)

# remove docker images
docker rmi $(docker images -q)