# -------------------------------------------------------------------
# Stage 0: Base image with CUDA runtime (CUDA 12.6 slim)
# -------------------------------------------------------------------
FROM nvidia/cuda:12.6.0-runtime-ubuntu22.04

# avoid interactive prompts and keep image small
ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1

# install Python 3 and pip, then clean up apt caches
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
      python3.10 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# -------------------------------------------------------------------
# Stage 1: Application
# -------------------------------------------------------------------
WORKDIR /app

# copy & install only your Python dependencies
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# copy your entire codebase
COPY . .

# expose your gRPC port
EXPOSE 50051

# launch server & client in the same container
CMD ["bash", "-c", "\
    python3 grpc_server.py & \
    python3 grpc_front.py \
"]
