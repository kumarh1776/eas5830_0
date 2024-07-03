import json
from web3 import Web3
from web3.middleware import geth_poa_middleware
from web3.providers.rpc import HTTPProvider

'''If you use one of the suggested infrastructure providers, the url will be of the form
now_url  = f"https://eth.nownodes.io/{now_token}"
alchemy_url = f"https://eth-mainnet.alchemyapi.io/v2/{alchemy_token}"
infura_url = f"https://mainnet.infura.io/v3/{infura_token}"
'''

def connect_to_eth():
    url = "https://mainnet.infura.io/v3/1ca518b0b5c2414ca764e1d1dba11465"
    w3 = Web3(HTTPProvider(url))
    assert w3.is_connected(), f"Failed to connect to provider at {url}"
    return w3

def connect_with_middleware(contract_json):
    with open(contract_json, "r") as f:
        d = json.load(f)
        d = d['bsc']
        address = d['address']
        abi = d['abi']

    bnb_url = "https://data-seed-prebsc-1-s1.binance.org:8545"
    print(f"Connecting to BNB testnet: {bnb_url}")
    w3 = Web3(HTTPProvider(bnb_url))
    assert w3.is_connected(), f"Failed to connect to provider at {bnb_url}"
    print(f"Connected to BNB testnet: {w3.is_connected()}")

    w3.middleware_onion.inject(geth_poa_middleware, layer=0)

    contract = w3.eth.contract(address=address, abi=abi)

    return w3, contract

if __name__ == "__main__":
    w3_eth = connect_to_eth()
    print(f"Connected to Ethereum mainnet: {w3_eth.is_connected()}")
    print(f"Latest block: {w3_eth.eth.get_block('latest')}")

    w3_bnb, merkle_validator_contract = connect_with_middleware("contract_info.json")
    print(f"Connected to BNB testnet: {w3_bnb.is_connected()}")
    print(f"Merkle Validator contract: {merkle_validator_contract}")
