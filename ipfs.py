import requests
import json

infura_url = "https://ipfs.infura.io:5001/api/v0"

def pin_to_ipfs(data):
		assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
		json_data = json.dumps(data)

		response = reqeusts.post(f"{infura_url}/add", files = {"file": json_data})

		if response.status_code == 200:
				cid = response.json()["Hash"]
				return cid
		else:
				raise Expection(response.text)

def get_from_ipfs(cid,content_type="json"):
		assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	
		response = requests.post(f"{infura_url}/cat?arg={cid}")
		
		if response.status_code == 200:
				if content_type = "json"
						data = response.json()
						assert isinstance(data,dict), f"get_from_ipfs should return a dict"
						return data
				else:
						raise Expection("Not dict")
		else:
				raise Expection(response.text)
