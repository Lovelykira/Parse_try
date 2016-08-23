from urllib.request import urlopen
from bs4 import BeautifulSoup
from lxml import etree, html


r = urlopen("https://python.org/blogs")
content = r.read()
bs = BeautifulSoup(content, "html.parser")
#print(bs.p) #first
#print(bs.a.prettify)
#print(bs.a["href"]) #attr href in first a
#aaaa = bs.find_all("a") #all
#for a in aaaa:
#    print(a['href'])

#print(bs.form.text)
#print(bs.find_all( attrs={"class":"menu"})[0])


root = etree.HTML(content)
#root = html.parse(content).getroot()
# aas = root.xpath('//a')
# for a in aas:
#     print(a.text)
#     print(a.attrib['href'])
#     print(a.xpath('text()'))

#print(root)
posts = root.xpath("//div[@class='most-recent-posts']")[0].xpath(".//ul[@class='list-recent-posts menu']/li")#[0].xpath("/li/a/text()")
for post in posts:
    print(post.xpath(".//a")[0].attrib['href'])
    print(post.xpath(".//time/text()"))
#print(posts)

