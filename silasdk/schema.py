Schema = [
    {"header_msg": {
        "header": {
            "reference": None,
            "created": None,
            "user_handle": None,
            "app_handle": None,
            "version": "0.2",
            "crypto": "ETH"
        },
        "message": "header_msg",
        "kyc_level": None,
        "entity_type": None
    }},
    {"link_account_msg_plaid": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "version": "0.2",
            "crypto": "ETH",
            "reference": None
        },
        "message": "link_account_msg",
        "plaid_token": None,
        "account_name": None,
        "selected_account_id": None,
        "plaid_token_type": None
    }},
    {"link_account_msg_mx": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "version": "0.2",
            "crypto": "ETH",
            "reference": None
        },
        "message": "link_account_msg",
        "provider": None,
        "provider_token_type": None,
        "provider_token": None,
        "account_name": None,
        "selected_account_id": None
    }},
    {"link_account_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "version": "0.2",
            "crypto": "ETH",
            "reference": None
        },
        "message": "link_account_msg",
        "account_number": None,
        "routing_number": None,
        "account_type": None,
        "account_name": None,
        "selected_account_id": None
    }},
    {"account_name_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "reference": None
        },
        "account_name": None
    }},
    {"transfer_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "version": "0.2",
            "crypto": "ETH",
            "reference": None
        },
        "message": "transfer_msg",
        "amount": None,
        "destination": None,
        "destination_handle": None,
        "destination_wallet": None,
        "destination_address": None,
        "business_uuid": None,
        "descriptor": None,
        "source_id": None,
        "destination_id": None,
        "transaction_idempotency_id":None
    }},
    {"issue_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "version": "0.2",
            "crypto": "ETH",
            "reference": None
        },
        "message": "issue_msg",
        "amount": None,
        "account_name": None,
        "card_name": None,
        "business_uuid": None,
        "descriptor": None,
        "processing_type": None,
        "source_id": None,
        "destination_id": None,
        "transaction_idempotency_id":None
    }},
    {"redeem_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "version": "0.2",
            "crypto": "ETH",
            "reference": None
        },
        "message": "redeem_msg",
        "amount": None,
        "account_name": None,
        "card_name": None,
        "business_uuid": None,
        "descriptor": None,
        "processing_type": None,
        "source_id": None,
        "destination_id": None,
        "mock_wire_account_name": None,
        "transaction_idempotency_id":None
    }},
    {"no_content_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "version": "0.2",
            "crypto": "ETH",
            "reference": None
        }
    }},
    {"update_wallet_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "version": "0.2",
            "crypto": "ETH",
            "reference": None
        },
        "nickname": None,
        "default": None,
        "statements_enabled": None
    }},
    {"register_wallet_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "version": "0.2",
            "crypto": "ETH",
            "reference": None
        },
        "wallet_verification_signature": None,
        "wallet": {
            "blockchain_address": None,
            "blockchain_network": "ETH",
            "nickname": None,
            "default": None,
            "statements_enabled": None
        }
    }},
    {"get_wallets_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "version": "0.2",
            "crypto": "ETH",
            "reference": None
        },
        "search_filters": {
            "page": None,
            "per_page": None,
            "sort_ascending": None,
            "blockchain_network": None,
            "blockchain_address": None,
            "nickname": None,
            "wallet_id":None
        }
    }},
    {"get_accounts_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "version": "0.2",
            "crypto": "ETH",
            "reference": None
        },
        "message": "get_accounts_msg"
    }},
    {"sila_balance_msg": {
        "address": None
    }},
    {"business_types_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "reference": None
        }
    }},
    {"business_roles_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "reference": None
        }
    }},
    {"naics_categories_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "reference": None
        }
    }},
    {"entity_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "version": "0.2",
            "crypto": "ETH",
            "reference": None
        },
        "message": "entity_msg",
        "address": {
            "address_alias": None,
            "street_address_1": None,
            "city": None,
            "state": None,
            "country": None,
            "postal_code": None,
            "street_address_2": None
        },
        "identity": {
            "identity_alias": None,
            "identity_value": None
        },
        "contact": {
            "contact_alias": None,
            "phone": None,
            "email": None,
            "sms_opt_in": None
        },
        "crypto_entry": {
            "crypto_alias": None,
            "crypto_code": "ETH",
            "crypto_address": None
        },
        "entity": {
            "first_name": None,
            "last_name": None,
            "entity_name": None,
            "birthdate": None,
            "relationship": None,
            "type": None,
            "business_type": None,
            "business_type_uuid": None,
            "business_website": None,
            "doing_business_as": None,
            "naics_code": None,
            "registration_state":None
        },
        "device": {
            "device_fingerprint": None,
            "session_identifier": None
        }
    }},
    {"link_business_member_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "business_handle": None,
            "reference": None
        },
        "role": None,
        "details": None,
        "ownership_stake": None
    }},
    {"unlink_business_member_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "business_handle": None,
            "reference": None
        },
        "role": None
    }},
    {"get_entity_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "reference": None
        }
    }},
    {"certify_beneficial_owner_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "business_handle": None,
            "reference": None
        },
        "member_handle": None,
        "certification_token": None
    }},
    {"certify_business_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "business_handle": None,
            "reference": None
        }
    }},
    {'get_transaction_msg': {
        "header": {
            "created": '',
            "app_handle": None,
            "user_handle": None,
            "version": None,
            "crypto": None,
            "reference": None
        },
        "message": "get_transactions_msg",
        "search_filters": {
            "transaction_id": None,
            "reference_id": None,
            "show_timelines": '',
            "sort_ascending": '',
            "max_sila_amount": '',
            "min_sila_amount": '',
            "statuses": [],
            "start_epoch": '',
            "end_epoch": '',
            "page": '',
            "per_page": '',
            "transaction_types": [],
            "bank_account_name":None,
            "processing_type": None,
            "payment_method_id":None,
        }
    }},
    {'cancel_transaction_msg': {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "version": None,
            "crypto": None,
            "reference": None
        },
        "transaction_id": None
    }},
    {"add_registration_data_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "reference": None
        },
        "email": None,
        "phone": None,
        "identity_alias": None,
        "identity_value": None,
        "address_alias": None,
        "street_address_1": None,
        "street_address_2": None,
        "city": None,
        "state": None,
        "postal_code": None,
        "country": None,
        "sms_opt_in": None,
        "device_fingerprint": None,
        "session_identifier": None,
        "registration_state":None
    }},
    {"update_registration_data_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "reference": None
        },
        "uuid": None,
        "email": None,
        "phone": None,
        "identity_alias": None,
        "identity_value": None,
        "address_alias": None,
        "street_address_1": None,
        "street_address_2": None,
        "city": None,
        "state": None,
        "postal_code": None,
        "country": None,
        "first_name": None,
        "last_name": None,
        "entity_name": None,
        "birthdate": None,
        "business_type": None,
        "naics_code": None,
        "doing_business_as": None,
        "business_website": None,
        "sms_opt_in": None,
        "registration_state":None
    }},
    {"delete_registration_data_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "reference": None
        },
        "uuid": None
    }},
    {"documents_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "version": "0.2",
            "crypto": "ETH",
            "reference": None
        },
        "message": None,
        "name": None,
        "filename": None,
        "hash": None,
        "mime_type": None,
        "document_type": None,
        "description": None,
        "file_metadata" :None
    }},
    {"list_documents_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "version": None,
            "crypto": None,
            "reference": None
        },
        "message": None,
        "start_date": None,
        "end_date": None,
        "doc_types": None,
        "search": None,
        "sort_by": None
    }},
    {"get_document_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "version": None,
            "crypto": None,
            "reference": None
        },
        "document_id": None
    }},
    {"document_types_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "version": None,
            "crypto": None,
            "reference": None
        }
    }},
    {"plaid_link_token_msg": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "reference": None
        },
        "android_package_name": None
    }},
    {"delete_account": {
        "header": {
            "created": None,
            "app_handle": None,
            "user_handle": None,
            "version": "0.2",
            "crypto": "ETH",
            "reference": None
        },
        "account_name": None
    }},
    {
        "check_partner_kyc": {
            "header": {
                "created": None,
                "app_handle": None,
                "version": "0.2",
                "crypto": "ETH",
                "reference": None
            },
            "query_app_handle": None,
            "query_user_handle": None
        }
    },
    {
        "update_account": {
            "header": {
                "created": None,
                "app_handle": None,
                "user_handle": None,
                "version": "0.2",
                "crypto": "ETH",
                "reference": None
            },
            "account_name": None,
            "new_account_name": None,
            "active": None
        }
    },
    {
        "plaid_update_link_token": {
            "header": {
                "created": None,
                "app_handle": None,
                "user_handle": None
            },
            "account_name": None,
        }
    },
    {
        'check_instant_ach': {
            "header": {
                "created": '',
                "app_handle": None,
                "user_handle": None,
                "version": "0.2",
                "crypto": "ETH",
                "reference": None
            },
            "account_name": None,
            "kyc_level": None
        }
    },
    {
        "get_institutions": {
            "header": {
                "created": None,
                "app_handle": None,
                "reference": None
            },
            "message": "header_msg",
            "search_filters": {
                "institution_name": None,
                "routing_number": None,
                "page": None,
                "per_page": None
            }
        }
    },
    {
        "link_card_msg": {
            "header": {
                "created": None,
                "app_handle": None,
                "user_handle": None,
                "version": "0.2",
                "crypto": "ETH",
                "reference": None
            },
            "message": "header_msg",
            "card_name": None,
            "account_postal_code": None,
            "token": None,
            "provider": None,
            "skip_verification" : None ,
        }
    },
    {
        "get_cards": {
            "header": {
                "created": None,
                "app_handle": None,
                "user_handle": None,
                "reference": None
            },
            "message": "header_msg"
        }
    },
    {
        "delete_card": {
            "header": {
                "created": None,
                "app_handle": None,
                "user_handle": None,
                "reference": None
            },
            "message": "header_msg",
            "card_name": None,
            "provider" : None
        }
    },
    {
        "reverse_transaction_msg": {
            "header": {
                "created": None,
                "app_handle": None,
                "user_handle": None,
                "version": None,
                "crypto": None,
                "reference": None
            },
            "transaction_id": None
        }
    },
    {
        "get_webhooks": {
            "header": {
                "created": None,
                "app_handle": None,
                "user_handle": None,
                "reference": None,
                "version": "0.2",
                "crypto": "ETH"
            },
            "message": "header_msg",
            "search_filters": {
                "uuid": None,
                "delivered": None,
                "sort_ascending": None,
                "event_type": None,
                "endpoint_name": None,
                "user_handle": None,
                "start_epoch": None,
                "end_epoch": None,
                "page": None,
                "per_page": None
            }
        }
    },
    {
        "retry_webhook": {
            "header": {
                "created": None,
                "app_handle": None,
                "user_handle": None,
                "reference": None,
                "version": "0.2",
                "crypto": "ETH"
            },
            "message": "header_msg",
            "event_uuid": None,
        }
    },
    {
        "open_virtual_acc": {
            "header": {
                "created": None, 
                "auth_handle": None, 
                "app_handle": None,
                "user_handle": None, 
                "version": "0.2", 
                "crypto": "ETH", 
                "reference": None
            },
            "virtual_account_name": None,
            "ach_credit_enabled": None,
            "ach_debit_enabled": None,
            "statements_enabled": None
        }
    },
    {
        "get_virtual_acc": {
            "header": {
                "created": None, 
                "auth_handle": None, 
                "user_handle": None,
                "app_handle": None,
                "version": "0.2", 
                "crypto": "ETH", 
                "reference": None
            },
            "virtual_account_id": None
        }
    },
    {
        "get_virtual_accounts_msg": {
            "header": {
                "created": None, 
                "auth_handle": None, 
                "user_handle": None,
                "app_handle": None,
                "version": "0.2", 
                "crypto": "ETH", 
                "reference": None
            }
        }
    },
    {
        "update_virtual_account_msg": {
            "header": {
                "created": None, 
                "auth_handle": None, 
                "user_handle": None, 
                "app_handle": None,
                "version": "0.2", 
                "crypto": "ETH", 
                "reference": None
            },
            "virtual_account_id": None,
            "virtual_account_name": None,
            "active": None,
            "ach_credit_enabled": None,
            "ach_debit_enabled": None
        }
    },
    {
        "get_payment_methods":{
            "header": {
                "created": None,
                "auth_handle": None,
                "user_handle": None,
                "app_handle": None,
                "reference": None,
            }
        }
    },
    {
        "close_virtual_account_msg": {
            "header": {
                "created": None, 
                "auth_handle": None, 
                "user_handle": None, 
                "app_handle": None,
                "version": "0.2", 
                "crypto": "ETH", 
                "reference": None
            },
            "virtual_account_id": None,
            "account_number": None,
        }
    },
    {
        "create_test_virtual_account_ach_transaction_msg": {
            "header": {
                "created": None, 
                "auth_handle": None, 
                "user_handle": None, 
                "app_handle": None,
                "version": "0.2", 
                "crypto": "ETH", 
                "reference": None
            },
            "amount": None,
            "virtual_account_number": None,
            "tran_code": None,
            "effective_date": None,
            "entity_name": None,
            "ced": None,
            "ach_name": None
        }
    },
    {
        "approve_wire_msg": {
            "header": {
                "created": None, 
                "auth_handle": None, 
                "user_handle": None, 
                "app_handle": None,
                "version": "0.2", 
                "crypto": "ETH", 
                "reference": None
            },
            "transaction_id": None,
            "approve": None,
            "notes": None,
            "mock_wire_account_name": None,

        }
    },
    {
        "mock_wire_out_file_msg": {
            "header": {
                "created": None, 
                "auth_handle": None, 
                "user_handle": None, 
                "app_handle": None,
                "version": "0.2", 
                "crypto": "ETH", 
                "reference": None
            },
            "transaction_id": None,
            "wire_status": None,
        }
    },
    {
    "get_statements_data_msg":{
      "header": {
        "created": None,
        "app_handle": None,
        "user_handle": None,
        "version": "0.2",
        "crypto": "ETH",
        "reference":  None
      },
       "search_filters":{
           "month": None,
           "page":None,
           "per_page":None
       }
    }
    },
    {
    "get_wallet_statement_data_msg":{
      "header": {
        "created": None,
        "app_handle": None,
        "user_handle":None,
        "version": "0.2",
        "crypto": "ETH",
        "reference": None
      },
       "wallet_id": None,
       "search_filters":{
           "start_month": None,
           "end_month":None,
           "page":None,
           "per_page":None
       }
    }
    },
    {
    "statements_msg":{
    "header": {
        "created": None, 
        "app_handle": None, 
        "user_handle": None, 	
        "version": "0.2", 
        "crypto": "ETH", 
        "reference":  None
    }, 
    "search_filters":{
        "start_date": None,
        "end_date": None,
        "user_name": None,
        "user_handle": None,
        "account_type": None,
        "email": None,
        "status": None,
        "identifier": None,
        "page": None,
        "per_page": None
        }
    }
    },

   {
    "resend_statements_msg":{
    "header": {
        "created": None, 
        "app_handle": None, 
        "user_handle":None, 
        "version": "0.2", 
        "crypto": "ETH", 
        "reference":None
    }, 
    "email":None
    }
    },

    {
    "refund_debit_card_msg":{
     "header": {
        "created": None,
        "app_handle": None,
        "user_handle":None,
        "version": "0.2",
        "crypto": "ETH",
        "reference": None
      },
    "transaction_id": None
    }
    },

    {
    "create_cko_testing_token_msg":{
     "header": {
        "created": None,
        "app_handle": None,
        "user_handle":None,
        "version": "0.2",
        "crypto": "ETH",
        "reference": None
      },
    "card_number": None,
    "expiry_month": None, 
    "expiry_year": None,
    "cvv": None,
    "cko_public_key": None
    }
    },
]
