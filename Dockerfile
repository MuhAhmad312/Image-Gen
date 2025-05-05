
# -------------------------------------------------------------------
# Stage 0: Base image with CUDA runtime (smallest official CUDA image)
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
    
    # copy and install only your Python dependencies
    COPY requirements.txt .
    RUN pip3 install --no-cache-dir -r requirements.txt
    
    # copy your service code
    # assume you have two folders: /backend and /frontend
    COPY . .
    
    # expose your gRPC port (adjust if needed)
    EXPOSE 50051
    
    # entrypoint: launch both backend and frontend
    # adjust the commands below to the actual startup scripts/filenames you have
    CMD ["bash", "-c", "\
        python3 grpc_server.py & \
        python3 grpc_front.py \
    "]
    