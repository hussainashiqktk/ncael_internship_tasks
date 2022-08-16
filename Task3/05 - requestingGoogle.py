import requests
url = "https://www.google.com/search?q=cybersecurity"
response = requests.get(url)
file = open("06_response.html", "wb") #for viewing it as HTMl in browser
file = open("06_response.text", "wb") #saving response in a text file
file.write(response.content)
print(response.content)
file.close()
