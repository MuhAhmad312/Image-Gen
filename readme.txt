Project README

This repository contains a GPU-enabled gRPC microservice running Dreamlike Photo Real 2.0 models. It includes both the backend gRPC server (grpc_server.py) and a client component (grpc_front.py), containerized with Docker and orchestrated via Docker Compose.

📋 Prerequisites

Docker (with NVIDIA Container Toolkit) installed on your machine

Docker Compose v2 (or the standalone plugin) available

NVIDIA GPU drivers compatible with CUDA 12.6 installed on the host

WSL 2 integration enabled (Windows users)

🔧 Setup

Clone the repository:

git clone https://github.com/MuhAhmad312/Image-Gen.git
cd your-repo

Prepare the model files:

Place your Dreamlike Photo Real 2.0 model checkpoint(s) in a local directory named models/.

Ensure the main model file (e.g. model.bin) is referenced by the MODEL_PATH environment variable in docker-compose.yml.

Ignore large files:

The .dockerignore file excludes the models/ folder from the build context.

🚀 Running with Docker Compose

Clean stale resources (optional but recommended):

docker builder prune -af
docker image prune -af

Build & start the service:

docker compose up --build

This:

Builds the Docker image using the Dockerfile (with CUDA 12.6 runtime)

Grants the container access to all GPUs

Mounts your local models/ directory into the container

Exposes gRPC on localhost:50051

Verify the container is running:

docker ps

Look for a service named grpc-app listening on port 50051.

View logs:

docker logs <container_id_or_name>

📡 Interacting with the Service

Use any gRPC client to connect to localhost:50051.

Load or update the model at MODEL_PATH inside the container (default: /app/models/model.bin).

🧹 Cleaning Up

To stop and remove containers:

docker compose down

To remove unused images and volumes:

docker system prune -af
docker volume prune -f

📝 License


there is no license we have no idea how this works if you get this
to work koodos you have done something that we were not able 
to do especially while using docker
