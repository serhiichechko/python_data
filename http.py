import requests as rq
from pip._vendor.requests.auth import HTTPBasicAuth

response = rq.get('http://195.138.93.170/LewaTest/hs/orders/buy_history?csk=777000075906'
                  , auth=HTTPBasicAuth('ultramobile', '09870'))
response.json()
print(response.json())
