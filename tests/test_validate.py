import unittest
import os
from httprunner_yaosansan.loader import load_yaml
from httprunner_yaosansan.validate import is_testcase, is_api


class TestValidate(unittest.TestCase):

    def test_is_testcase(self):
        yaml_path = os.path.join(os.path.dirname(__file__), 'testcases', 'mubu_login.yml')
        yaml_dict = load_yaml(yaml_path)

        self.assertTrue(is_testcase(yaml_dict))

    def test_is_api(self):
        yaml_path = os.path.join(os.path.dirname(__file__), 'api', 'httpbin_get.yml')
        yaml_dict = load_yaml(yaml_path)

        self.assertTrue(is_api(yaml_dict))
