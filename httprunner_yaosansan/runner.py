import requests

session = requests.session()


def run_api(api_info: dict):
    """ 运行单个api接口
    :param api_info:
    {
        "request":{},
        "validate": {}
    }
    :return:
    """
    request = api_info['request']
    url = request.pop('url')
    method = request.pop('method')
    return session.request(method, url, **request)

