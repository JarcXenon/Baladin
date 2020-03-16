import requests
import json

n = 45.7536
s = 45.7305
e = 4.8937
w = 4.8469


bbox = (s,w,n,e)
condition = ["historic"]

overpass_url = "http://overpass-api.de/api/interpreter"
overpass_query = f"""[out:json];
nwr{condition}{bbox};
out;
"""

print(overpass_query)

response = requests.get(overpass_url, 
                        params={'data': overpass_query})
data = response.json()
