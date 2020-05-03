from bs4 import BeautifulSoup

html = """
<html>
<body>
<p class="story">
            Once upon a time there were three little sisters; and their names \
were<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a><a \
href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
</p>
"""

soup = BeautifulSoup(html, 'lxml')
print('Next Sibling:')
print(type(soup.a.next_sibling))
print(soup.a.next_sibling)
print(soup.a.next_sibling.string)
print('Parent:')
print(type(soup.a.parents))
print(list(soup.a.parents)[0])
print(list(soup.a.parents)[0].attrs['class'])
