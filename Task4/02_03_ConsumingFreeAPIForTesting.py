
import requests
response = requests.get("https://api.thedogapi.com/v1/breeds")
print(response.text)