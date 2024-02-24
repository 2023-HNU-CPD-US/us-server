import openai
import os
import textwrap
from google.cloud import vision
from google_vision_ai import VisionAI
from google_vision_ai import prepare_image_local, prepare_image_web, draw_boundary, draw_boundary_normalized

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'client_file_vision_ai_demo.json'

#Instantiates a client
client = vision.ImageAnnotatorClient()

image_file_path = './images/20230523.jpg'
image = prepare_image_local(image_file_path)
va = VisionAI(client, image)

import sys
message = ""
texts = va.text_detection()
print("원본내용\n")
for indx, text in enumerate(texts):
    print(text.description)
    message += text.description
    if indx > 3:
        break

print('\n')


openai.api_key = "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"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "이 책에 내용을 교수가 대학생들에게 간단하게 설명해주려고해",
        },
        {
            "role": "user",
            "content": f"{message}\n" + "한국어로 요약해줘.",
        },
    ],
)
print("GPT 요약\n")
long_text = completion.choices[0].message["content"]
result = textwrap.fill(long_text, width=50)
print(result)