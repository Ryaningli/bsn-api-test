import json
import requests
import readConfig
from common.Log import MyLog

localReadConfig = readConfig.ReadConfig()
logger = MyLog.get_log()
log = logger.get_logger()

class ConfigHttp:

    def __init__(self):
        global scheme, host, port, timeout
        scheme = localReadConfig.get_http('scheme')
        host = localReadConfig.get_http('host')
        port = localReadConfig.get_http('port')
        timeout = localReadConfig.get_http('timeout')
        
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}
        self.state = 0

    def set_url(self, url):
        """
        set url
        :param: interface url
        :return:
        """
        self.url = scheme+'://'+host+url

    def set_headers(self, header):
        """
        set headers
        :param header:
        :return:
        """
        self.headers = header

    def set_params(self, param):
        """
        set params
        :param param:
        :return:
        """
        self.params = param

    def set_data(self, data):
        """
        set data
        :param data:
        :return:
        """
        self.data = data

    def set_files(self, filename):
        """
        set upload files
        :param filename:
        :return:
        """
        if filename != '':
            file_path = 'C:/Users/shangchain/Desktop/Ryan/BSN-API-Test/testFile/' + filename
            self.files = {'file': open(file_path, 'rb')}

        if filename == '' or filename is None:
            self.state = 1

    def get(self):
        """
        defined get method
        :return:
        """
        try:
            response = requests.get(self.url, headers=self.headers, params=self.params, data=self.data, timeout=float(timeout))
            return response
        except requests.exceptions.ReadTimeout:
            log.error('超时！！！')
            return None

    def post(self):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, params=self.params, data=self.data, timeout=float(timeout))
            # response.raise_for_status()
            return response
        except requests.exceptions.ReadTimeout:
            log.error('超时！！！')
            return None

    def post_file(self):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, data=self.data, files=self.files, timeout=float(timeout))
            return response
        except requests.exceptions.ReadTimeout:
            log.error('超时！！！')
            return None

    def post_json(self):
        """
        defined post method
        :return:
        """
        try:
            response = requests.post(self.url, headers=self.headers, json=self.data, timeout=float(timeout))
            return response
        except requests.exceptions.ReadTimeout:
            log.error('超时!!!')
            return None


if __name__ == '__main__':
    testHttp = ConfigHttp()
    testHttp.set_url('/shangchain/bsnApi/login/userLogin')
    s = '{"phone":"18815596963","password":"abc123"}'
    j = json.loads(s)
    testHttp.set_data(j)

    res = testHttp.post_json()
    print(res.text + '\n' + str(res.status_code))