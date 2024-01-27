import requests
"""
response = requests.get("http://127.0.0.1:8000")

print(response.json())
"""
base_url = "http://127.0.0.1:8000"

item_id = 5
query_parm = "somevalue"

response = requests.get(f"{base_url}/items/{item_id}?q={query_parm}")
print(f"Response from '/items/{item_id}?=q{query_parm}':", response.json())
