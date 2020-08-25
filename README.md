# Sila-Python Full Documentation

Sila api wrapper in python

This lists the full functionality available in the Python SDK, Version 0.2. Requires python version >=3.6. This sdk abstracts the signature piece for signing the messages locally using user private keys.

## Usage

### Installation

```python

pip3 install silasdk==0.2.10rc2

```

### Initialize the application

```python
import os
from silasdk import App
from silasdk import User
from silasdk import Transaction
from silasdk import Wallet
silaApp=App("SANDBOX",app_private_key,app_handle)

```

Sets up the app private key and handle for the SDK to use for signing subsequent request. The other SDK functionality will not be available until this configuration is completed. The SDK does not store this information outside of the instance that is configured. Information like private keys etc is never transmitted over the network or stored outside the scope of this instance.
**_SECURITY ALERT_**
: : **Never transmit user private keys over the network in the request body**

## User Methods

### Check handle

```python

payload={

        "user_handle": "user.silamoney.eth"    #Required
    }

User.checkHandle(silaApp,payload)

```

**_Make sure to check the availability of user_handle before trying to register the user_**

### Success Response Object _200 OK_

```python
{
    status: 'SUCCESS',
    message: "user.silamoney.eth is available",
}
```

### Failure Response Object _200 OK_

```python
{
    status: 'FAILURE',
    message: 'user.silamoney.eth is already taken',
}
```

##

### Register a user

```python

payload={
            "country": "US",
            "user_handle": 'user1234.silamoney.eth',            # Required:  Must not be already in use
            "first_name": 'First',                              # Required
            "last_name": 'Last',                                # Required
            "email":"xxx@silamoney.com",                        # Required
            "entity_name": 'Last Family Trust',                 # Required
            "identity_value": "123452222",                      # Required:  Must in in 2222 in the sandbox
            "phone": "1234567890",                              # Required:  Must be a valid phone number (format not enforced)
            "street_address_1": '123 Main St',                  # Required:  Must be a valid USPS mailing address
            "city": 'Anytown',                                  # Required:  Must be a valid US City matching the zip
            "state": 'OR',                                      # Required:  Must be a 2 character US State abbr.
            "postal_code": "12345",                             # Required:  Must be a valid US Postal Code
            "crypto_address": '0x123...890',                    # Required:  Must be a valid ethereum 20 byte address starting with 0x
            "birthdate":"1990-05-19",                           # Required
            }

User.register(silaApp,payload)

```

### Success Response Object

```python
{
    status: 'SUCCESS',
    message: 'user.silamoney.eth has been submitted to KYC queue.',
}
```

### Failure Response Object

```python
{
    status: 'FAILURE',
    message: 'error',
}
```

##

### Request Kyc

```python

payload={

        "user_handle": "user.silamoney.eth"    #Required
    }

User.requestKyc(silaApp,payload,user_private_key, use_kyc_level=False)

```

### Custom request Kyc

```python

payload={

        "user_handle": "user.silamoney.eth"    #Required
    }

User.requestKyc(silaApp,payload,user_private_key, use_kyc_level=True)

```

### Success Response Object

```python
    {
        status: 'SUCCESS',
        message: 'user submitted for kyc',
    }
```

### Failure Response Object

```python
{
    status: 'FAILURE',
    message: 'error',
}
```

**_SECURITY ALERT_**
: :**_This sdk never transmits private keys over the network,it is advised to use a secure way for managing user private keys_**

##

### CheckKyc

```python

payload={

        "user_handle": "user.silamoney.eth"    #Required
    }

User.checkKyc(silaApp,payload,user_private_key)

```

### Success Response Object

```python
{
    status: 'SUCCESS',
    message: 'Kyc passed for user.silamoney.eth',
}
```

### Failure Response Object

```python
{
    status: 'FAILURE',
    message: 'error',
}
```

