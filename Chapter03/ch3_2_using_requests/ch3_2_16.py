import requests

# 使用的是免费西刺代理，可能会失效
proxies = {
    'http': 'http://114.223.103.47:8118',
    'https': 'https://223.68.190.130:8181'
}
r = requests.get('https://www.taobao.com', proxies=proxies)
print(r.status_code)
