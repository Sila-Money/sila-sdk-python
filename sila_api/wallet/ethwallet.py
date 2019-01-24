from web3.auto import w3


def createEthWallet():
    
    account=w3.eth.account.create()
    
    return ("This is not the recommended way to create your ethereum wallet",
            {"private_key":account.privateKey.hex(),"eth_address":account.address})
    