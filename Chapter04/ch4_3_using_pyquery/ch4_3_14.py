from pyquery import PyQuery as pq
doc = pq(filename='demo3.html')
li = doc('.item-0.active')
print(li)
li.removeClass('active')
print(li)
li.addClass('active')
print(li)
