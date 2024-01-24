import os
import openai

openai.api_key = '****'

system_message = 'Given an English reasoning-heavy question, you will provide a well-reasoned, step-by-step response in Spanish.'

response = openai.ChatCompletion.create(
    model = 'ft:gpt-3.5-turbo-0613:melitacruces:test02:8iNp1SuI',
    messages = [
      {
        "role": "system",
        "content": system_message,
      },
      {
        "role": "user",
        "content": "I want to learn how to make a website.",
      }
    ],
)

response.choices[0].message['content']