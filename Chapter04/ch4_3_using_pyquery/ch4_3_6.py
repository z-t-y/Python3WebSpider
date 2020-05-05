from pyquery import PyQuery as pq

# 为方便起见，这里把HTML信息存储在demo3.html中
doc = pq(filename='demo3.html')

items = doc('.list')
container = items.parent()
print(type(container))
print(container)
