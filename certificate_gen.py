from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from constants import arabic_font, english_font
from arabic_reshaper import ArabicReshaper


import re
def is_english(text):

    english_pattern = re.compile(r'[a-zA-Z]')
    return bool(english_pattern.search(text))

configuration = {"use_unshaped_instead_of_isolated": True}

def generate_certificate(name, workshop, folder_path, female=False):
    workshop = str(workshop)
    if female:
        if workshop ==1:
            template_file = female.jpg
            name_position = (452, 535)
        else:
            template_file = f"female{workshop}.jpg"
            name_position = (1240, 1490)
    else:
        if workshop ==1:
            template_file = f"male.jpg"
            name_position = (452, 525)
        else:
            template_file = f"male{workshop}.jpg"
            name_position = (1240, 1460)

    if workshop ==1:
        size = 37
    else:
        size = 93

    # Load the certificate template
    template_path = folder_path + template_file
    template = Image.open(template_path)

    # Initialize the drawing context
    draw = ImageDraw.Draw(template)
    reshaper = ArabicReshaper(configuration=configuration)
    if is_english(name):
        reshaped_name = name
        font = ImageFont.truetype(f'{folder_path}{english_font}', size=size)
    else:
        reshaped_name = reshaper.reshape(name)
        reshaped_name = reshaped_name[::-1]
        font = ImageFont.truetype(f'{folder_path}{arabic_font}', size=size)

    draw.text(name_position, reshaped_name, font=font, fill="black", anchor="ms")

    output_path = f'{folder_path}{name}.jpg'
    template.save(output_path)

