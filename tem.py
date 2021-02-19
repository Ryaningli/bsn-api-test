import requests
import json


url = 'http://120.78.132.70/shangchain/bsnApi/getBsnUser'

headers = {
    'Content-Type': 'application/json',
    'X-Token': '574a415b515d534f50535041505f5f56495e5045465b'
}

body = {
    'phone': '18815596963',
    'password': 'abc123'
}

response = requests.post(url, headers=headers, data=json.dumps(body))
# response = requests.post(url, headers=headers)

print(response.text)
