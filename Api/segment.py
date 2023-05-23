import numpy as np
import torch
import matplotlib.pyplot as plt
import cv2
from segment_anything import sam_model_registry, SamPredictor
from utils import read_image

def load_sam_predictor(model_checkpoint,device, model_type):
    sam = sam_model_registry[model_type](checkpoint=model_checkpoint)
    sam.to(device=device)
    predictor = SamPredictor(sam)
    return predictor

def load_image_to_model(predictor,image):
    predictor.set_image(image)

def find_mask(predictor,prompt,prompt_label):
    masks, scores, logits = predictor.predict(
        point_coords=prompt,
        point_labels=prompt_label,
        multimask_output=True,
    )
    best_mask = np.argmax(np.array(scores)) 
    return masks[best_mask] , max(list(scores))

def get_mask(predictor,prompt,prompt_label,img_path):
    prompt = np.array([prompt])
    prompt_label = np.array([prompt_label])
    image = read_image(img_path)
    load_image_to_model(predictor,image)
    mask,s = find_mask(predictor, prompt, prompt_label)
    return mask