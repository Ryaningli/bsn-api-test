import json
import unittest
from common.Log import MyLog as Log
from common.configHttp import ConfigHttp

configHttp = ConfigHttp()


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.log = Log.get_log()

    def testLogin(self):
        configHttp.set_url('/shangchain/bsnApi/login/userLogin')

        data = json.loads('{"phone":"18815596963","password":"abc123"}')
        configHttp.set_data(data)

        res = configHttp.post_json()

        print(res.text)

    def tearDown(self):
        pass