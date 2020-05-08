from pyquery import PyQuery as pq

doc = pq(filename='demo3.html')

li = doc('.list .item-0.active')
print(li.siblings())
print(li.siblings('.active'))
