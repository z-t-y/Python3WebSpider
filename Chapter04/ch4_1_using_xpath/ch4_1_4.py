from lxml import etree

html = etree.parse(
    open(r'E:\Python\py3_web_spider\Chapter04\ch4_1_using_xpath\test.html'),
    etree.HTMLParser()
)
# 获取子节点
result = html.xpath('//li/a')
print(result)