**_The python demo app in the Sila-Python github repository (https://github.com/Sila-Money/Sila-Python) shows how to use plaid plugin and get a public token to make this request_**

##

### Link Account (Plaid flow)

```python

payload={
            "public_token": "public-development-0dc5f214-56a2-4b69-8968-f27202477d3f",  # Required token from plaid
            "user_handle": "user.silamoney.eth"                                         # Required
            "account_name": "User's First Financial Checking"                           # Optional bank account name/identifier
        }

User.linkAccount(silaApp, payload, user_private_key, plaid=True)

```

### Link Account (Direct account linking flow)

```python

payload={
            "user_handle": "user.silamoney.eth",                                       # Required
            "account_number": "123456789012",                                          # Required
            "routing_number": "123456789",                                             # Required
            "account_type": "CHECKING",                                                # Optional (only CHECKING is currently supported)
            "account_name": "Custom Account Name"                                      # Optional
        }

User.linkAccount(silaApp, payload, user_private_key, plaid=False)

```

### Success Response Object

```python
{
    status: 'SUCCESS'
}
```

### Failure Response Object

```python
{
    status: 'FAILURE'
}
```

##

### Add Crypto

```python

payload={
        "crypto_address": "0x88DDBA46ddBc57a5fCbBdfa528999426993fA5aF",   # Must be a valid 20 byte ethereum address
        "user_handle":    "user.silamoney.eth"
        }

User.addCrypto(silaApp,payload,user_private_key)

```

### Success Response Object

```python
{
    status: 'SUCCESS'
}
```

### Failure Response Object

```python
{
    status: 'FAILURE'
}
```

##

### Add Identity

```python

payload={
        "identity_value": your ssn ,
        "first_name":    "first",
        "last_name" :    "last",
        "user_handle":   "user.silamoney.eth"
        }

User.addIdentity(silaApp,payload,user_private_key)

```

### Success Response Object

```python
{
    status: 'SUCCESS'
}
```

### Failure Response Object

```python
{
    status: 'FAILURE'
}
```

##

### Get Accounts

```python

payload={

        "user_handle": "user.silamoney.eth"    #Required
    }

User.getAccounts(silaApp,payload,user_private_key)            # users_private_key (256 bits) associated with ethereum address

```

### Success Response Object

```python
{
    status: 'SUCCESS'
}
```

### Failure Response Object

```python
{
    status: 'FAILURE'
}
```

##

### Get Transactions

```python

payload={

        "user_handle": "user.silamoney.eth",    #Required
        "search_filters": {                     #Optional
            "transaction_id": "some UUID string assigned by Sila",
            "reference_id": "the reference string sent in the header object when transaction request was made",
            "show_timelines": true,
            "sort_ascending": false,
            "max_sila_amount": 1300,
            "min_sila_amount": 1000,
            "statuses": ["queued", "pending", "failed", "success", "rollback", "review"],
            "start_epoch": 1234567860,
            "end_epoch": 1234567891,
            "page": 1,
            "per_page": 20,
            "transaction_types": ["issue", "redeem", "transfer"]
        }
    }

User.getTransactions(silaApp,payload,user_private_key)        #Requires 256 bit ethereum private key

```

### Success Response Object

```python
{
    status: 'SUCCESS'
}
```

### Failure Response Object

```python
{
    status: 'FAILURE'
}
```

##

### Get Sila balance 

```python
silaBalance = User.getSilaBalance(app, eth_address)
```

### Success Response Object

```python
{
  "success": true,
  "address": "0x...",
  "sila_balance": 100.0
}
```

### Failure Response Object

```python
{
  "success": false
}
```
##

### Get account balance

```python
payload = {
    "user_handle": "user.silamoney.eth",
    "account_name": "default"
}

response = User.getAccountBalance(app, payload, user_private_key)
```

### Success Response Object

```python
{
    "success": True,
    "available_balance": 100,
    "current_balance": 110,
    "masked_account_number": "0000",
    "routing_number": 123456789,
    "account_name": "default"

}
```

### Failure Response Object

```python
{
    "success": False,
    "message": "Error message"
}
```

## Transaction methods

### Plaid same day auth

```python
payload = {
    "user_handle": "user.silamoney.eth",
    "account_name": "default_plaid"
}

response = Transaction.plaidSamedayAuth(app, payload, user_private_key)
```

### Success Response Object

```python
{
  "status": "SUCCESS",
  "public_token": String,
  "message": "Plaid public token successfully created."
}
```

### Failure Response Object

```python
{
  "status": "FAILURE",
  "public_token": String,
  "message": "Message error"
}
```

##

### Issue Sila

```python

payload={
        "amount": 100000000000000000000000,
        "user_handle":   "user.silamoney.eth",
        "descriptor": "Transaction Descriptor",
        "business_uuid": "UUID of a business with an approved ACH name",
        "account_name": "account name"
        }

Transaction.issueSila(silaApp,payload,user_private_key)

```

### Success Response Object

```python
{
    status: 'SUCCESS'
}
```

### Failure Response Object

```python
{
    status: 'FAILURE'
}
```

##

### Redeem Sila

```python

payload={
        "amount": 100000000000000000000000,
        "user_handle":   "user.silamoney.eth",
        "descriptor": "Transaction Descriptor",
        "business_uuid": "UUID of a business with an approved ACH name",
        "account_name": "account name"
        }

Transaction.redeemSila(silaApp,payload,user_private_key)

```

### Success Response Object

```python
{
    status: 'SUCCESS'
}
```

### Failure Response Object

```python
{
    status: 'FAILURE'
}
```

##

### Transfer Sila

```python

payload={
        "amount": 100000000000000000000000,
        "user_handle":  "user.silamoney.eth",
        "destination_handle":  "donald.silamoney.eth",
        "descriptor": "Transaction Descriptor",
        "business_uuid": "UUID of a business with an approved ACH name"
        }

Transaction.transferSila(silaApp,payload,user_private_key)

```

**_User private key is never transmitted over the network_**

### Success Response Object

```python
{
    status: 'SUCCESS'
}
```

### Failure Response Object

```python
{
    status: 'FAILURE'
}
```

## Ethereum Wallet methods

### Create Wallet

```python
from silasdk import EthWallet

EthWallet.create("provide some entropy for randomness")
```

**_Use hd (heirarchical deterministic) wallets if you are managing users ethereum private keys_**

### Response Object

```python
{
   "eth_private_key":"************************************","eth_address":"0xD...."
}
```

### Sign a message

```python

EthWallet.signMessage("my_message","private_key")

```

### Verify signature

```python

EthWallet.verifySignature("my_message",signature)

```

## Multiple wallets

### Register Wallet

```python
payload = {
    "user_handle": "user.silamoney.eth",
    "wallet_verification_signature": "verification_signature",
    "wallet": {
        "blockchain_address": '0x123...890',
        "blockchain_network": "ETH",
        "nickname": "wallet_python_new"
    }
}

response = Wallet.registerWallet(app, payload, user_private_key)
```

### Success Response Object

```python
{
  "reference": "ref",
  "message": "Blockchain address [address] registered.",
  "success": True,
  "wallet_nickname": "new_wallet_nickname-123erf"
}
```

### Failure Response Object

```python
{
  "reference": "ref",
  "message": "Error message",
  "success": False
}
```

##

### Get Wallets

```python
payload = {
    "user_handle": "user.silamoney.eth",
    "search_filters": {
        "page": 1,
        "per_page": 20,
        "sort_ascending": False,
        "blockchain_network": "ETH",
        "blockchain_address": '0x123...890',
        "nickname": "wallet_python"
    }
}

response = Wallet.getWallets(app, payload, user_private_key)
```

### Success Response Object

```python
{
  "success": True,
  "wallets": [
    {
      "blockchain_address": "",
      "blockchain_network": "ETH",
      "default": false,
      "frozen": false,
      "nickname": ""
    },
    "page": 1,
    "returned_count": 1,
    "total_count": 1,
    "total_page_count": 1
  ]
}
```

### Failure Response Object

```python
{
  "success": True,
  "wallets": []
}
```

##

### Get Wallet

```python
payload = {
    "user_handle": "user.silamoney.eth"
}

response = Wallet.getWallet(app, payload, user_private_key)
```

### Success Response Object

```python
{
    "success": True,
    "reference": "ref",
    "wallet": {
        "nickname": "my_wallet_nickname",
        "default": False,
        "blockchain_address": "0x...",
        "blockchain_network": "ETH"
    },
    "is_whitelisted": True,
    "sila_balance": 300.0
}
```

### Failure Response Object

```python
{
    "success": False,
    "reference": "ref",
    "message": "Error message"
}
```

##

### Update Wallet

```python
payload = {
    "user_handle": "user.silamoney.eth",
    "nickname": "wallet_python_updated",
    "default": True
}

response = Wallet.updateWallet(app, payload, user_private_key)
```

### Success Response Object

```python
{
  "message": "Wallet updated.",
  "success": True,
  "wallet": {
    "blockchain_address": "(address)",
    "blockchain_network": "ETH",
    "nickname": "new_wallet_nickname",
    "default": True
  },
  "changes": [
    {
      "attribute": "nickname",
      "old_value": "",
      "new_value": "new_wallet_nickname"
    },
    {
      "attribute": "default",
      "old_value": False,
      "new_value": True
    }
  ]
}
```

### Failure Response Object

```python
{
    "message": "Wallet updated.",
    "success": True
}
```

##

### Delete Wallet

```python
payload = {
    "user_handle": "user.silamoney.eth"
}

response = Wallet.deleteWallet(app, payload, user_private_key)
```

### Success Response Object

```python
{
  "message": "Address [address] deleted; can no longer be used to sign user requests through the API.",
  "success": True,
  "reference": "ref"
}
```

### Failure Response Object

```python
{
  "message": "Error message",
  "success": False,
  "reference": "ref"
}
```

##
### Get Business Types

```python
response = BusinessInformation.getBusinessTypes(app)
```

### Success Response Object

```python
{
    "success": true,
    "business_types": [
        {
            "uuid": "4819b5f8-4cab-4366-95ec-df7a36c5c140",
            "name": "corporation",
            "label": "Corporation"
        },
        ...
    ]
}
```

##
### Get Business Roles

```python
response = BusinessInformation.getBusinessRoles(app)
```

### Success Response Object

```python
{
    "success": true,
    "business_roles": [
        {
            "uuid": "2352ec19-130d-45ba-8e0f-83a5b902e7ce",
            "name": "controlling_officer",
            "label": "Controlling Officer"
        },
        ...
    ]
}
```

##
### Get Naics Categories

```python
response = BusinessInformation.getNaicsCategories(app)
```

### Success Response Object

```python
{
    "success": true,
    "naics_categories": {
    "Accommodation and Food Services": [
            {
                "code": 721,
                "subcategory": "Accommodation"
            },
            ...
        ],
    ...
    },
    ...
}
```

##
### Link Business Member

```python
payload = {
    "user_handle": user_handle,
    "business_handle": business_handle,
    "role": "controlling_officer",
    "details": "this is the business administrator"
}
response = BusinessOperations.linkBusinessMember(app, payload, user_private_key, business_private_key)
```

### Success Response Object

```python
{
    "success": true,
    "message": "User \"Postman User\" has been made a Controlling Officer for business Sila, Inc.",
    "role": "controlling_officer",
    "details": "this is the business administrator",
    "verification_uuid": null
}
```

##
### Unlink Business Member

```python
payload = {
    "user_handle": user_handle,
    "business_handle": business_handle,
    "role": "controlling_officer"
}
response = BusinessOperations.linkBusinessMember(app, payload, user_private_key, business_private_key)
```

### Success Response Object

```python
{
    "success": true,
    "message": "User \"another_user_handle\" has been unlinked as a Controlling Officer for business Sila, Inc.",
    "role": "controlling_officer"
}
```

##
### Certify Beneficial Owner

```python
payload = {
    "user_handle": user_handle,
    "business_handle": business_handle,
    "member_handle": member_handle,
    "certification_token": certification_token
}

response = BusinessOperations.certifyBeneficialOwner(app, payload, user_private_key, business_private_key)
```

### Success Response Object

```python
{
    "success": true,
    "message": "Beneficial owner successfully certified."
}
```

##
### Certify Business

```python
payload = {
    "user_handle": user_handle,
    "business_handle": business_handle
}

response = BusinessOperations.certifyBusiness(app, payload, user_private_key, business_private_key)
```

### Success Response Object

```python
{
    "success": true,
    "message": "Business successfully certified."
}
```

##
### Get Entities

```python
payload = {
    "entity_type": "individual | business"
}

response = User.getEntities(app, payload, per_page, page)
```

### Success Response Object

```python
{
    "success": true,
    "entities": {
        "individuals": [
            {
                "handle": "app_user_1",
                "full_name": "Test User",
                "created": 1587169254,
                "status": "active",
                "blockchain_addresses": [
                    "0x0558fE768Bb4fA4D85d9A21Bf855A15Cb2841377"
                ]
            },
            ...
        ],
        "businesses": [
            {
                "handle": "biz_entity_1",
                "full_name": "Test User",
                "created": 1587169254,
                "status": "active",
                "blockchain_addresses": [
                    "0x200a260a21b4cBd17887F179549C7337FF63e0Bb"
                ],
                "uuid": "2c43d338-93aa-4132-8433-a5eef45da82d",
                "business_type": "sole_proprietorship",
                "dba": ""
            },
            ...
        ]
    },
    "pagination": {
        "returned_count": 5,
        "total_count": 5,
        "current_page": 1,
        "total_pages": 1
    }
}
```

##
### Get Entity

```python
payload = {
    "user_handle": user_handle
}

response = User.getEntity(app, payload, user_private_key)
```

### Success Response Object (Individual)

```python
{
    "success": true,
    "user_handle": "your_individual_user",
    "entity_type": "individual",
    "entity": {
        "created_epoch": 1591402237,
        "entity_name": "Postman User",
        "birthdate": "1990-08-31",
        "first_name": "Postman",
        "last_name": "User"
    },
    "addresses": [
        {
            "added_epoch": 1591402237,
            "modified_epoch": 1591402237,
            "uuid": "532e8b4c-6ba2-43e2-82d4-c3a964cef60f",
            "nickname": "Office",
            "street_address_1": "920 SW 6th Ave.",
            "street_address_2": "",
            "city": "Portland",
            "state": "OR",
            "country": "US",
            "postal_code": "97204"
        }
    ],
    "identities": [
        {
            "added_epoch": 1591402237,
            "modified_epoch": 1591402237,
            "uuid": "1e472c30-1086-4152-9092-b4eb0b268fbe",
            "identity_type": "SSN",
            "identity": "*2222"
        }
    ],
    "emails": [
        {
            "added_epoch": 1591402237,
            "modified_epoch": 1591402237,
            "uuid": "a180ad8d-02d4-4677-8b87-20a204f07c68",
            "email": "molly@silamoney.com"
        }
    ],
    "phones": [
        {
            "added_epoch": 1591402237,
            "modified_epoch": 1591402237,
            "uuid": "a33de417-4436-4cca-86ce-e8f4cea15812",
            "phone": "1231231234"
        }
    ],
    "memberships": [
        {
            "business_handle": "business_user",
            "entity_name": "Sila, Inc.",
            "role": "controlling_officer",
            "details": null,
            "ownership_stake": null,
            "certification_token": null
        },
    ]
}
```

### Success Response Object (Business)

```python
{
    "success": true,
    "user_handle": "kyb-test-3-business",
    "entity_type": "business",
    "entity": {
        "created_epoch": 1591749796,
        "entity_name": "Sila, Inc.",
        "birthdate": null,
        "business_uuid": "f9d19e39-06b1-47a2-a028-4d6a2b87db38",
        "business_type": "corporation",
        "naics_code": 721,
        "naics_category": "Accommodation and Food Services",
        "naics_subcategory": "Accommodation",
        "doing_business_as": "Sila",
        "business_website": "https://www.silamoney.com"
    },
    "addresses": [
        {
            "added_epoch": 1591749796,
            "modified_epoch": 1591749796,
            "uuid": "5adce68c-039f-4109-83ad-b91d96b989f1",
            "nickname": "Office",
            "street_address_1": "920 SW 6th Ave.",
            "street_address_2": "",
            "city": "Portland",
            "state": "OR",
            "country": "US",
            "postal_code": "97204"
        }
    ],
    "identities": [
        {
            "added_epoch": 1591749796,
            "modified_epoch": 1591749796,
            "uuid": "2807dfd5-7468-4459-b4c3-d70454e52b13",
            "identity_type": "EIN",
            "identity": "*7252"
        }
    ],
    "emails": [
        {
            "added_epoch": 1591749796,
            "modified_epoch": 1591749796,
            "uuid": "3fd08fbf-af78-4789-bd53-b7f9b2dab272",
            "email": "molly@silamoney.com"
        }
    ],
    "phones": [
        {
            "added_epoch": 1591749796,
            "modified_epoch": 1591749796,
            "uuid": "e090f8d5-fc47-4ab2-bcb7-f9381974c40b",
            "phone": "1231231234"
        }
    ],
    "members": [
        {
            "user_handle": "kyb-test-1-individual",
            "first_name": "Postman",
            "last_name": "User",
            "role": "controlling_officer",
            "details": null,
            "ownership_stake": null
        }
    ]
}
```
