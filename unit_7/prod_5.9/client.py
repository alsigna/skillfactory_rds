import requests

resp = requests.post("http://127.0.0.1:5000/add", json={"num": 15})
print(resp.status_code)

if resp.status_code == 200:
    print(resp.json()["result"])
else:
    print(resp.text)
