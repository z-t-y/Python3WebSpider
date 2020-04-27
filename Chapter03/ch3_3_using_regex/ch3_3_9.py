import re

# search扫描整个字符串，并返回第一个结果

content = 'Extra stings Hello 1234567 World_This is a Regex Demo'
result = re.search(r'Hello.*?(\d+).*?Demo', content)
print(result)
print(result.group(1))
