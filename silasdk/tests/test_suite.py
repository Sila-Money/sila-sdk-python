import unittest

from silasdk.tests.test001_check_handle import CheckHandleTest
from silasdk.tests.test002_register import RegisterTest
from silasdk.tests.test003_check_handle_failure import CheckHandleFailTest
from silasdk.tests.test004_request_kyc import RequestKycTest
from silasdk.tests.test005_check_kyc import CheckKycTest
from silasdk.tests.test006_link_account import LinkAccountTest
from silasdk.tests.test007_get_accounts import GetAccountsTest
from silasdk.tests.test008_get_account_balance import GetAccountBalanceTest
from silasdk.tests.test009_issue_sila import IssueSilaTest
from silasdk.tests.test010_transfer_sila import TrasferSilaTest
from silasdk.tests.test011_redeem_sila import RedeemSilaTest
from silasdk.tests.test012_get_transactions import GetTransactionsTest
from silasdk.tests.test013_plaid_same_day_auth import PlaidSameDayAuthTest
from silasdk.tests.test014_register_wallet import RegisterWalletTest
from silasdk.tests.test015_get_wallets import GetWalletsTest
from silasdk.tests.test016_get_wallet import GetWalletTest
from silasdk.tests.test017_update_wallet import UpdateWalletTest
from silasdk.tests.test018_delete_wallet import DeleteWalletTest


def create_suite(classes):
    suite = unittest.TestSuite()
    for _class in classes:
        _object = _class()
        for function_name in dir(_object):
            if function_name.lower().startswith("test"):
                suite.addTest(_class(function_name))
    return suite


def run_unit_tests():
    runner = unittest.TextTestRunner()
    classes = [
        CheckHandleTest,
        RegisterTest,
        CheckHandleFailTest,
        RequestKycTest,
        CheckKycTest,
        LinkAccountTest,
        GetAccountsTest,
        GetAccountBalanceTest,
        IssueSilaTest,
        TrasferSilaTest,
        RedeemSilaTest,
        GetTransactionsTest,
        PlaidSameDayAuthTest,
        RegisterWalletTest,
        GetWalletsTest,
        GetWalletTest,
        UpdateWalletTest,
        DeleteWalletTest
    ]
    runner.run(create_suite(classes))


if __name__ == "__main__":
    run_unit_tests()
