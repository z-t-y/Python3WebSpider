from urllib.parse import urlparse

result = urlparse('http://www.baidu.com/index.html;user?id=5#comment',
                  allow_fragments=False)
print(result.scheme, result[0], result.netloc, result[1], sep='\n')
