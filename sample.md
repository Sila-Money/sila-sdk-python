

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
 signature=EthWallet.signMessage("My message","0x4e68dd56cb63ea4134c8c0aa12*************************************")
```
"9635fee544f5a1bc20d95cf3437ffade8f4f513d204fcb52fec58f61796e7c7e527f662ba11e03654e252f43fcdb44758cb520c0b2d6c3eb0c463ff81f95fedc1c"

```
EthWallet.verifySignature("My Message",signature)
```
"0x328525f96B7b6AF7abfCF14E8930b1dA314044Fb"



