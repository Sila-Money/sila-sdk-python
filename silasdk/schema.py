Schema = [
    {"header_msg": {
        "header": {
            "reference": "",
            "created": "",
            "user_handle": "",
            "auth_handle": "",
            "version": "0.2",
            "crypto": "ETH"
        },
        "message": "header_msg",
        "kyc_level": "",
        "entity_type": ""
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
    }},
    {"business_types_msg": {
        "header": {
            "created": "",
            "auth_handle": ""
        }
    }},
    {"business_roles_msg": {
        "header": {
            "created": "",
            "auth_handle": ""
        }
    }},
    {"naics_categories_msg": {
        "header": {
            "created": "",
            "auth_handle": ""
        }
    }},
    {"entity_msg": {
        "header": {
            "created": "",
            "auth_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "message": "entity_msg",
        "address": {
            "address_alias": "default",
            "street_address_1": "",
            "city": "",
            "state": "",
            "country": "",
            "postal_code": ""
        },
        "identity": {
            "identity_alias": "SSN",
            "identity_value": ""
        },
        "contact": {
            "contact_alias": "default",
            "phone": "",
            "email": ""
        },
        "crypto_entry": {
            "crypto_alias": "default",
            "crypto_code": "ETH",
            "crypto_address": ""
        },
        "entity": {
            "first_name": "",
            "last_name": "",
            "entity_name": "",
            "birthdate": "",
            "relationship": "",
            "type": "",
            "business_type": "",
            "business_website": "",
            "doing_business_as": "",
            "naics_code": ""
        }
    }},
    {"link_business_member_msg": {
        "header": {
            "created": "",
            "auth_handle": "",
            "user_handle": "",
            "business_handle": ""
        },
        "role": "",
        "details": "",
        "ownership_stake": ""
    }},
    {"unlink_business_member_msg": {
        "header": {
            "created": "",
            "auth_handle": "",
            "user_handle": "",
            "business_handle": ""
        },
        "role": ""
    }},
    {"get_entity_msg": {
        "header": {
            "created": "",
            "auth_handle": "",
            "user_handle": ""
        }
    }},
    {"certify_beneficial_owner_msg": {
        "header": {
            "created": "",
            "auth_handle": "",
            "user_handle": "",
            "business_handle": ""
        },
        "member_handle": "",
        "certification_token": ""
    }},
    {"certify_business_msg": {
        "header": {
            "created": "",
            "auth_handle": "",
            "user_handle": "",
            "business_handle": ""
        }
    }},
    {'get_transaction_msg': {
        "header": {
            "created": '',
            "auth_handle": "",
            "user_handle": "",
            "version": "",
            "crypto": "",
            "reference": ""
        },
        "message": "get_transactions_msg",
        "search_filters": {
            "transaction_id": "",
            "reference_id": "",
            "show_timelines": '',
            "sort_ascending": '',
            "max_sila_amount": '',
            "min_sila_amount": '',
            "statuses": [],
            "start_epoch": '',
            "end_epoch": '',
            "page": '',
            "per_page": '',
            "transaction_types": []
        }
    }}
]
