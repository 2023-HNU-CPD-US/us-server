import os
import openai
openai.api_key = "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"

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