import requests


headers = {
    'Accept': 'application/json',
    'user-key': '64d77bbb8da06cbddfa478d08ef80aa0',
    }

# params = (
#     ('query', 'Visakhapatnam'),
# )
url = 'https://developers.zomato.com/api/v2.1/locations?query=Visakhapatnam'
response = requests.get(url, headers=headers)
result = response.json()

# for res1 in result['location_suggestions']:
#     print(res1['latitude'])
#     print(res1['longitude'])

