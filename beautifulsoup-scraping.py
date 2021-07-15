import json
import requests
from bs4 import BeautifulSoup

data = {
    "sort": "Einfahrtzeit-desc",
    "page": "1",
    "pageSize": "10",
    "group": "",
    "filter": "",
    "__RequestVerificationToken": "",
    "locid": "1",
}

headers = {"X-Requested-With": "XMLHttpRequest"}

url = "https://www.laerm-monitoring.de/zug/"
api_url = "https://www.laerm-monitoring.de/zug/train_read"

with requests.Session() as s:
    soup = BeautifulSoup(s.get(url).content, "html.parser")
    data["__RequestVerificationToken"] = soup.select_one(
        '[name="__RequestVerificationToken"]'
    )["value"]
    data = s.post(api_url, data=data, headers=headers).json()

# pretty print the data
print(json.dumps(data, indent=4))
