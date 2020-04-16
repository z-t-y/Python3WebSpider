from urllib import request, parse

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozzilla/4.0 (compatible;  MSIE5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'Germany'
}
data = bytes(parse.urlencode(dict), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
