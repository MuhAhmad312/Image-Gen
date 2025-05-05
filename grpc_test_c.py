from multiprocessing import Process
import grpc
from io import BytesIO
from PIL import Image
import image_generator_pb2
import image_generator_pb2_grpc

def make_grpc_request(i):
    prompt = f"mechanical keyboards {i}"
    try:
        # Set up gRPC channel and stub
        channel = grpc.insecure_channel('localhost:50051')
        stub = image_generator_pb2_grpc.ImageGeneratorStub(channel)

        # Send request
        request = image_generator_pb2.ImageRequest(prompt=prompt)
        response = stub.GenerateImage(request)

        # Save the image
        image = Image.open(BytesIO(response.image))
        image.save(f"generated_image_{i}.png")
        print(f"[User {i}] Image saved as generated_image_{i}.png")

    except grpc.RpcError as e:
        print(f"[User {i}] gRPC Error: {e.code()} | {e.details()}")
    except Exception as e:
        print(f"[User {i}] Unexpected Error: {e}")

if __name__ == "__main__":
    num_users = 10
    processes = []

    for i in range(num_users):
        p = Process(target=make_grpc_request, args=(i,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
