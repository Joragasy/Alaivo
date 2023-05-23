import numpy as np
from typing import Union, List, Optional , Dict
from fastapi import FastAPI 
from PIL import Image
from pydantic import BaseModel
from PIL import Image
from fastapi import File , UploadFile , Form , Depends
from utils import get_colored_mask , transform_white_to_transparent
from segment import  load_sam_predictor,  get_mask
from starlette.responses import StreamingResponse

app = FastAPI(
    title="Alaivo API"
)

sam_checkpoint = "./trained_model/sam_vit_b_01ec64.pth"
device = "cuda"
model_type = "vit_b" # "default" or "vit_b" or "vit_l"

predictor = load_sam_predictor(sam_checkpoint,device,model_type)

class Item(BaseModel):
    prompt : List[int]
    prompt_label : int
    img_path : str 

class Modelparam(BaseModel):
    image : UploadFile = File(...)
    # image : str

@app.get("/")
def root():
    return {"message": "Welcome to Alaivo , enjoy it"}

@app.post("/get_mask")
def create_item(item: Item):
    mask = get_mask(predictor,item.prompt,item.prompt_label,item.img_path)
    return {"mask": mask.tolist()}

@app.post("/upload_image")
async def get_image_from_client(image : UploadFile = File(...), prompt : List = Form(...) , prompt_label : List = Form(...)  ):
    with open("./images/temp_image_real.jpg", "wb") as temp_image:
        temp_image.write(await image.read())
    prompt = [float(x) for x in prompt[0].split(",")]
    prompt_label = int(prompt_label[0])
    img_path = "./images/temp_image_real.jpg"    
    mask = get_mask(predictor,prompt,prompt_label,img_path)
    # mask = get_colored_mask(mask)
    mask = np.where(mask == True, 0 , 255 )
    mask = np.array(mask,dtype=np.uint8)
    mask = Image.fromarray(mask, mode="L")
    mask = transform_white_to_transparent(mask)
    mask.save('./images/mask_tempo.png')
    with open('./images/mask_tempo.png', "rb") as file:
        image_bytes = file.read() 
    return StreamingResponse(iter([image_bytes]), media_type="image/png")
