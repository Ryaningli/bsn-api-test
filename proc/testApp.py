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
        headers = {'X-Token': token}
        self.ch.set_headers(headers)

        self.app_name = None
        self.user_id = None
        self.account = None
        self.usable_node = None
        self.order_id = None
        self.app_info_id = None
        self.pay_price = None
        self.frame_type = None
        self.cover_path = None
        self.doc_path = None
        self.default_chain_code_data = None
        self.default_chain_code_func = None
        self.new_chain_code_path = None

    # 获取用户信息（用户id与账户余额）
    def get_user_info(self):
        self.ch.set_url(common.user_info)
        response = self.ch.post()
        json_data = response.json()
        try:
            assert json_data['code'] == 0
            self.user_id = json_data['data']['bsnUser']['userId']
            self.account = json_data['data']['bsnUser']['userAccount']
            log.info('获取用户信息成功')
        except AssertionError:
            log.error('获取用户信息失败:{}'.format(json_data))
            raise AssertionError('返回code不等于0！')

    # 获取可用的节点列表
    def get_usable_node(self):
        data = {"pageNum": 1, "pageSize": 50, "appType": 1, "tps": 10, "capacity": 10}
        self.ch.set_url(common.usable_node)
        self.ch.set_data(data)
        response = self.ch.post_json()
        json_data = response.json()
        try:
            assert json_data['code'] == 0
            self.usable_node = json_data['rows']
            log.info('获取可用的节点列表成功')
        except AssertionError:
            log.info('获取可用的节点列表失败:{}'.format(json_data))
            raise AssertionError('返回code不等于0！')

    # 购买服务订单
    def by_app(self):
        ran = random.sample(list(range(len(self.usable_node))), 3)
        self.app_name = self.rc.get_http('app_name')

        data = {
            "appType": 1,
            "payType": 1,
            "appName": self.app_name,
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
        json_data = response.json()
        try:
            assert json_data['code'] == 0

            # 更新服务名称
            new_app_name = self.app_name.split('_')[0] + '_' + str(int(self.app_name.split('_')[1]) + 1)
            self.rc.set_http('app_name', new_app_name)

            self.order_id = json_data['data']['orderId']
            self.app_info_id = json_data['data']['appInfoId']
            self.pay_price = json_data['data']['payPrice']
            log.info('购买服务订单生成成功，服务名：{}'.format(self.app_name))

        except AssertionError:
            log.error('购买服务订单生成失败:{}'.format(json_data))
            raise AssertionError('返回code不等于0！')

    # 购买服务订单支付
    def pay_app_order(self):
        data = {
            "orderId": self.order_id
        }
        self.ch.set_url(common.pay)
        self.ch.set_data(data)
        response = self.ch.post_json()
        json_data = response.json()
        try:
            assert json_data['code'] == 0
            log.info('支付成功')
        except AssertionError:
            log.error('支付失败:{}'.format(json_data))
            raise AssertionError('返回code不等于0！')

    # 获取服务类型
    def app_get(self):
        data = {
            "appInfoId": self.app_info_id
        }
        self.ch.set_url(common.app_get)
        self.ch.set_data(data)
        response = self.ch.post_json()
        json_data = response.json()
        try:
            assert json_data['code'] == 0
            self.frame_type = json_data['data']['frameType']
            log.info('获取服务类型成功')
        except AssertionError:
            log.error('获取服务类型失败:{}'.format(json_data))
            raise AssertionError('返回code不等于0！')

    # 上传封面
    def upload_cover(self):
        img = 'cover.png'
        self.ch.set_files(img)
        self.ch.set_url(common.upload_img)
        response = self.ch.post_file()
        json_data = response.json()
        try:
            assert json_data['code'] == 0
            self.cover_path = json_data['url']
            log.info('上传服务封面成功')
        except AssertionError:
            log.error('上传服务封面失败:{}'.format(json_data))
            raise AssertionError('返回code不等于0！')

    # 上传服务文档资料
    def upload_doc(self):
        file = '测试-服务文档资料.txt'
        self.ch.set_files(file)
        self.ch.set_url(common.upload_file)
        response = self.ch.post_file()
        json_data = response.json()
        try:
            assert json_data['code'] == 0
            self.doc_path = json_data['url']
            log.info('上传服务文档成功')
        except AssertionError:
            log.error('上传服务文档失败:{}'.format(json_data))
            raise AssertionError('返回code不等于0！')

    # 获取默认链码包信息
    def get_default_chain_code(self):
        data = {
            "stringType": self.frame_type,
            "pageIndex": 1,
            "pageSize": 10
        }
        self.ch.set_data(data)
        self.ch.set_url(common.default_chain_code)
        response = self.ch.post_json()
        json_data = response.json()
        try:
            assert json_data['code'] == 0
            self.default_chain_code_data = json_data['rows'][0]
            log.info('获取默认链码包信息成功')
        except AssertionError:
            log.error('获取默认链码包信息失败:{}'.format(json_data))
            raise AssertionError('返回code不等于0！')

    # 获取默认链码包方法
    def get_default_chain_code_func(self):
        data = {"id": self.default_chain_code_data['id']}
        self.ch.set_data(data)
        self.ch.set_url(common.default_chain_code_func)
        response = self.ch.post_json()
        json_data = response.json()
        try:
            assert json_data['code'] == 0
            self.default_chain_code_func = json_data['rows']
            log.info('获取默认链码包信息成功')
        except AssertionError:
            log.error('获取默认链码包信息失败:{}'.format(json_data))
            raise AssertionError('返回code不等于0！')

    # 上传新增链码包
    def upload_new_chain_code(self):
        file = 'ChainCode.zip'
        self.ch.set_files(file)
        self.ch.set_url(common.upload_file)
        response = self.ch.post_file()
        json_data = response.json()
        try:
            assert json_data['code'] == 0
            self.new_chain_code_path = json_data['url']
            log.info('上传新增链码包成功')
        except AssertionError:
            log.error('上传新增链码包失败:{}'.format(json_data))
            raise AssertionError('返回code不等于0！')

    # 上传服务
    def upload_app(self):
        # 造方法数据
        funcs = []
        for func in self.default_chain_code_func:
            f = {
                "id": "",
                "funcName": func['funcName'],
                "funcType": str(func['funcType']),
                "ccName": func['ccName'],
                "ccMethod": func['ccMethod']
            }

            funcs.append(f)

        funcs.append({
            "id": "",
            "funcName": "新的功能-预置",
            "funcType": "2",
            "ccName": self.default_chain_code_func[0]['ccName'],
            "ccMethod": "new_method1"
        })
        funcs.append({
            "id": "",
            "funcName": "新的功能-新增",
            "funcType": "3",
            "ccName": "新增链码包-Python",
            "ccMethod": "new_method2"
        })

        # 造用户数据
        user1_func = random.sample(funcs, random.randint(1, len(funcs)))
        s1 = ''
        for f in user1_func:
            s1 = s1 + f['funcName'] + ','

        user2_func = random.sample(funcs, random.randint(1, len(funcs)))
        s2 = ''
        for f in user2_func:
            s2 = s2 + f['funcName'] + ','

        data = {
            "appName": self.app_name,
            "userId": self.user_id,
            "appInfoId": self.app_info_id,
            "vers": "1.1.1",
            "img": self.cover_path,
            "introduction": "这是服务的简介-Python",
            "appDesc": "<p>这是服务的描述-Python</p>",
            "caType": "1",
            "docList": [
                {
                    "docName": "这是服务的文档资料-Python",
                    "docType": str(random.randint(1, 3)),
                    "docPath": self.doc_path,
                    "id": None
                }
            ],
            "chainCodeList": [
                {
                    "ccLanguage": self.default_chain_code_data['ccType'],
                    "ccName": self.default_chain_code_data['ccName'],
                    "ccPackageName": self.default_chain_code_data['ccPackageName'],
                    "ccPath": self.default_chain_code_data['ccPath'],
                    "ccVerNo": self.default_chain_code_data['ccVersion'],
                    "initParam": "",
                    "mainPath": self.default_chain_code_data['mainPath']
                },
                {
                    "ccName": "新增链码包-Python",
                    "ccVerNo": "1.1.1.1",
                    "ccLanguage": "1",
                    "ccPath": self.new_chain_code_path,
                    "ccPackageName": "ChainCode.zip",
                    "mainPath": "",
                    "initParam": "init"
                }
            ],
            "funcList": funcs,
            "roleList": [
                {
                    "roleName": "用户1",
                    "roleDesc": "这是用户1-Python",
                    "funcList": user1_func,
                    "rolePermissionDesc": s1[:-1]
                },
                {
                    "roleName": "用户2",
                    "roleDesc": "这是用户2-Python",
                    "funcList": user2_func,
                    "rolePermissionDesc": s2[:-1]
                }
            ],
            "appServiceType": "1"
                }

        self.ch.set_data(data)
        self.ch.set_url(common.upload_app)
        response = self.ch.post_json()
        json_data = response.json()
        try:
            assert json_data['code'] == 0
            log.info('上传服务成功')
        except AssertionError:
            log.error('上传服务失败:{}'.format(json_data))
            raise AssertionError('返回code不等于0！')


if __name__ == '__main__':
    p = TestApp()
    p.get_user_info()
    p.get_usable_node()
    p.by_app()
    p.pay_app_order()
    p.app_get()
    p.upload_cover()
    p.upload_doc()
    p.get_default_chain_code()
    p.get_default_chain_code_func()
    p.upload_new_chain_code()
    p.upload_app()
