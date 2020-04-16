import http.cookiejar
import urllib.request

filename = "ch3_1_11.txt"
cookie = http.cookiejar.MozillaCookieJar(filename) # 保存为Mozzila格式
# cookie = http.cookiejar.LWPCookie(filename) # 保存为LWP格式
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
cookie.save(ignore_discard=True, ignore_expires=True)
