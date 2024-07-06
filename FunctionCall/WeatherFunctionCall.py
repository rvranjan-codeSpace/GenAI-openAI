import openai
from dotenv import load_dotenv
import os
import http.client
import pprint

load_dotenv()
#print(openai.__version__)
openai.api_key = os.getenv('OPENAI_API_KEY')


conn = http.client.HTTPSConnection("ai-weather-by-meteosource.p.rapidapi.com")
headers = {
    'x-rapidapi-key': "77baae66admsh18605897e990d3fp1854a8jsn43af732e4551",
    'x-rapidapi-host': "ai-weather-by-meteosource.p.rapidapi.com"
}

conn.request("GET", "/time_machine?lat=37.81021&lon=-122.42282&date=2021-08-24&units=auto", headers=headers)
res = conn.getresponse()
data = res.read()

responses = openai.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "My age is 30 and I am learning to learn AIML"},
        {"role": "user", "content": "What is my age?"},
        {"role": "user", "content": "What am I suppose to learn?"},
    ],   
)

#print(responses.choices[0].message)

for ch in responses.choices:
    print(f"Role=${ch.message.role}\n")
    print(f"Messages={ch.message.content}\n")

