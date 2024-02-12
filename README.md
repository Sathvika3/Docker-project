# Docker Python Application Project

This project contains a Dockerized Python application that performs several tasks with text files, demonstrating basic Docker functionality and Python scripting.

## Features

- Starts from a lightweight Python base image.
- Includes a Python script that:
  - Lists names of all text files in a specified directory.
  - Counts the total number of words in each text file.
  - Calculates the grand total of words across all files.
  - Identifies the top 3 most frequent words in a specific file.
  - Finds the IP address of the container.
  - Writes all output to a specified result file and prints the contents to the console.

## Prerequisites

- Docker installed on your machine. Visit [Docker's official website](https://www.docker.com/products/docker-desktop) for installation instructions.

## Project Structure

/docker-python-app
├── Dockerfile

├── script.py

└── data/

├── IF.txt

└── Limerick-1.txt

Quick Start
Follow these steps to get the project up and running:

1. Build the Docker Image :Navigate to the root of the project directory and run the following command to build your Docker image:

      --> docker build -t my-python-app .

   This command creates a Docker image named my-python-app based on the Dockerfile in the current directory.

3. Run the Docker Container :Execute the following command to run the Docker container from the image you just built:

   --> docker run my-python-app

   This will start the container, execute the Python script, and display the results in the console.

4. Save the Docker Image (Optional) :To save the Docker image to a tar file for distribution or backup, use:

   --> docker save my-python-app > proj2docker_rk.tar

5. Load the Docker Image (Optional) :On another system with Docker installed, you can load the saved image from the tar file with:
   
   --> docker load < proj2docker_rk.tar

