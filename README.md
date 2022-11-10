
docker build -t promaxima .

sudo docker run -it -p 8080:8080 --rm --name promaxima promaxima


Backend

sudo docker-compose up --build