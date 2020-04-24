import requests

files = {'file': open('ch3_2_7_download.ico', 'rb')}
r = requests.post("http://httpbin.org/post", files=files)
print(r.text)
