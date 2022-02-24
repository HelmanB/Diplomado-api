from urllib import response
from pandas import json_normalize
import requests 
import json 
response = requests.get('http://127.0.0.1:8000/datos')
info = json.loads(response.text)
datos = json_normalize(info)
print(datos)