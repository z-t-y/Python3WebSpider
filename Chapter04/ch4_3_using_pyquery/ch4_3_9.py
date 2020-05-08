from pyquery import PyQuery as pq

doc = pq(filename='demo3.html')
li = doc('.item-0.active')
print(li)
print(str(li))

lis = doc('li').items()
print(type(lis))
for li in lis:
    print(li, type(li))
