Schema = [
    {"header_msg": {
        "header": {
            "reference": "",
            "created": "",
            "user_handle": "",
            "app_handle": "",
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
            "app_handle": "",
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
            "app_handle": "",
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
            "app_handle": "",
            "user_handle": "",
        },
        "account_name": ""
    }},
    {"transfer_msg": {
        "header": {
            "created": "",
            "app_handle": "",
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
            "app_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "message": "issue_msg",
        "amount": "",
        "account_name": "",
        "business_uuid": "",
        "descriptor": "",
        "processing_type": ""
    }},
    {"redeem_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "message": "redeem_msg",
        "amount": "",
        "account_name": "",
        "business_uuid": "",
        "descriptor": "",
        "processing_type": ""
    }},
    {"no_content_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        }
    }},
    {"update_wallet_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "nickname": "",
        "default": ""
    }},
    {"register_wallet_msg": {
        "header": {
            "created": "",
            "app_handle": "",
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
            "app_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "search_filters": {
            "page": "",
            "per_page": "",
            "sort_ascending": "",
            "blockchain_network": "",
            "blockchain_address": "",
            "nickname": ""
        }
    }},
    {"get_accounts_msg": {
        "header": {
            "created": "",
            "app_handle": "",
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
            "app_handle": ""
        }
    }},
    {"business_roles_msg": {
        "header": {
            "created": "",
            "app_handle": ""
        }
    }},
    {"naics_categories_msg": {
        "header": {
            "created": "",
            "app_handle": ""
        }
    }},
    {"entity_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "message": "entity_msg",
        "address": {
            "address_alias": "",
            "street_address_1": "",
            "city": "",
            "state": "",
            "country": "",
            "postal_code": "",
            "street_address_2": ""
        },
        "identity": {
            "identity_alias": "",
            "identity_value": ""
        },
        "contact": {
            "contact_alias": "",
            "phone": "",
            "email": "",
            "sms_opt_in": ""
        },
        "crypto_entry": {
            "crypto_alias": "",
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
            "business_type_uuid": "",
            "business_website": "",
            "doing_business_as": "",
            "naics_code": ""
        },
        "device": {
            "device_fingerprint": ""
        }
    }},
    {"link_business_member_msg": {
        "header": {
            "created": "",
            "app_handle": "",
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
            "app_handle": "",
            "user_handle": "",
            "business_handle": ""
        },
        "role": ""
    }},
    {"get_entity_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": ""
        }
    }},
    {"certify_beneficial_owner_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "business_handle": ""
        },
        "member_handle": "",
        "certification_token": ""
    }},
    {"certify_business_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "business_handle": ""
        }
    }},
    {'get_transaction_msg': {
        "header": {
            "created": '',
            "app_handle": "",
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
    }},
    {'cancel_transaction_msg': {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "version": "",
            "crypto": "",
            "reference": ""
        },
        "transaction_id": ""
    }},
    {"add_registration_data_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": ""
        },
        "email": "",
        "phone": "",
        "identity_alias": "",
        "identity_value": "",
        "address_alias": "",
        "street_address_1": "",
        "street_address_2": "",
        "city": "",
        "state": "",
        "postal_code": "",
        "country": "",
        "sms_opt_in": "",
        "device_fingerprint": ""
    }},
    {"update_registration_data_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": ""
        },
        "uuid": "",
        "email": "",
        "phone": "",
        "identity_alias": "",
        "identity_value": "",
        "address_alias": "",
        "street_address_1": "",
        "street_address_2": "",
        "city": "",
        "state": "",
        "postal_code": "",
        "country": "",
        "first_name": "",
        "last_name": "",
        "entity_name": "",
        "birthdate": "",
        "business_type": "",
        "naics_code": "",
        "doing_business_as": "",
        "business_website": "",
        "sms_opt_in": ""
    }},
    {"delete_registration_data_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": ""
        },
        "uuid": ""
    }},
    {"documents_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "version": "0.2",
            "crypto": "ETH",
            "reference": ""
        },
        "message": "",
        "name": "",
        "filename": "",
        "hash": "",
        "mime_type": "",
        "document_type": "",
        "identity_type": "",
        "description": ""
    }},
    {"list_documents_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "version": "",
            "crypto": "",
            "reference": ""
        },
        "message": "",
        "start_date": "",
        "end_date": "",
        "doc_types": "",
        "search": "",
        "sort_by": ""
    }},
    {"get_document_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "user_handle": "",
            "version": "",
            "crypto": "",
            "reference": ""
        },
        "document_id": ""
    }},
    {"document_types_msg": {
        "header": {
            "created": "",
            "app_handle": "",
            "version": "",
            "crypto": "",
            "reference": ""
        }
    }},
    {"plaid_link_token_msg": {
        "header": {
            "created": "", 
            "app_handle": "", 
            "user_handle": "", 
        }
    }},
    {"delete_account": {
        "header": {
            "created": "", 
            "app_handle": "", 
            "user_handle":"", 
            "version": "0.2", 
            "crypto": "ETH", 
            "reference": ""
        },
        "account_name": ""
    }}
]
