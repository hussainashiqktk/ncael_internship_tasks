
#I signed up on VT and got my API key
from urllib import request

import requests

api_key = "d42b6925fe69ea9a46dfa8f46329a6b32a70c8cd1a2f5799bf960c59a36b54ab"
malacious_hash = "c0202cf6aeab8437c638533d14563d35"
url = "https://www.virustotal.com/api/v3/files/"+malacious_hash

headers = {
    "Accept": "application/json",
    "x-apikey": api_key
}

response = requests.get(url, headers=headers)
file = open("04_responseFromVirusTotal.txt", "w") #saving in text file
file.write(response.text)
file.close()
print(response.text)
