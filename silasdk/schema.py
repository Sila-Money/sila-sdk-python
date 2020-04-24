Schema = [
    {"header_msg_kyc_level": {
        "header": {
            "reference": "",
            "created": 1587419132,
            "user_handle": "",
            "auth_handle": "",
            "version": "0.2",
            "crypto": "ETH"
        },
        "message": "header_msg_kyc_level",
        "kyc_level": "CUSTOM_KYC_FLOW_NAME"
    }},
    {"link_account_msg": {
        "header": {
            "created": 1234567890,
            "auth_handle": "handle.silamoney.eth",
            "user_handle": "user.silamoney.eth",
            "version": "0.2",
            "crypto": "ETH",
            "reference": "ref"
        },
        "message": "link_account_msg",
        "public_token": "public-xxx-xxx",
        "account_name": "Custom Account Name",
        "selected_account_id": "optional_selected_account_id"
    }},
    {"link_account_msg_plaid": {
        "header": {
            "created": 1234567890,
            "auth_handle": "handle.silamoney.eth",
            "user_handle": "user.silamoney.eth",
            "version": "0.2",
            "crypto": "ETH",
            "reference": "ref"
        },
        "message": "link_account_msg_plaid",
        "account_number": "123456789012",
        "routing_number": "123456789",
        "account_type": "CHECKING",
        "account_name": "Custom Account Name",
        "selected_account_id": "0"
    }},
    {"account_name_msg": {
        "header": {
            "created": 1234567890,
            "auth_handle": "handle.silamoney.eth",
            "user_handle": "user.silamoney.eth",
        },
        "account_name": "Custom Account Name"
    }},
    {"transfer_msg_address": {
        "header": {
            "created": 1234567890,
            "auth_handle": "handle.silamoney.eth",
            "user_handle": "user.silamoney.eth",
            "version": "0.2",
            "crypto": "ETH",
            "reference": "ref"
        },
        "message": "transfer_msg_address",
        "amount": 13,
        "destination": "user2.silamoney.eth",
        "destination_address": "user2.silamoney.eth"
    }},
    {"no_content_msg": {
        "header": {
            "created": 1234567890,
            "auth_handle": "handle.silamoney.eth",
            "user_handle": "user.silamoney.eth",
            "version": "0.2",
            "crypto": "ETH",
            "reference": "ref"
        }
    }},
    {"update_wallet_msg": {
        "header": {
            "created": 1234567890,
            "auth_handle": "handle.silamoney.eth",
            "user_handle": "user.silamoney.eth",
            "version": "0.2",
            "crypto": "ETH",
            "reference": "ref"
        },
        "nickname": "new_wallet_nickname",
        "default": True
    }},
    {"register_wallet_msg": {
        "header": {
            "created": 1234567890,
            "auth_handle": "handle.silamoney.eth",
            "user_handle": "user.silamoney.eth",
            "version": "0.2",
            "crypto": "ETH",
            "reference": "ref"
        },
        "wallet_verification_signature": "(signature generated from signing address as the message)",
        "wallet": {
            "blockchain_address": "(address to register to user_handle)",
            "blockchain_network": "ETH",
            "nickname": "new_wallet_nickname"
        }
    }},
    {"get_wallets_msg": {
        "header": {
            "created": 1234567890,
            "auth_handle": "handle.silamoney.eth",
            "user_handle": "user.silamoney.eth",
            "version": "0.2",
            "crypto": "ETH",
            "reference": "ref"
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
            "created": 1234567890,
            "auth_handle": "handle.silamoney.eth",
            "user_handle": "user.silamoney.eth",
            "version": "0.2",
            "crypto": "ETH",
            "reference": "ref"
        },
        "message": "get_accounts_msg"
    }},
    {"sila_balance_msg": {
        "address": "0x0000"
    }}
]
