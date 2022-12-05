from bs4 import BeautifulSoup

html_doc = """<html><head><title>
The Dormouse's story

The Dormouse's story



Once upon a time there were three little sisters; and their names were


Elsie,
Lacie and
Tillie;
and they lived at the bottom of a well.

...
</p>"""

soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup)
print(soup.prettify())
print(soup.title)
print(soup.title.text)
print(soup.find_all('p'))




# print(soup.prettify())
# soup = BeautifulSoup(html_doc, 'html.parser')


# print(soup.title)
# print(soup.title.text)
# print(soup.find_all("p"))
# print([i.text for i in soup.find_all("p")])

# print(soup.p['class'])
# print(soup.find_all("a"))

# for link in soup.find_all('a'):
#     print(link.get('href'))