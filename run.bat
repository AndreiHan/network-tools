docker build -t network:latest .

docker run -d --name tools.network network:latest

docker exec -it tools.network python main.py

docker stop tools.network

docker rm tools.network

docker rmi network:latest