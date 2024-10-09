import unittest, silasdk

from tests.test_config import *


class Test019GetSilaBalanceTest(unittest.TestCase):
    def test_200(self):
        self.assertEqual(True, silasdk.User.getSilaBalance(app, eth_address)['success'])
        self.assertEqual(eth_address, silasdk.User.getSilaBalance(app, eth_address)['address'])


if __name__ == '__main__':
    unittest.main()
