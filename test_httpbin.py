import requests
import unittest


class TestHttpBin(unittest.TestCase):

    def test_send_get(self):
        url = "http://httpbin.org/get"
        resp = requests.get(url)
        assert resp.status_code == 200


if __name__ == '__main__':
    unittest.main()
