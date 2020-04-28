from lxml import etree

html = etree.parse(
    open(r'E:\Python\py3_web_spider\Chapter04\ch4_1_using_xpath\test.html'),
    etree.HTMLParser()
)
result = html.xpath('//li/a/@href')
print(result)
