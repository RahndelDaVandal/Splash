# img_to_ansii.py
from pathlib import Path
from PIL import Image
from typing import Optional

def convert(
            img_path:Path,
            outfile:Path,
            new_width:int = field(default = 80),
            user_chars:Optional[list],
             ) -> None:
    """Convert Image to ANSII Art.

    ARGS:
        img_path(pathlib.Path): path to img file
        outfile(pathlib.Path): path to outfile
            i.e. ~/Documents/outfile.txt
        new_width(int): width of ansii art 
        user_chars(list): list of chars to use
    """
    img = Image.open(img_path).convert('L')
    width, height = img.size
    aspect_ration = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    img = img.resize(new_width, new_height)
    pixels = img.getdata()

    if user_chars:
        chars = user_chars
    else:
        chars = ["*", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]

    new_pixels = [chars[pixel // 25] for pixel in pixels]
    new_pixels = ''.join(new_pixels)

    ansii_img = [
                 new_pixels[index : index + width]
                 for index in range(0, len(new_pixels), new_width)
                 ]

    ansii_img = ''.join(ansii_img)

    with outfile.open(mode='w') as file:
        file.write(ansii_img)
