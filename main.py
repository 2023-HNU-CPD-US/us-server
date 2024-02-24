import os
import openai
openai.api_key = "대충 키 값이였던 것"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Hi? Can you hear me?"
        }
    ]
)
print(completion)
