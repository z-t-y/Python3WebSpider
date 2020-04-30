from lxml import etree

# 我在这里对源码进行了一些修改，请将下文中的E:\Path_to_my_html_file改为你自己的绝对路径
html = etree.parse(
    open(r'E:\Python\py3_web_spider\Chapter04\ch4_1_using_xpath\test.html'),
    etree.HTMLParser()
)
result = etree.tostring(html)
print(result.decode('utf-8'))
