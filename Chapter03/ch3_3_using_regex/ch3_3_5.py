import re

# 非贪婪匹配
content = 'Hello 1234567 World_This ia a Regex Demo'
result = re.match(r'^He.*?(\d+).*Demo$', content)
print(result)
print(result.group(1))
