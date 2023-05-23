import os
from google.cloud import vision
from google_vision_ai import VisionAI
from google_vision_ai import prepare_image_local, prepare_image_web, draw_boundary, draw_boundary_normalized

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_file_vision_ai_demo.json'

#Instantiates a client
client = vision.ImageAnnotatorClient()

image_file_path = './images/20230523_204700018.jpg'
image = prepare_image_local(image_file_path)
va = VisionAI(client, image)

import sys

texts = va.text_detection()
for indx, text in enumerate(texts):
    print(text.description)
    if indx > 3:
        sys.exit()