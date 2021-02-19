import random
import common
import readConfig
from common.configHttp import ConfigHttp
from common.getToken import get_token
from common.Log import MyLog

logger = MyLog.get_log()
log = logger.get_logger()


class TestApp:
    def __init__(self):
        self.ch = ConfigHttp()
        self.rc = readConfig.ReadConfig()
        token = get_token()
        headers = {
            'X-Token': token
        }
        self.ch.set_headers(headers)

        self.user_id = None
        self.account = None
        self.usable_node = None
        self.order_id = None
        self.app_info_id = None
        self.pay_price = None
        self.frame_type = None
        self.cover_path = None
        self.doc_path = None
        self.default_chain_code_id = None

    @staticmethod
    def assert_code(response, msg=None):
        json_data = response.json()
        try:
            assert json_data['code'] == 0
            log.info('成功：{}'.format(msg))
            return json_data
        except AssertionError:
            log.error('失败:{}:{}'.format(msg, json_data))
            raise AssertionError('返回code不等于0！')

    # 获取用户信息（用户id与账户余额）
    def get_user_info(self):
        self.ch.set_url(common.user_info)
        response = self.ch.post()
        json_data = self.assert_code(response, '获取用户信息')
        self.user_id = json_data['data']['bsnUser']['userId']
        self.account = json_data['data']['bsnUser']['userAccount']

    # 获取可用的节点列表
    def get_usable_node(self):
        data = {"pageNum": 1, "pageSize": 50, "appType": 1, "tps": 10, "capacity": 10}
        self.ch.set_url(common.usable_node)
        self.ch.set_data(data)
        response = self.ch.post_json()
        json_data = self.assert_code(response, '获取可用节点列表')
        self.usable_node = json_data['rows']

    # 购买服务订单
    def by_app(self):
        ran = random.sample(list(range(len(self.usable_node))), 3)
        app_name = self.rc.get_http('app_name')
        data = {
            "appType": 1,
            "payType": 1,
            "appName": app_name,
            "algorithmType": 2,
            "frameType": "fabric",
            "orgList": [
                {
                    "orgCode": self.usable_node[ran[0]]['orgCode'],
                    "orgName": self.usable_node[ran[0]]['orgName'],
                    "spCode": self.usable_node[ran[0]]['spCode'],
                    "spName": self.usable_node[ran[0]]['spName'],
                    "operatorCode": self.usable_node[ran[0]]['operatorCode'],
                    "address": self.usable_node[ran[0]]['address'],
                    "nodeCount": "1",
                    "tps": 10,
                    "capacity": 10,
                    "chainNodeList": self.usable_node[ran[0]]['chainNodeList']
                },
                {
                    "orgCode": self.usable_node[ran[1]]['orgCode'],
                    "orgName": self.usable_node[ran[1]]['orgName'],
                    "spCode": self.usable_node[ran[1]]['spCode'],
                    "spName": self.usable_node[ran[1]]['spName'],
                    "operatorCode": self.usable_node[ran[1]]['operatorCode'],
                    "address": self.usable_node[ran[1]]['address'],
                    "nodeCount": "1",
                    "tps": 10,
                    "capacity": 10,
                    "chainNodeList": self.usable_node[ran[1]]['chainNodeList']
                },
                {
                    "orgCode": self.usable_node[ran[2]]['orgCode'],
                    "orgName": self.usable_node[ran[2]]['orgName'],
                    "spCode": self.usable_node[ran[2]]['spCode'],
                    "spName": self.usable_node[ran[2]]['spName'],
                    "operatorCode": self.usable_node[ran[2]]['operatorCode'],
                    "address": self.usable_node[ran[2]]['address'],
                    "nodeCount": "1",
                    "tps": 10,
                    "capacity": 10,
                    "chainNodeList": self.usable_node[ran[2]]['chainNodeList']
                }
            ]
        }

        self.ch.set_url(common.by_app)
        self.ch.set_data(data)
        response = self.ch.post_json()
        json_data = self.assert_code(response, '购买服务订单')

        # 更新服务名称
        new_app_name = app_name.split('_')[0] + '_' + str(int(app_name.split('_')[1]) + 1)
        self.rc.set_http('app_name', new_app_name)

        self.order_id = json_data['data']['orderId']
        self.app_info_id = json_data['data']['appInfoId']
        self.pay_price = json_data['data']['payPrice']

    # 购买服务订单支付
    def pay_app_order(self):
        data = {
            "orderId": self.order_id
        }
        self.ch.set_url(common.pay)
        self.ch.set_data(data)
        response = self.ch.post_json()
        self.assert_code(response, '购买服务订单支付')

    # 获取服务类型
    def app_get(self):
        data = {
            "appInfoId": self.app_info_id
        }
        self.ch.set_url(common.app_get)
        self.ch.set_data(data)
        response = self.ch.post_json()
        json_data = self.assert_code(response, '获取服务类型')
        self.frame_type = json_data['data']['frameType']

    # 上传服务封面
    def upload_cover(self):
        img = 'cover.png'
        self.ch.set_files(img)
        self.ch.set_url(common.upload_img)
        response = self.ch.post_file()
        json_data = self.assert_code(response, '上传服务封面')
        self.cover_path = json_data['url']

    # 上传服务文档资料
    def upload_doc(self):
        file = '测试-服务文档资料.txt'
        self.ch.set_files(file)
        self.ch.set_url(common.upload_file)
        response = self.ch.post_file()
        json_data = self.assert_code(response, '上传服务文档')
        self.doc_path = json_data['url']

    def get_default_chain_code(self):
        data = {
            "stringType": self.frame_type,
            "pageIndex": 1,
            "pageSize": 10
        }
        self.ch.set_data(data)
        self.ch.set_url(common.default_chain_code)
        response = self.ch.post_json()
        json_data = self.assert_code(response, '获取默认链码包信息')
        self.default_chain_code_id = json_data['rows'][0]['id']

    # 获取默认链码包方法
    def get_default_chain_code_func(self):
        data = {"id": self.default_chain_code_id}
        self.ch.set_data(data)
        self.ch.set_url(common.default_chain_code_func)


if __name__ == '__main__':
    p = TestApp()
    p.get_usable_node()
    p.by_app()
    p.pay_app_order()
    p.app_get()
    p.upload_cover()
    p.upload_doc()
    p.get_default_chain_code()
