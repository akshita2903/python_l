import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_Key=os.getenv('API_Key')
city=input("Enter the city name \n")
city=city.capitalize()
url=f'http://api.weatherapi.com/v1/current.json?key={API_Key}&q={city}'
r=requests.get(url)
# print(r.text)
dict=json.loads(r.text)
print('Country'+" : "+dict['location']['country'],"\nTemperature : "+(str)(dict['current']['temp_c']))