import requests
import json

response = requests.get("https://data.covid19india.org/v4/min/timeseries.min.json")
if response.status_code == 200:
    result = json.loads(response.text)
    print(result)
else:
    print("API IS NOT RESPONDING")