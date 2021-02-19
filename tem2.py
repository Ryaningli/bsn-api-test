import random

d1 = {"total": 5, "rows": [
    {"nodeId": None, "orgCode": "ORG2020040820393202956", "orgName": "商用测试-5", "spCode": "25", "spName": "测试企业名称",
     "operatorCode": "000002", "operatorName": None, "address": "中华人民共和国江苏省", "nodeNum": 3,
     "nodeList": [{"appType": 1, "nodeName": "test0.test.com", "tps": 71400, "capacity": 629350},
                  {"appType": 1, "nodeName": "test1.test.com", "tps": 71400, "capacity": 629190},
                  {"appType": 1, "nodeName": "test2.test.com", "tps": 71400, "capacity": 629510}], "jdnum": "1",
     "capacity": 0, "tps": 0, "gatewayUrl": None,
     "chainNodeList": [{"appType": 1, "nodeName": "test0.test.com", "tps": 71400, "capacity": 629350},
                       {"appType": 1, "nodeName": "test1.test.com", "tps": 71400, "capacity": 629190},
                       {"appType": 1, "nodeName": "test2.test.com", "tps": 71400, "capacity": 629510}],
     "certList": None, "monthPrice": {"tpsPrice": "22.91", "capacityPrice": "104.58", "flowPrice": "114.58"},
     "yearPrice": {"tpsPrice": "250.00", "capacityPrice": "1250.00", "flowPrice": "1250.00"}},
    {"nodeId": None, "orgCode": "ORG2020040819450655818", "orgName": "商用测试-4", "spCode": "25", "spName": "测试企业名称",
     "operatorCode": "000003", "operatorName": None, "address": "中华人民共和国江苏省", "nodeNum": 3,
     "nodeList": [{"appType": 1, "nodeName": "test0.test.com", "tps": 71410, "capacity": 629250},
                  {"appType": 1, "nodeName": "test1.test.com", "tps": 71400, "capacity": 629300},
                  {"appType": 1, "nodeName": "test2.test.com", "tps": 71350, "capacity": 629380}], "jdnum": "1",
     "capacity": 0, "tps": 0, "gatewayUrl": None,
     "chainNodeList": [{"appType": 1, "nodeName": "test0.test.com", "tps": 71410, "capacity": 629250},
                       {"appType": 1, "nodeName": "test1.test.com", "tps": 71400, "capacity": 629300},
                       {"appType": 1, "nodeName": "test2.test.com", "tps": 71350, "capacity": 629380}],
     "certList": None, "monthPrice": {"tpsPrice": "22.91", "capacityPrice": "114.58", "flowPrice": "114.58"},
     "yearPrice": {"tpsPrice": "250.00", "capacityPrice": "1250.00", "flowPrice": "1250.00"}},
    {"nodeId": None, "orgCode": "ORG2020033020450185718", "orgName": "商用测试-3", "spCode": "25", "spName": "测试企业名称",
     "operatorCode": "000003", "operatorName": None, "address": "中华人民共和国江苏省", "nodeNum": 3,
     "nodeList": [{"appType": 1, "nodeName": "test0.test.com", "tps": 71310, "capacity": 629550},
                  {"appType": 1, "nodeName": "test1.test.com", "tps": 71340, "capacity": 629410},
                  {"appType": 1, "nodeName": "test2.test.com", "tps": 71320, "capacity": 629620}], "jdnum": "1",
     "capacity": 0, "tps": 0, "gatewayUrl": None,
     "chainNodeList": [{"appType": 1, "nodeName": "test0.test.com", "tps": 71310, "capacity": 629550},
                       {"appType": 1, "nodeName": "test1.test.com", "tps": 71340, "capacity": 629410},
                       {"appType": 1, "nodeName": "test2.test.com", "tps": 71320, "capacity": 629620}],
     "certList": None, "monthPrice": {"tpsPrice": "22.92", "capacityPrice": "114.59", "flowPrice": "114.59"},
     "yearPrice": {"tpsPrice": "250.00", "capacityPrice": "1250.00", "flowPrice": "1250.00"}},
    {"nodeId": None, "orgCode": "ORG2020032819015310631", "orgName": "商用测试-1", "spCode": "25", "spName": "测试企业名称",
     "operatorCode": "000004", "operatorName": None, "address": "中华人民共和国江苏省", "nodeNum": 5,
     "nodeList": [{"appType": 1, "nodeName": "test0.test.com", "tps": 71300, "capacity": 626280},
                  {"appType": 1, "nodeName": "test1.test.com", "tps": 71270, "capacity": 626130},
                  {"appType": 1, "nodeName": "test2.test.com", "tps": 71240, "capacity": 626100},
                  {"appType": 1, "nodeName": "test3.test.com", "tps": 71270, "capacity": 626190},
                  {"appType": 1, "nodeName": "test5.test.com", "tps": 71310, "capacity": 626280}], "jdnum": "1",
     "capacity": 0, "tps": 0, "gatewayUrl": None,
     "chainNodeList": [{"appType": 1, "nodeName": "test0.test.com", "tps": 71300, "capacity": 626280},
                       {"appType": 1, "nodeName": "test1.test.com", "tps": 71270, "capacity": 626130},
                       {"appType": 1, "nodeName": "test2.test.com", "tps": 71240, "capacity": 626100},
                       {"appType": 1, "nodeName": "test3.test.com", "tps": 71270, "capacity": 626190},
                       {"appType": 1, "nodeName": "test5.test.com", "tps": 71310, "capacity": 626280}],
     "certList": None, "monthPrice": {"tpsPrice": "22.92", "capacityPrice": "114.59", "flowPrice": "114.59"},
     "yearPrice": {"tpsPrice": "250.00", "capacityPrice": "1250.00", "flowPrice": "1250.00"}},
    {"nodeId": None, "orgCode": "ORG2020031819050615481", "orgName": "红枣节点（Fabric和fisco）", "spCode": "25",
     "spName": "测试企业名称", "operatorCode": "000005", "operatorName": None, "address": "中华人民共和国浙江省", "nodeNum": 3,
     "nodeList": [{"appType": 1, "nodeName": "peer1.hongzao.bsngate.com", "tps": 70420, "capacity": 629090},
                  {"appType": 1, "nodeName": "peer2.hongzao.bsngate.com", "tps": 70450, "capacity": 629080},
                  {"appType": 1, "nodeName": "peer3.hongzao.bsngate.com", "tps": 70460, "capacity": 629040}],
     "jdnum": "1", "capacity": 0, "tps": 0, "gatewayUrl": None,
     "chainNodeList": [{"appType": 1, "nodeName": "peer1.hongzao.bsngate.com", "tps": 70420, "capacity": 629090},
                       {"appType": 1, "nodeName": "peer2.hongzao.bsngate.com", "tps": 70450, "capacity": 629080},
                       {"appType": 1, "nodeName": "peer3.hongzao.bsngate.com", "tps": 70460, "capacity": 629040}],
     "certList": None, "monthPrice": {"tpsPrice": "240.10", "capacityPrice": "20.57", "flowPrice": "21.25"},
     "yearPrice": {"tpsPrice": "437.50", "capacityPrice": "6.25", "flowPrice": "1.25"}}], "code": 0, "msg": None}

usable_node = d1['rows']
ran = random.sample(list(range(len(d1['rows']))), 3)

d2 = {
    "appType": 1,
    "payType": 1,
    "appName": "app_001",
    "algorithmType": 2,
    "orgList": [
        {
            "orgCode": self.self.usable_node[ran[0]]['orgCode'],
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



print(ran[0], ran[1], ran[2])