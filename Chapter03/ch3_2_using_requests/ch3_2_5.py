import requests
import re

headers = {
    'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36')
}
r = requests.get("https://www.zhihu.com/explore", headers=headers)
pattern = re.compile(r'data-za-detail-view-id="5794">(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)
