Schema = [
    {"header_msg_kyc_level": {
        "header": {
            "reference": "",
            "created": "",
            "user_handle": "",
            "auth_handle": "",
            "version": "0.2",
            "crypto": "ETH"
        },
        "message": "header_msg",
        "kyc_level": ""
    }},
    {"link_account_msg_plaid": {
        "header": {
            "created": "",
            "auth_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "message": "link_account_msg",
        "public_token": "",
        "account_name": "",
        "selected_account_id": ""
    }},
    {"link_account_msg": {
        "header": {
            "created": "",
            "auth_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "message": "link_account_msg",
        "account_number": "",
        "routing_number": "",
        "account_type": "",
        "account_name": "",
        "selected_account_id": ""
    }},
    {"account_name_msg": {
        "header": {
            "created": "",
            "auth_handle": "",
            "user_handle": "",
        },
        "account_name": ""
    }},
    {"transfer_msg": {
        "header": {
            "created": "",
            "auth_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "message": "transfer_msg",
        "amount": "",
        "destination": "",
        "destination_handle": "",
        "destination_wallet": "",
        "destination_address": "",
        "business_uuid": "",
        "descriptor": ""
    }},
    {"issue_msg": {
        "header": {
            "created": "",
            "auth_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "message": "issue_msg",
        "amount": "",
        "account_name": "",
        "business_uuid": "",
        "descriptor": ""
    }},
    {"redeem_msg": {
        "header": {
            "created": "",
            "auth_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "message": "redeem_msg",
        "amount": "",
        "account_name": "",
        "business_uuid": "",
        "descriptor": ""
    }},
    {"no_content_msg": {
        "header": {
            "created": "",
            "auth_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        }
    }},
    {"update_wallet_msg": {
        "header": {
            "created": "",
            "auth_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "nickname": "",
        "default": False
    }},
    {"register_wallet_msg": {
        "header": {
            "created": "",
            "auth_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "wallet_verification_signature": "",
        "wallet": {
            "blockchain_address": "",
            "blockchain_network": "ETH",
            "nickname": ""
        }
    }},
    {"get_wallets_msg": {
        "header": {
            "created": "",
            "auth_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "search_filters": {
            "page": 1,
            "per_page": 20,
            "sort_ascending": False,
            "blockchain_network": "ETH",
            "blockchain_address": "",
            "nickname": ""
        }
    }},
    {"get_accounts_msg": {
        "header": {
            "created": "",
            "auth_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "message": "get_accounts_msg"
    }},
    {"sila_balance_msg": {
        "address": ""
    }}
]
