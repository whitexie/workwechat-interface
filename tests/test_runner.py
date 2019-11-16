import os
import unittest

from httprunner_yaosansan.loader import load_yaml
from httprunner_yaosansan.runner import run_api, run_yaml


class TestRunner(unittest.TestCase):

    def test_run_api(self):
        api_path = os.path.join(os.path.dirname(__file__), 'api', 'httpbin_get.yml')
        api_info = load_yaml(api_path)
        success = run_api(api_info)
        self.assertTrue(success)

        api_path = os.path.join(os.path.dirname(__file__), 'api', 'httpbin_post.yml')
        api_info = load_yaml(api_path)
        success = run_api(api_info)
        self.assertTrue(success)

    def test_run_yaml(self):
        api_path = os.path.join(os.path.dirname(__file__), 'testcases', 'mubu_login.yml')
        results = run_yaml(api_path)
        self.assertEqual(len(results), 3)