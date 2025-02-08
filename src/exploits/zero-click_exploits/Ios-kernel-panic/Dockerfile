# Use an official Ubuntu base image
FROM ubuntu:20.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libpcap-dev \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy the project files to the container
COPY . /app

# Compile the project
RUN gcc -o CVE-2021-1965-poc CVE-2021-1965-poc.c -lpcap

# Set the entry point for the container
ENTRYPOINT ["./CVE-2021-1965-poc"]
