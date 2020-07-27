import requests 
url = "http://10.128.0.36:8086/query?pretty=true&q=SELECT mean(\"usage_system\") AS \"mean_usage_system\"
 FROM \"telegraf\".\"autogen\".\"cpu\" WHERE time > now() - 5m AND \"host\"='airflow' GROUP BY time(10s) 
FILL(previous)"
# Making a get request 
response = requests.get(url) 
jsondata = response.json()
print(jsondata) 
jsonfile = open("data.json", "w")
jsonfile.write(str(jsondata))
jsonfile.close()