import location
import requests

headers = {
    'Accept': 'application/json',
    'user-key': '64d77bbb8da06cbddfa478d08ef80aa0',
    }


for res1 in location.result['location_suggestions']:
    lat = res1['latitude']
    lon = res1['longitude']


search_url = "https://developers.zomato.com/api/v2.1/search?q="+"pizza"+"&lat="+str(lat)+"&lon="+str(lon)
search_response = requests.get(search_url, headers=headers)
search_result = search_response.json()

for sr in search_result['restaurants']:
    print(sr['restaurant'])
