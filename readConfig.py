import os
import codecs
import configparser


proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")


class ReadConfig:
    def __init__(self):
        fd = open(configPath)
        data = fd.read()

        #  remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath, encoding='utf-8')

    def get_email(self, name):
        value = self.cf.get("EMAIL", name)
        return value

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def set_http(self, name, value):
        self.cf.set('HTTP', name, value)
        self.cf.write(open(configPath, 'w', encoding='utf-8'))

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value


if __name__ == '__main__':
    print(ReadConfig().get_http('baseurl'))