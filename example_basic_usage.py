import io
import os
import pandas as pd
from google.cloud import vision
from google_vision_ai import VisionAI
from google_vision_ai import prepare_image_local, prepare_image_web, draw_boundary, draw_boundary_normalized


#Instantiates a client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_file_vision_ai_demo.json'
client = vision.ImageAnnotatorClient()

#prepare the image(local source)
# image_path = './images/13020555.jpg'
# with io.open(image_path, 'rb') as image_file:
#     content = image_file.read()
# image = vision.Image(content=content)
#
# #prepare the image(web source)
# image_url = 'https://www.google.com/imgres?imgurl=https%3A%2F%2Fmelonicedlatte.com%2Fsystem%2Fuploads%2Fimages%2F000%2F001%2F137%2Foriginal%2Fimage.png%3F1530191049&tbnid=ltGtBq7-2EFMaM&vet=12ahUKEwjnrc_dm4v_AhUdm1YBHf05D1IQMygAegUIARC3AQ..i&imgrefurl=https%3A%2F%2Fmelonicedlatte.com%2Fpython%2F2017%2F06%2F30%2F145309.html&docid=w7vGTGlhTiEjtM&w=337&h=257&q=python%20%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0%20%EB%AC%B8&ved=2ahUKEwjnrc_dm4v_AhUdm1YBHf05D1IQMygAegUIARC3AQ'
# image = vision.Image()
# image.source.image_uri = image_url
#
# response = client.label_detection(image=image)
# for label in response.label_annotations:
#     print(label.description)
#     print(label.score)

image_path = './images/13020555.jpg'
image = prepare_image_local(image_path)
va = VisionAI(client, image)
label_detections = va.label_detection()

df = pd.DataFrame(label_detections)
print(df)