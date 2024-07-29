@echo off
echo Pulling Docker image from Docker Hub...
docker pull xferax/flask-app:1.2

echo Running Docker container...
docker run -d -p 5000:5000 --name flask_app xferax/flask-app:1.2

echo Docker container is up and running.
pause
