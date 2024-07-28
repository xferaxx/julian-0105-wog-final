שלב 1

first of all i made a Dockerfile with this content:

# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=main_score.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run Flask when the container launches
CMD ["flask", "run"]

########################################################

שלב 2

DOCKER COMMANDS THAT I USED TO CREATE THE CONTAINER

1) cd C:\Users\PC\PycharmProjects\wog = (go to the project Folder)


2) docker build -t flask-app:1.2 . = (i build the image)


3) docker images = (to see my images)
i got this output :
REPOSITORY        TAG       IMAGE ID       CREATED          SIZE
flask-app         1.2       a88cd75abadf   56 seconds ago   264MB


4) docker run -d -p 5000:5000 flask-app:1.2 = (to run the image that i created)
i got this output : 76b01bd297ecd5d15700438bcc9563f119d3b80418b2d9127ae01e4b8706d0b9


5) docker ps = (to see the running containers)
i got this output :
CONTAINER ID   IMAGE           COMMAND       CREATED         STATUS         PORTS                    NAMES
40ec49235b20   flask-app:1.2   "flask run"   10 seconds ago   Up 9 seconds    0.0.0.0:5000->5000/tcp   crazy_shamir



and if you run http://localhost:5000/ you will see the WEBSITE running and the score is showed up 
            or http://127.0.0.1:5000/


###########################################

how i created this YML:
docker-compose.yml
content:


version: '3.8'

services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "5000:5000"
    image: xferax/flask-app:1.2
    environment:
      - FLASK_APP=main_score.py
      - FLASK_RUN_HOST=0.0.0.0


navigating to the project folder and run:

1)docker-compose build = (Build the docker image)


2)docker-compose up = (Run the docker contianer)

         this is the out put that the flask server is running:

 * Serving Flask app 'main_score.py'
web-1  |  * Debug mode: off
web-1  | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
web-1  |  * Running on all addresses (0.0.0.0)
web-1  |  * Running on http://127.0.0.1:5050


3)docker-compose push = (Push the docker image to docker hub)


you can use >>>>> ( docker pull xferax/flask-app ) to download the image from docker hub


###########################################


Jenkins 

i open Jenkins and Run and i created an agent
then i created a Pipeline called pip-flask01

and i created a stage to checkout the project from GitHub
then to build a docker image for that project
after that we run the docker container
then we test the flask server 
and at the end if all is succeed we push the new image we created to docker hub


when Jenkins is building we can check the image and the container if all is working live

use command: docker ps

we will see the container is running and the flask server is running on port 8777

CONTAINER ID   IMAGE            COMMAND       CREATED          STATUS          PORTS                    NAMES
3cce3eb907eb   jenkinsimg:0.2   "flask run"   28 seconds ago   Up 26 seconds   0.0.0.0:8777->5000/tcp   flask_app

if we run 127.0.0.1:8777 we can see the score 

after that the container is being removed

and the imaged pushed to DockerHub

if you want to download the image from docker hub

use the command: docker pull xferax/jenkinsimg

