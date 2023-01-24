import requests
import pandas as pd
url = "https://api.bigcommerce.com/stores/3l9ek/v3/catalog/trees/categories"
querystring = {"limit": "500"}
headers = {
    "Content-Type": "application/json",
    "X-Auth-Token": "oy0mgky1u7znihvjspg37u2f2fnm2n0"
}
response = requests.request("GET", url, headers=headers, params=querystring)

data = response.json()
secdata=list(data['data'])
# print(len(secdata))
finalData=[]
for points in secdata:
    finalData.append({"Id": points['category_id'], "name": points['name']})

df = pd.DataFrame(finalData)

df.to_csv('data.csv', index=False, columns=['Id', 'name'])