from pyquery import PyQuery as pq

doc = pq(filename='demo.htm')
print(doc('li'))
