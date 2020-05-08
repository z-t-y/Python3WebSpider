from pyquery import PyQuery as pq

doc = pq(filename='demo3.html')
a = doc('.item-0.active a')
print(a)
print(a.text())
print()
li = doc('.item-0.active')
print(li)
print(li.html())
