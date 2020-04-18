from urllib.parse import urlunparse

# urlunparse长度必须为6
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=6', 'comment']
print(urlunparse(data))
