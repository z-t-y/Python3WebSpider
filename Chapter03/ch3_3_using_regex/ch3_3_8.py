import re

content = '(百度)www.baidu.com'
result = re.match(r'\(百度\)www\.baidu\.com', content)
print(result)
