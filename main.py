import requests
from datetime import datetime as dt

USERNAME = "tatoshkin"
TOKEN = "eight8character$"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
     "username": USERNAME,
     "agreeTermsOfService": "yes",
     "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name":"Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
today = dt.now()
pixela_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many km did you run today? "),
}
# response = requests.post(url=pixela_creation_endpoint,json=pixel_data, headers=headers)
# print(response.text)

update_pixel_data = {
    "quantity": "15"
}
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
# response = requests.put(url=update_endpoint, json=update_pixel_data, headers=headers)


delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
