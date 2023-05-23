import os
from google.cloud import vision
from google_vision_ai import VisionAI
from google_vision_ai import prepare_image_local, prepare_image_web, draw_boundary

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_file_vision_ai_demo.json'

#Instantiates a client
client = vision.ImageAnnotatorClient()

image_file_path = './images/321321.jpg'
image = prepare_image_local(image_file_path)

va = VisionAI(client, image)
landmarks = va.landmark_detection()
for landmark in landmarks:
    print(landmark.description)
    print(landmark.score)
    draw_boundary(image_file_path, landmark.bounding_poly, landmark.description)