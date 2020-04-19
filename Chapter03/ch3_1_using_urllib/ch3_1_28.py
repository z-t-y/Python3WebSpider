from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
# 访问不了简书的robots.txt因此自己copy了一份放在Github Gist里面
rp.set_url('https://gist.githubusercontent.com/z-t-y/661ed36307b6e3c6c86e1d878f300761/raw/ee796389b03cf5c0f325052a8ba036764a6b6c5c/jianshu_robots.txt')
rp.read()
print(rp.can_fetch('*', 'http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*', 'http://www.jianshu.com/search?q=python&page=1&type=collections'))
