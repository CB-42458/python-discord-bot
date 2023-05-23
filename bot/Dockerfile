# use multi-architecture base image
FROM --platform=$BUILDPLATFORM python:3.11.2-slim-buster

# upgrade pip
RUN pip install --upgrade pip

# install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends gcc python3-dev

# copy requirements.txt and install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy the bot
COPY . /app
RUN chmod +x app/entrypoint.sh

# set the working directory
WORKDIR /app

# install the logger package
RUN pip install ./loggerPackage
RUN rm -rf ./loggerPackage/build
RUN rm -rf ./loggerPackage/logger.egg-info

ENV PYTHONUNBUFFERED=1
# run the bot
CMD ["python", "-u", "supervisor.py"]