import numpy as np
import cv2
from PIL import Image

def read_image(img_path):
    image = cv2.imread(img_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

def get_colored_mask(mask, random_color=False):
    if random_color:
        color = np.concatenate([np.random.random(3), np.array([0.6])], axis=0)
    else:
        color = np.array([30, 144, 255, 0.6])
    h, w = mask.shape[-2:]
    mask_image = mask.reshape(h, w, 1) * color.reshape(1, 1, -1)
    # mask_image_flatten = mask_image.flatten()
    return mask_image

def transform_white_to_transparent(image):
    image = image.convert('RGBA')
    np_image = np.array(image)

    white_pixels = (np_image[:, :, 0] == 255) & (np_image[:, :, 1] == 255) & (np_image[:, :, 2] == 255)
    np_image[:, :, 3][white_pixels] = 0

    non_white_pixels = ~((np_image[:, :, 0] == 255) & (np_image[:, :, 1] == 255) & (np_image[:, :, 2] == 255))
    np_image[:, :, :3][non_white_pixels] = [135, 255, 255]
    np_image[:, :, 3][non_white_pixels] = 150

    output_image = Image.fromarray(np_image)
    return output_image