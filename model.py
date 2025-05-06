import torch 
from diffusers import StableDiffusionPipeline
import tqdm
pipe = StableDiffusionPipeline.from_pretrained("dreamlike-art/dreamlike-photoreal-2.0",torch_dtype=torch.float16)
# Move to GPU (optional)

pipe.save_pretrained("dreamlike-photoreal-2.0")
