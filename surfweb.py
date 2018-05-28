
# -*- coding: utf-8 -*-
import sys
def lecture1():

    print (ord('i'))
    print (ord('\n'))
    #new line

    # uppercase letters are lower than lowercase letters

   # in python3, all strings are unicode

    x = b'abc'
    print (type(x))

    x =  '我爱你'
    print(type(x))

def lecture2():
    import urllib.request, urllib.parse,urllib.error
    fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    for line in fhand:
        print (line.decode().strip())
#urllib: library does all the socket work and makes web page like a file

    import urllib.request, urllib.parse, urllib.error
    fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

    counts = dict()
    for line in fhand:
        words = line.decode().split()
        for word in words:
            counts[word]=counts.get(word,0)+1
    print (counts)


    # also request html file
    import urllib.request, urllib.parse, urllib.error
    fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
    for line in fhand:
        print (line.decode().strip())

def bs4():

    import urllib.request,urllib.parse, urllib.error
    from bs4 import BeautifulSoup

    url = input('Enter-')
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    #retrive all the anchor tags
    tags = soup('a')
    for tag in tags:
        print (tag.get('href',None))


def assignment1():

    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import ssl

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter - ')
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        # Look at the parts of a tag
        print('TAG:', tag)
        print('URL:', tag.get('href', None))
        print('Contents:', tag.contents[0])
        print('Attrs:', tag.attrs)


def assignment2():

    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import ssl

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter-')
    html = urlopen(url,context =ctx).read()
    soup = BeautifulSoup(html,'html.parser')

    tags = soup('span')
    l =list()
    for tag in tags:
        num = tag.contents[0]
        n = float(num)
        l.append(n)
    print(sum(l))

def assignment3():

    import urllib.request, urllib.parse, urllib.error
    from bs4 import BeautifulSoup
    import ssl

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE







    url = input('Enter -')
    count = int(input('Enter count'))
    position = int(input('Enter position'))


    names =list()

    #for i in range(count):

    while count > 0:


        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')



    # Retrieve all of the anchor tags
        tags = soup('a')


        url = tags[position-1].get('href', None)


        name = tags[position-1].string
        names.append(name)
        count = count-1
    print(names)







if __name__=='__main__':
    print(sys.version)
    assignment3()

