import urllib.parse
import urllib.request
import pprint

data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding="utf-8")
response = urllib.request.urlopen('http://httpbin.org/post', data=data)
print(response.read())
