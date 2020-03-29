import json
import requests
API_URL= requests.get('https://api.hgbrasil.com/finance/quotations?key=2418a82c')
info=json.loads(API_URL.content.decode('utf-8'))

print(info)