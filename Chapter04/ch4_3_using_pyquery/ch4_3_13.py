from pyquery import PyQuery as pq

doc = pq(filename='demo4.html')
li = doc('li')
print(li.html())
print(li.text())
print(type(li.text()))
