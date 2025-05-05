import gradio as gr
import grpc
import image_generator_pb2
import image_generator_pb2_grpc
from PIL import Image
from io import BytesIO

def generate_image(prompt):
    try:
        channel = grpc.insecure_channel('localhost:50051')
        stub = image_generator_pb2_grpc.ImageGeneratorStub(channel)
        response = stub.GenerateImage(image_generator_pb2.ImageRequest(prompt=prompt))
        image = Image.open(BytesIO(response.image))
        return image
    except Exception as e:
        print(f"Error: {e}")
        return None

def run_gradio():
    with gr.Blocks() as demo:
        prompt = gr.Textbox(label="Prompt")
        output = gr.Image()
        demo_btn = gr.Button("Generate")
        demo_btn.click(generate_image, inputs=prompt, outputs=output)
    demo.launch(server_name="0.0.0.0", server_port=7000, share=True)

if __name__ == "__main__":
    run_gradio()
