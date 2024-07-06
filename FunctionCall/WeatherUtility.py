import json
import requests

def getCurrentWeather(location):
    """ Get current weather in a given location"""

    url="http://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q": location}
 
    headers = {
    'x-rapidapi-key': "77baae66admsh18605897e990d3fp1854a8jsn43af732e4551",
    'x-rapidapi-host': "weatherapi-com.p.rapidapi.com"
    }
    try:
        response = requests.get(url=url,headers=headers,params=querystring)  
        data = response.json()
        print(data)
        #print(json.dumps(data, indent=4))  # Pretty print the JSON response
    except:
         print(f"Error ={response.raise_for_status()}")  # Raise HTTPError for bad responses

getCurrentWeather("Bangalore")