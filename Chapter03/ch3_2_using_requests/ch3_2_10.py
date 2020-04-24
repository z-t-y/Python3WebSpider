import requests

headers = {
    'User-Agent': ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
"AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36")
}
r = requests.get('http://jianshu.com', headers=headers)
(exit() if not r.status_code == requests.codes.ok
        else print('Request Successfully'))
