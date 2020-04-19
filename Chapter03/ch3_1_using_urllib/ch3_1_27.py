from urllib.parse import quote, unquote

keyword = "壁纸"
url = 'https://www.baidu.com/s?wd=' + quote(keyword)
print(url)
print(unquote(url))
