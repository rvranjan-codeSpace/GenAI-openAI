#from openai import OpenAI
import openai
from dotenv import load_dotenv # import env variable from .env file
import os
import pandas as pd

# Load environment variables from .env file
load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
models = openai.models.list().data


#print(type(models))
#print(pd.DataFrame(models))

#Chat completion API


response = openai.completions.create(
    model = 'davinci-002',
    prompt= "what is a computer",
    max_tokens=40,
    temperature=0.5,
    n=1 # number of ouputs
)
for i in response.choices:
    print(i.text)
    print(i.finish_reason)






