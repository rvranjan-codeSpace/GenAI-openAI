#from openai import OpenAI
import openai
from dotenv import load_dotenv # import env variable from .env file
import os
import pandas as pd

# Load environment variables from .env file
load_dotenv()
print(openai.__version__)

openai.api_key = os.getenv('OPENAI_API_KEY')
#models = openai.models.list().data

# chat completion AI requires a role and then content as a prompt 
response = openai.chat.completions.create(
    model = 'gpt-3.5-turbo',
     messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Who are you?"},
        {"role": "user", "content": "My age is 30 and I am learning to learn AIML"}
    ],
    temperature= 0.9,
    n=1
    
)
print(len(response.choices))
for ch in response.choices:
    print (f"role={ch.message.role}")
    print (f"role={ch.message.content}")








