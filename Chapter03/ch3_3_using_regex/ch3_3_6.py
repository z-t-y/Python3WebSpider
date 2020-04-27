import re

# 贪婪匹配与非贪婪匹配的比较
content = 'http://weibo.com/comment/kEraCN'
result1 = re.match(r'http.*?comment/(.*?)', content)
result2 = re.match(r'http.*?comment/(.*)', content)
print('result1', result1.group(1))
print('result2', result2.group(1))
