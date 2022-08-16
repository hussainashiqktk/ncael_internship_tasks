from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/aphrodite"
page = urlopen(url) #urlopen() returns an HTTPResponse object:
# html_bytes = page.read()
# html = html_bytes.decode("utf-8")
# f = open("test.html", "w")
# f.writelines(html)
# print(html)

