import re

content = '''Hello 1234567 World_This
is a Regex Demo
'''
# S模式作用是使.匹配包括换行符在内的所有字符
result = re.match(r'^He.*?(\d+).*?Demo$', content, re.S)
print(result.group(1))
