from pyquery import PyQuery as pq

doc = pq(filename='demo3.html')
a = doc('a')
print(a, type(a))
print(a.attr('href'))
print(a.attr.href)
print("\n")
for item in a.items():
    print(item.attr('href'))
