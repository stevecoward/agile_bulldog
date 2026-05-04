import urllib.request

url = "http://localhost:8000/"

with urllib.request.urlopen(url) as response:
    data = response.read()
    with open("response.txt", "w", encoding="utf-8") as fh:
        fh.write(data)

