# use multi-architecture base image
FROM --platform=$BUILDPLATFORM python:3.11.2-slim-buster

# upgrade pip
RUN pip install --upgrade pip

# set the working directory
WORKDIR /app

# copy the bot files
COPY . .

# install the requirements
RUN pip install --no-cache-dir -r requirements.txt

# install the logger package
RUN pip install ./loggerPackage
RUN rm -rf ./loggerPackage/build
RUN rm -rf ./loggerPackage/logger.egg-info

ENV PYTHONUNBUFFERED=1
# run the bot
CMD ["python", "-u", "supervisor.py"]