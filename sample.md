

## 1.Required tools 

Tools and frame works needed:
  - Python >= 3.6
  - pip(python package manager)



## 2.Installation

pip install sila_api:


## 3.Usage

   - Wallet Methods

```
from sila_api import EthWallet

EthWallet.create("Provide some entropy for randomness")

```
('This is not the recommended way to create your ethereum wallet', {'private_key': '**************************************', 'eth_address': '0x328525f96B7b6AF7abfCF14E8930b1dA314044Fb'})

```
 signature=EthWallet.signMessage("My message","0x4e68dd56cb63ea4134c8c0aa12************************")
```
"9635fee544f5a1bc20d95cf3437ffade8f4f513d204fcb52fec58f61796e7c7e527f662ba11e03654e252f43fcdb44758cb520c0b2d6c3eb0c463ff81f95fedc1c"

```
EthWallet.verifySignature("My Message",signature)
```
"0x328525f96B7b6AF7abfCF14E8930b1dA314044Fb"

   
   - User Methods (Api calls)
   
   - Create new user

```
message={
        "data": {
            "address": {
                "street_address": "920 SW 6th Av",
                "country": "US",
                "city": "Portland",
                "state": "OR",
                "postal_code": "97204"
            },
            "identity": {
                "identity_type": "SSN",
                "identity_value": "2222"
            },
            "contact": {
                "phone": "571-245-5906",
                "email": "bob@silamoney.com"
            },
            "header": {
                "reference": "none",
                "created": 1234567890,
                "user_handle": "end2end.silamoney.eth",
                "auth_handle": "end2end.silamoney.eth",
                "version": "v1_1",
                "crypto": "ETH"
            },
            "crypto_entry": {
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


from sila_api import EthWallet

usersignature= EthWallet.signMessage(message,user_private_key)
appsinature= EthWallet.signMessage(message,app_private_key)

header={

    'Content-Type': 'application/json',
    "usersignature": usersignature,
    "appsignature":  appsignature
}


from sila_api import User

User.createEntity(message,header)

```



