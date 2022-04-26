import requests
import json

from requests.auth import AuthBase


class Auth(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['X-Token'] = self.token
        return r



body = {
    'phone': '18815596963',
    'password': 'abc123'
}
url = 'http://120.78.132.70/shangchain/bsnApi/login/userLogin'
url2 = 'http://120.78.132.70/shangchain/bsnApi/getBsnUser'
url3 = 'http://120.78.132.70/shangchain/bsnApi/invoice/billableMoney'


# s = requests.session()
# # s.auth = ('X-Token', '574a415b5057514d51555041505f5f56495e5045465b')
# # s.headers.update({'X-Token': '574a415b5057514d51555041505f5f56495e5045465b'})
# # r = s.post(url, json=body)
# r2 = s.post(url2)
# r3 = s.get(url3)
#
# # print(r.status_code)
# # print(r.json())
#
# print(r2.status_code)
# print(r2.json())
#
# print(r3.json())

r = requests.post(url2, auth=Auth('574a415b5057514d51555041505f5f56495e5045465b'))

print(r.json())


