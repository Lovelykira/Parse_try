from urllib.request import urlopen
from pyquery import PyQuery as pq


r = urlopen("https://python.org/blogs")
content = r.read()

d = pq(content)
#print(d("div"))
#print(d(".list-recent-posts"))
#print(d("#id"))
#print(d("[disabled]"))

#print(d("div:first"))

#артибуты: .text .attr

a = d(".most-recent-posts a")
[print(el.attrib['href']) for el in a]
# for el in a:
#     print(el.attrib['href'])
time = d(".most-recent-posts time")
for t in time:
    print(t.text)
# posts = root.xpath("//div[@class='most-recent-posts']")[0].xpath(".//ul[@class='list-recent-posts menu']/li")#[0].xpath("/li/a/text()")
# for post in posts:
#     print(post.xpath(".//a")[0].attrib['href'])
#     print(post.xpath(".//time/text()"))
