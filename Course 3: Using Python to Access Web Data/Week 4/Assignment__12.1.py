import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1305291.html'
html = urllib.request.urlopen(url, context=ctx).read()
# Read html and clean it up
mySoup = BeautifulSoup(html, 'html.parser')

sum = 0

# Returns a list
tags = mySoup('span')
for tag in tags:
    #print('Tag: ', tag)
    #print(tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
    try:
        sum += int(tag.contents[0])
    except:
        continue
print(sum)

# Answer by:
# kunal5042
# Email    : kunalwadhwa.cs@gmail.com
# Alternate: kunalwadhwa900@gmail.com