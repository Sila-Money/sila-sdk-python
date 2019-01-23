from web3.auto import w3


def createEthWallet(pass_phrase):
    
    account=w3.eth.account.create(pass_phrase)
    
    return {"private_key":account.privateKey,"eth_address":account.address}
    