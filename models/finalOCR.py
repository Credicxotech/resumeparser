import pdf2image
import easyocr as e
import numpy as np
import PIL
from PIL import ImageDraw
import spacy 

bounds= []
def do_ocr(user_input):
    reader = e.Reader(['en'])
    images = (pdf2image.convert_from_path(user_input, 
    poppler_path=r'C:\Program Files\poppler-0.68.0\bin'))
    
    for i in range(0,len(images)):
        bounds.append(reader.readtext(np.array(images[i]), min_size=0,
        slope_ths=0.2,ycenter_ths=0.7,height_ths=0.6,width_ths=0.8,
        decoder='beamsearch', beamWidth=10))
    text=''
    for j in range(len(bounds)):
        for i in range(len(bounds[j])):
            text = text + bounds[j][i][1] + ' '

    return text         

ocr = do_ocr(user_input)

def sending_text():
    return ocr 
    
   