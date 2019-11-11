import unittest
import os
from httprunner_yaosansan.loader import load_yaml


class TestLoader(unittest.TestCase):

    def test_load_yaml(self):
        """加载出的接口请求参数与原始信息一致
        """
        yaml_file_path = os.path.join(os.path.dirname(__file__), 'api', 'httpbin_get.yml')
        json_object = load_yaml(yaml_file_path)
        self.assertEqual(json_object['url'], 'http://httpbin.org/get')
