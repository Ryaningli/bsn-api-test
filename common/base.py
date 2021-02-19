import requests


class Base:
    def base_response(self, url, headers, data, timeout=2):
        response = requests.session().request()