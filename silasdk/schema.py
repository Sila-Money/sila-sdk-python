Schema=[   {
        "_test_uri": "/register",
        "data": {
            "address": {
                "country": "US",
                "city": "Portland",
                "address_alias": "default",
                "street_address_1": "920 SW 6th Av",
                "state": "OR",
                "postal_code": "97204-1239"
            },
            "identity": {
                "identity_alias": "SSN",
                "identity_value": "2222"
            },
            "contact": {
                "phone": "571-245-5906",
                "contact_alias": "default",
                "email": "bob@silamoney.com"
            },
            "header": {
                "reference": "none",
                "created": 1234567890,
                "user_handle": "end2end.silamoney.eth",
                "auth_handle": "end2end.silamoney.eth",
                "version": "0.1.1",
                "crypto": "ETH"
            },
            "crypto_entry": {
                "crypto_alias": "default",
                "crypto_status": "active",
                "crypto_address": "0x88DDBA46ddBc57a5fCbBdfa528999426993fA5aF",
                "crypto_code": "ETH"
            },
            "message": "entity_msg",
            "entity": {
                "birthdate": "1958-10-03",
                "entity_name": "Test User",
                "last_name": "User",
                "relationship": "developer",
                "first_name": "Test"
            }
        }
    },
    {
        "_test_uri": "/link_account",
        "data": {
            "public_token": "public-development-0dc5f214-56a2-4b69-8968-f27202477d3f",
            "account_name": "default",
            "header": {
                "reference": "none",
                "created": 1234567890,
                "user_handle": "end2end.silamoney.eth",
                "auth_handle": "end2end.silamoney.eth",
                "version": "0.1.1",
                "crypto": "ETH"
            },
            "message": "link_account_msg"
        }
    },
    {
        "_test_uri": "/issue_sila",
        "data": {
            "amount": 1,
            "account_name": "default",
            "header": {
                "reference": "none",
                "created": 1234567890,
                "user_handle": "avery.silamoney.eth",
                "auth_handle": "avery.silamoney.eth",
                "version": "0.1.1",
                "crypto": "ETH"
            },
            "message": "issue_msg"
        }
    },
    {
        "_test_uri": "/add_crypto",
        "data": {
            "header": {
                "reference": "none",
                "created": 1234567890,
                "user_handle": "end2end.silamoney.eth",
                "auth_handle": "end2end.silamoney.eth",
                "version": "0.1.1",
                "crypto": "ETH"
            },
            "crypto_entry": {
                "crypto_alias": "default",
                "crypto_status": "active",
                "crypto_address": "0x88DDBA46ddBc57a5fCbBdfa528999426993fA5aF",
                "crypto_code": "ETH"
            },
            "message": "crypto_msg"
        }
    },
    {
        "_test_uri": "/transfer_sila",
        "data": {
            "amount": 1.2,
            "destination": "bree.silamoney.xlm",
            "header": {
                "reference": "none",
                "created": 1234567890,
                "user_handle": "end2end.silamoney.eth",
                "auth_handle": "end2end.silamoney.eth",
                "version": "0.1.1",
                "crypto": "ETH"
            },
            "message": "transfer_msg"
        }
       
    },
    {
        "_test_uri": "/redeem_sila",
        "data": {
            "amount": 1.2,
            "account_name": "default",
            "header": {
                "reference": "none",
                "created": 1234567890,
                "user_handle": "end2end.silamoney.eth",
                "auth_handle": "end2end.silamoney.eth",
                "version": "0.1.1",
                "crypto": "ETH"
            },
            "message": "redeem_msg"
        }
       
    },
    {
        "_test_uri": "/check_handle",
        "data": {
            "header": {
                "reference": "none",
                "created": 1234567890,
                "user_handle": "test.silamoney.eth",
                "auth_handle": "test.silamoney.eth",
                "version": "0.1.1",
                "crypto": "ETH"
            },
            "message": "header_msg"
        }
    },
    {
        "_test_uri": "/get_accounts",
        "data": {
            "header": {
                "reference": "none",
                "created": 1234567890,
                "user_handle": "shamir.silamoney.eth",
                "auth_handle": "shamir.silamoney.eth",
                "version": "0.1.1",
                "crypto": "ETH"
            },
            "message": "get_accounts_msg"
        }
       
    },
    {
        "_test_uri": "/get_users",
        "data": {
            "header": {
                "reference": "none",
                "created": 1234567890,
                "user_handle": "shamir.silamoney.eth",
                "auth_handle": "shamir.silamoney.eth",
                "version": "0.1.1",
                "crypto": "ETH"
            },
            "message": "get_users_msg"
        }
      
    },
    {
        "_test_uri": "/check_kyc",
        "data": {
            "header": {
                "reference": "none",
                "created": 1234567890,
                "user_handle": "test.silamoney.eth",
                "auth_handle": "test.silamoney.eth",
                "version": "0.1.1",
                "crypto": "ETH"
            },
            "message": "header_msg"
        }
    },
    {
        "_test_uri": "/request_kyc",
        "data": {
            "header": {
                "reference": "none",
                "created": 1234567890,
                "user_handle": "test.silamoney.eth",
                "auth_handle": "test.silamoney.eth",
                "version": "0.1.1",
                "crypto": "ETH"
            },
            "message": "header_msg"
        }
    },
    {
        "_test_uri": "/add_crypto",
        "data": {
            "header": {
                "reference": "none",
                "created": 1234567890,
                "user_handle": "end2end.silamoney.eth",
                "auth_handle": "end2end.silamoney.eth",
                "version": "0.1.1",
                "crypto": "ETH"
            },
            "crypto_entry": {
                "crypto_alias": "default",
                "crypto_status": "active",
                "crypto_address": "0x88DDBA46ddBc57a5fCbBdfa528999426993fA5aF",
                "crypto_code": "ETH"
            },
            "message": "crypto_msg"
        }
      
    },
    {
        "_test_uri": "/add_identity",
        "data": {
            "country": "US",
            "identity": {
                "identity_alias": "SSN",
                "identity_value": "2222"
            },
            "header": {
                "reference": "none",
                "created": 1234567890,
                "user_handle": "end2end.silamoney.eth",
                "auth_handle": "end2end.silamoney.eth",
                "version": "0.1.1",
                "crypto": "ETH"
            },
            "message": "identity_msg",
            "entity": {
                "last_name": "silver",
                "relationship": "user",
                "first_name": "Bob"
            }
        }
    }]