#         Python Stream Doeck Library
#      Released under the GPLv2 licence
#
#  Authors:
#    * Lisias T (https://github.com/lisias)

import os
from PIL import Image, ImageOps

ASSETS_PATH = os.path.join(os.path.dirname(__file__), "../..", "Assets")

def load_asset(fname:str) -> list:
    fullpathname = os.path.join(ASSETS_PATH, fname)
    with open(fullpathname, mode='rb') as f:
        payload = f.read()
    return payload

def load_asset_image(fname:str, image_format=None) -> Image:
    fullpathname = os.path.join(ASSETS_PATH, fname)
    image = Image.open(os.path.join(ASSETS_PATH, fullpathname))
    if image_format:
        image = adjust_image(image, image_format)
    return image

def create_image(image_format, background) -> Image:
    return Image.new("RGB", image_format['size'], background)

def adjust_image(image, image_format) -> Image:
    if image.size != image_format['size']:
        image = scale_image(image, image_format)

    if image_format['rotation']:
        image = image.rotate(image_format['rotation'], expand=1)

    if image_format['flip'][0]:
        image = image.transpose(Image.FLIP_LEFT_RIGHT)

    if image_format['flip'][1]:
        image = image.transpose(Image.FLIP_TOP_BOTTOM)

    return image.convert("RGB")

def scale_image(image, image_format, margins=[0, 0, 0, 0], background='black') -> Image:
    if len(margins) != 4:
        raise ValueError("Margins should be given as an array of four integers.")

    final_image = create_image(image_format, background=background)

    thumbnail_max_width = final_image.width - (margins[1] + margins[3])
    thumbnail_max_height = final_image.height - (margins[0] + margins[2])

    thumbnail = image.convert("RGBA")
    thumbnail.thumbnail((thumbnail_max_width, thumbnail_max_height), Image.LANCZOS)

    thumbnail_x = (margins[3] + (thumbnail_max_width - thumbnail.width) // 2)
    thumbnail_y = (margins[0] + (thumbnail_max_height - thumbnail.height) // 2)

    final_image.paste(thumbnail, (thumbnail_x, thumbnail_y), thumbnail)

    return final_image.convert("RGB")
