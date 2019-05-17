# Full Documentation

This lists the full functionality available in the Python SDK, Version 0.2,requires python version >=3.6.This sdk abstracts the signature piece for signing the messages locally using user private keys.

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

### Register a user

```python

payload={
            "country": "US",
            "user_handle": 'user1234.silamoney.eth',            # Required: Must not be already in use
            "first_name": 'First',                              # Required
            "last_name": 'Last',                                # Required
            "email":"xxx@silamoney.com",                        # Required
            "entity_name": 'Last Family Trust',                 # Required
            "identity_value": your ssn,                         # Required
            "phone": 1234567890,                                # Required: Must be a valid phone number (format not enforced)
            "street_address_1": '123 Main St',                  # Required:  Must be a valid USPS mailing address
            "city": 'Anytown',                                  # Required:  Must be a valid US City matching the zip
            "state": 'OR',                                      # Required:  Must be a 2 character US State abbr.
            "postal_code": 12345,                               # Required:  Must be a valid US Postal Code
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

### requestKyc

```python

payload={

        "user_handle": "user.silamoney.eth"    #Required
    }

User.requestKyc(silaApp,payload,user_private_key)

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

### Linkaccount

```python

payload={
            "public_token": "public-development-0dc5f214-56a2-4b69-8968-f27202477d3f",  # Required token from plaid
            "user_handle": "user.silamoney.eth"                                         # Required
        }

User.linkAccount(silaApp,payload,user_private_key)

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


### addCrypto

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

### addIdentity

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

### getAccounts

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

### getTransactions

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

## Transaction methods

### IssueSila

```python

payload={
        "amount": 100000000000000000000000,                                        
        "user_handle":   "user.silamoney.eth"
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

### RedeemSila

```python

payload={
        "amount": 100000000000000000000000,                                        
        "user_handle":   "user.silamoney.eth"
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
### TransferSila

```python

payload={
        "amount": 100000000000000000000000,                                        
        "user_handle":  "user.silamoney.eth",
        "destination":  "donald.silamoney.eth"
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

