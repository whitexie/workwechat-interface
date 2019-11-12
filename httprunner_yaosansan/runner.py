import requests
import jsonpath

session = requests.session()


def extract_json_field(resp, key):
    """

    :param resp: (requests.models.Response)
    :param key: (str) $.code
    :return:
    """
    print('resp------', type(resp))
    values = jsonpath.jsonpath(resp.json(), key)
    return values[0]


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

    resp = session.request(method, url, **request)

    validator_mapping = api_info['validate']
    for key, value in validator_mapping.items():
        if '$' in key:
            actual_value = extract_json_field(resp, key)
        else:
            actual_value = getattr(resp, key)

        assert actual_value == value
    return True

