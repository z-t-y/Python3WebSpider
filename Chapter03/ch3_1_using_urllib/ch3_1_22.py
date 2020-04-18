from urllib.parse import urlunsplit

# urlunsplit长度必须为5
data = ['http', 'www.baidu.com', 'index.html', 'a=6', 'comment']
print(urlunsplit(data))
