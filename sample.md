# Full Documentation

This lists the full functionality available in the Python SDK, Version 0.2. Requires python version >=3.6. This sdk abstracts the signature piece for signing the messages locally using user private keys.

## Usage

### Installation

```python

pip3 install silasdk

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
***SECURITY ALERT***
: : **Never transmit user private keys over the network in the request body**

##  User Methods

### Check handle

```python

payload={

        "user_handle": "user.silamoney.eth"    #Required
    }

User.checkHandle(silaApp,payload)

```
***Make sure to check the availability of user_handle before trying to register the user***

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

***SECURITY ALERT***
: :***This sdk never transmits private keys over the network,it is advised to use a secure way for managing user private keys***

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

***The python demo app in the Sila-Python github repository (https://github.com/Sila-Money/Sila-Python) shows how to use plaid plugin and get a public token to make this request***

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

        "user_handle": "user.silamoney.eth"    #Required
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
silaBalance = User.silaBalance(app, eth_address)
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
        "business_uuid": "UUID of a business with an approved ACH name"
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
        "business_uuid": "UUID of a business with an approved ACH name"
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
***User private key is never transmitted over the network***

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
***Use hd (heirarchical deterministic) wallets if you are managing users ethereum private keys***

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
