import requests

r = requests.get("https://github.com/favicon.ico")

with open('ch3_2_7_download.ico', 'wb') as f:
    f.write(r.content)
