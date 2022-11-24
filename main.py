from PIL import Image, ImageEnhance, ImageFilter
import os

path='./imags'
pathOut='/editedImages'

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit=img.filter(ImageFilter.SHARPEN)
    cleanName=os.path.splitext(filename)[0]
    edit.save(f'.{pathOut}/{cleanName}_edited_img.jpg')