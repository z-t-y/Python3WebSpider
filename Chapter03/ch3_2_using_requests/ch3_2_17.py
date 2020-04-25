import requests
from requests.auth import HTTPBasicAuth

# 这里用flask和flask_httpauth两个库建了一个本地的网站
# 代码位于https://gist.github.com/z-t-y/fa1a09672a5d25ab56d71854e428cf55
r = requests.get('http://localhost:5000', auth=HTTPBasicAuth('username',
                                                             'password'))
print(r.status_code)
