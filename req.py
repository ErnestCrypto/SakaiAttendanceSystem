import requests
import json
import requests

url = "https://ipgeolocation.abstractapi.com/v1"

querystring = {"api_key":"f5717dc070fb45d1ae361a31e761badf","ip_address":"76.76.21.61"}

response = requests.request("GET", url, params=querystring)

print(response.text)
#TjiHMM1yQS17hnKVupK98Ir5