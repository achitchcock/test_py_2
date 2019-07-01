# client.py  
import socket, time
while True:
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    # get local machine name
    host = socket.gethostname()                           

    port = 9999

    # connection to hostname on the port.
    s.connect((host, port))                               

    # Receive no more than 1024 bytes
    tm = s.recv(1024)
    print("The time got from the server is %s" % tm.decode('ascii'))
    time.sleep(3)
    s.send('got it!')
    s.close()

    
    time.sleep(1)
raw_input()
