from lxml import etree

html = etree.parse(
    open(r'E:\Python\py3_web_spider\Chapter04\ch4_1_using_xpath\test.html'),
    etree.HTMLParser()
)
result = html.xpath('//a[@href="link4.html"]/../@class')
# 也可以这样写：
# result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)
