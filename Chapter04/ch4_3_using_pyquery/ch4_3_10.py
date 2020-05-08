from pyquery import PyQuery as pq

doc = pq(filename='demo3.html')
a = doc('.item-0.active a')
print(a, type(a))
print(a.attr('href'))
# 也可以写为print(a.attr.href)
