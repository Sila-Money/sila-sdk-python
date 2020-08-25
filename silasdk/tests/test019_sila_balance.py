import unittest, silasdk

from silasdk.tests.test_config import *


class GetSilaBalanceTest(unittest.TestCase):
    def test_200(self):
        # Deprecated
        # self.assertEqual(True, silasdk.User.silaBalance(app, eth_address))
        self.assertEqual(True, silasdk.User.getSilaBalance(app, eth_address)['success'])
        self.assertEqual(eth_address, silasdk.User.getSilaBalance(app, eth_address)['address'])


if __name__ == '__main__':
    unittest.main()
