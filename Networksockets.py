# Transport control protocol (TCP)
# TCP connection : Sockets
# TCP Ports: HTTP(80) --> web server



#application protocol: HTTP - Hypertext Transfer Protocol
# HTTP: is the set of rules to allow browsers to retrieve web docs from servers over the internet
#for the web to retrieve HTML, Images, docs...etc.
# make a connection - request a document - retrieve the doc - close the connection
# each time we click on a tag, the browser connect to the web server and issues a 'get' request to GET the content of the
# page at the specific url(uniform resouce locator). The server then returns the HTML doc to the browser which formats and displays the docs

# browser is a piece of software running on computer
#after the click, the browser determines which web server to connect to, which port to connect on the web server, and
# what doc to retrieve. the browser then make a socket to send the GET request
# the web server then parse the request, run program, and produce a response on the same socket in the format of html
# then the browser reads the html
# making a HTTP request: GET http://www.psu.edu/university-park/ HTTP/1.0
# telnet is a pre-stall software that can send info to any server/any port on any server in a insecure manner

# $ telnet www.psu.edu 80
# GET http://www.psu.edu/university-park/ HTTP/1.0
# the above 2 lines will convince the web server to send a page back: 1. Metadata about the file I am getting including
# the type of the file: text/html   2. then the content of the file
# then the connection will close
# this is how people HACK a computer




# an HTTP Request in Python:


def lecture2():

    import socket

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'. encode()
    mysock.send(cmd)


    while True:
        data = mysock.recv(512)
        if (len(data) < 1):
            break
        print (data.decode())
    mysock.close()



def assignment1():

    import socket

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'. encode() #default as UTF8 : from unicode to byte
    mysock.send(cmd)


    while True:
        data = mysock.recv(20)
        if (len(data)<1):
            break
        print (data.decode())

        #data is byte, after decoding, it becomes unicode


    mysock.close()





if __name__=='__main__':
    lecture2()

