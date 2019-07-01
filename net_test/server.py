# server.py 
import socket                                         
import time
from random import randint

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()                           

port = 9999                                           

# bind to the port
try:
    serversocket.bind((host, port))
except:
    print("I'm the client")
    while True:
        serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        serversocket.connect((host, port))                               
        # Receive no more than 1024 bytes
        tm = serversocket.recv(1024)
        d = tm.strip().split(",")
        print d
        button = [int(x) for x in d]
        print button


        print("The time got from the server is %s" % tm.decode('ascii'))
        time.sleep(3)
        serversocket.send('got it!')
        serversocket.close()

    
    time.sleep(1)
else:    
    # queue up to 5 requests
    serversocket.listen(5)                                           

    while True:
        # establish a connection
        try:
            clientsocket,addr = serversocket.accept()      

            print("Got a connection from %s" % str(addr))
            currentTime = time.ctime(time.time()) + "\r\n"
            clientsocket.send("{},{}".format(randint(0,2), randint(0,2)))
            b = clientsocket.recv(1024)
            print b


            clientsocket.close()
        except Exception as e:
            print(e)
            raw_input()
