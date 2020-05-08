from pyquery import PyQuery as pq

# 为方便起见，这里把HTML信息存储在demo2.html中
doc = pq(filename='demo2.html')

items = doc('.list')
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)
print("\n")
lis = items.children()
print(type(lis))
print(lis)
