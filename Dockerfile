# Use Alpine Linux as the base image for its minimal size
FROM alpine:latest

# Install Python and pip
RUN apk add --no-cache python3 py3-pip

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and text files into the container
COPY script.py /app/
COPY ./data/IF.txt /app/home/data/IF.txt
COPY ./data/Limerick-1.txt /app/home/data/Limerick-1.txt

# Create the output directory
RUN mkdir -p /app/home/output

# Command to run the Python script
CMD ["python3", "script.py"]
