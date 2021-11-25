FROM python:3.9-slim-bullseye

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev && \
    apt-get install -y default-libmysqlclient-dev build-essential && \
    apt-get install nano
# set the working directory in the container
WORKDIR /app

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

EXPOSE 5566
# copy the content of the local src directory to the working directory
COPY . .
# command to run on container start
CMD [ "python", "./collector.py" ]