#!/usr/bin/env bash
set -e

# Start gRPC server in the background
python grpc_server.py &
SERVER_PID=$!

# Wait for the server to start listening on port 50051 (adjust port if needed)
echo "Waiting for gRPC server to become ready on localhost:50051..."
if command -v nc &> /dev/null; then
  while ! nc -z localhost 50051; do
    sleep 1
  done
else
  # fallback if netcat isn't installed
  echo "nc not found; sleeping for 5 seconds..."
  sleep 5
fi

echo "gRPC server is up!"

# Now launch the front-end
python grpc_front.py

# (optional) when front.py exits, kill the server
kill "$SERVER_PID"
