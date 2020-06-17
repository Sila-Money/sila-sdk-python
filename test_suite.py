import coverage
import os
import unittest
import xmlrunner

from silasdk.tests.test001_check_handle import Test001CheckHandleTest
from silasdk.tests.test002_register import Test002RegisterTest
from silasdk.tests.test003_check_handle_failure import Test003CheckHandleFailTest
from silasdk.tests.test004_request_kyc import Test004RequestKycTest
from silasdk.tests.test005_check_kyc import Test005CheckKycTest
from silasdk.tests.test006_link_account import Test006LinkAccountTest
from silasdk.tests.test007_get_accounts import Test007GetAccountsTest
from silasdk.tests.test008_get_account_balance import Test008GetAccountBalanceTest
from silasdk.tests.test009_issue_sila import Test009IssueSilaTest
from silasdk.tests.test010_transfer_sila import Test010TrasferSilaTest
from silasdk.tests.test011_redeem_sila import Test011RedeemSilaTest
from silasdk.tests.test012_get_transactions import Test012GetTransactionsTest
from silasdk.tests.test013_plaid_same_day_auth import Test013PlaidSameDayAuthTest
from silasdk.tests.test014_register_wallet import Test014RegisterWalletTest
from silasdk.tests.test015_get_wallets import Test015GetWalletsTest
from silasdk.tests.test016_get_wallet import Test016GetWalletTest
from silasdk.tests.test017_update_wallet import Test017UpdateWalletTest
from silasdk.tests.test018_delete_wallet import Test018DeleteWalletTest


def create_suite(classes):
    suite = unittest.TestSuite()
    for _class in classes:
        _object = _class()
        for function_name in dir(_object):
            if function_name.lower().startswith("test"):
                suite.addTest(_class(function_name))
    return suite


def run_unit_tests():
    cov = coverage.Coverage()
    cov.start()
    results = os.path.abspath('./test-results.xml')
    print(results)
    print('test')
    with open(results, 'wb') as output:
        runner=xmlrunner.XMLTestRunner(output=output, buffer=False)
        classes = [
            Test001CheckHandleTest,
            Test002RegisterTest,
            Test003CheckHandleFailTest,
            Test004RequestKycTest,
            Test005CheckKycTest,
            Test006LinkAccountTest,
            Test007GetAccountsTest,
            Test008GetAccountBalanceTest,
            Test009IssueSilaTest,
            Test010TrasferSilaTest,
            Test011RedeemSilaTest,
            Test012GetTransactionsTest,
            Test013PlaidSameDayAuthTest,
            Test014RegisterWalletTest,
            Test015GetWalletsTest,
            Test016GetWalletTest,
            Test017UpdateWalletTest,
            Test018DeleteWalletTest
        ]
        runner.run(create_suite(classes))
    cov.stop()
    cov.save()

    cov.xml_report()


if __name__ == "__main__":
    run_unit_tests()
