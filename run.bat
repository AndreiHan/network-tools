docker build -t network:latest .

docker run -d --name tools.network network:latest

docker exec -it tools.network python main.py

docker stop -f tools.network

docker rm -f tools.network

docker rmi -f network:latest