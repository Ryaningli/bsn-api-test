import common
import readConfig
from common.configHttp import ConfigHttp
from common.Log import MyLog

logger = MyLog.get_log()
log = logger.get_logger()


def get_token():
    ch = ConfigHttp()
    rc = readConfig.ReadConfig()
    username = rc.get_http('username')
    password = rc.get_http('password')
    data = {
        'phone': username,
        'password': password
    }

    ch.set_url(common.login)
    ch.set_data(data)
    try:
        res = ch.post_json()
        assert res.json()['code'] == 0
        log.info('获取token成功')
        return eval(res.text)['data']['token']
    except AssertionError:
        log.error('获取token失败')


if __name__ == '__main__':
    print(get_token())