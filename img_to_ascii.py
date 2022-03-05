# img_to_ansii.py
from pathlib import Path
from PIL import Image
from typing import Optional

def convert(
            img_path:Path,
            outfile:Path,
        user_chars:Optional[list] = None,
            new_width:int = 80,
             ) -> None:
    """Convert Image to ANSII Art.

    ARGS:
        img_path(pathlib.Path): path to img file
        outfile(pathlib.Path): path to outfile
            i.e. ~/Documents/outfile.txt
        user_chars(list): list of chars to use
        new_width(int): width of ansii art 
    """
    img = Image.open(img_path).convert('L')
    width, height = img.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    img = img.resize((new_width, new_height))
    pixels = img.getdata()

    if user_chars:
        chars = user_chars
    else:
        chars = ["*", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]

    print(chars) # ADDED FOR TESTING PURPOSES

    new_pixels = [chars[pixel // 25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    new_pixels_count = len(new_pixels)
    ascii_img = [
        new_pixels[index : index + new_width]
        for index in range(0, new_pixels_count, new_width)
    ]

    print([line for line in ansii_img])

    with outfile.open(mode='w') as file:
        file.write(ansii_img)
