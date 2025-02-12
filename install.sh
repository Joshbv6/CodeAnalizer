#!/bin/bash

# Navigate to the Docker directory
cd ./Docker

# Build the Docker image
docker build -t codeanalizer_image .

# Start the project using docker-compose
docker-compose -p codeanalizer_project up -d

# Notify the user that the app has been installed successfully
notify-send "App has been installed successfully!"

# Open the app in the default web browser
xdg-open http://localhost:8000