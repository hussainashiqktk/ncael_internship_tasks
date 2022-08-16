from urllib import response
import requests
url = "http://127.0.0.1:7777/user/?user=HUSSAINASHIQ"
response = requests.get(url)
print(response.text)
