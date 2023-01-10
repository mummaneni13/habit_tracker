import requests
from datetime import datetime

USERNAME = "mummaneni"
TOKEN = "PES@RL@NK@"
GRAPH_ID = "graph1234"
#mytrackerpage = https://pixe.la/v1/users/mummaneni/graphs/graph1234.html

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# POST( To create a user )
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Time Graph",
    "unit": "hr",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# to create a graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

date = datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": date.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today ? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date.strftime('%Y%m%d')}"


## PUT
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

## DELETE
#delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
