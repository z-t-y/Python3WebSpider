from urllib.robotparser import RobotFileParser
from urllib.request import urlopen

rp = RobotFileParser()
url = 'https://gist.githubusercontent.com/z-t-y/661ed36307b6e3c6c86e1d878f300761/raw/ee796389b03cf5c0f325052a8ba036764a6b6c5c/jianshu_robots.txt'
rp.parse(urlopen(url).read().decode('utf-8').split('\n'))
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', 'http://www.jianshu.com/search?q=python&page=1&type=collections'))
