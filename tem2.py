import random

j = {"total": 5, "rows": [
    {"id": 7, "defaultChainCodeId": 18, "funcName": "保存数据", "ccMethod": "set", "funcType": 1, "funcTypeLabel": "invoke",
     "ccName": "FabricBaseChaincodeCN", "frameType": "fabric", "frameTypeLabel": None,
     "createTime": "2020-10-20 15:53:56"},
    {"id": 8, "defaultChainCodeId": 18, "funcName": "更新数据", "ccMethod": "update", "funcType": 1,
     "funcTypeLabel": "invoke", "ccName": "FabricBaseChaincodeCN", "frameType": "fabric", "frameTypeLabel": None,
     "createTime": "2020-10-20 15:54:29"},
    {"id": 9, "defaultChainCodeId": 18, "funcName": "删除数据", "ccMethod": "delete", "funcType": 1,
     "funcTypeLabel": "invoke", "ccName": "FabricBaseChaincodeCN", "frameType": "fabric", "frameTypeLabel": None,
     "createTime": "2020-10-20 15:54:47"},
    {"id": 10, "defaultChainCodeId": 18, "funcName": "获取数据", "ccMethod": "get", "funcType": 1,
     "funcTypeLabel": "invoke", "ccName": "FabricBaseChaincodeCN", "frameType": "fabric", "frameTypeLabel": None,
     "createTime": "2020-10-20 15:55:01"},
    {"id": 11, "defaultChainCodeId": 18, "funcName": "获取历史数据", "ccMethod": "getHistory", "funcType": 1,
     "funcTypeLabel": "invoke", "ccName": "FabricBaseChaincodeCN", "frameType": "fabric", "frameTypeLabel": None,
     "createTime": "2020-10-20 15:55:13"}], "code": 0, "msg": None}

d = j['rows']

funcs = []
for func in d:
    f = {
        "id": "",
        "funcName": func['funcName'],
        "funcType": func['funcType'],
        "ccName": func['ccName'],
        "ccMethod": func['ccMethod']
    }

    funcs.append(f)

print(len(funcs))

df = random.sample(funcs, random.randint(1, len(funcs)))

s = ''
for f in df:
    s = s + f['funcName'] + ','
    print(f['funcName'])

print(s[:-1])