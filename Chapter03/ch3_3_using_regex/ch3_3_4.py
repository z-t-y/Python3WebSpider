import re

# 贪婪匹配
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match(r'^He.*(\d+).*Demo$', content)
print(result)
print(result.group(1))
