import unittest

from silasdk import User
from silasdk.tests.test_config import *


class GetSilaBalanceTest(unittest.TestCase):
    def test_200(self):
        self.assertEqual(True, User.silaBalance(app, eth_address))


if __name__ == '__main__':
    unittest.main()
