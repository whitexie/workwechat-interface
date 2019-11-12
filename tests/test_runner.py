import os
import unittest

from httprunner_yaosansan.loader import load_yaml
from httprunner_yaosansan.runner import run_api


class TestRunner(unittest.TestCase):

    def test_run_api(self):
        api_path = os.path.join(os.path.dirname(__file__), 'api', 'httpbin_get.yml')
        api_info = load_yaml(api_path)
        resp = run_api(api_info)
        self.assertEqual(resp.status_code, 200)
