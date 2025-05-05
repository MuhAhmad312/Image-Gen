import torch
from concurrent import futures
import grpc
from diffusers import DiffusionPipeline
from io import BytesIO
import image_generator_pb2
import image_generator_pb2_grpc
import os

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

pipe = DiffusionPipeline.from_pretrained(
    "./dreamlike-photoreal-2.0",
    torch_dtype=torch.float16,
    use_safetensors=True
)
pipe.to("cuda")

class ImageGenServicer(image_generator_pb2_grpc.ImageGeneratorServicer):
    def GenerateImage(self, request, context):
        try:
            image = pipe(request.prompt).images[0]
            img_bytes = BytesIO()
            image.save(img_bytes, format="PNG")
            return image_generator_pb2.ImageResponse(image=img_bytes.getvalue())
        except Exception as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return image_generator_pb2.ImageResponse()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=8))
    image_generator_pb2_grpc.add_ImageGeneratorServicer_to_server(ImageGenServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server running on port 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
