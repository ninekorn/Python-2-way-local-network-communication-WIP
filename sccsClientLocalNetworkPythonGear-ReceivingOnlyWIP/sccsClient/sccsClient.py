#https://realpython.com/python-sockets/
#!/usr/bin/env python3

import socket
import sys
#import time
UDP_IP = "127.0.0.1" # set it to destination IP.. RPi in this case #127.0.0.1 #45.58.99.25
UDP_PORT = 5000
#print("UDP target IP:", UDP_IP)
#print("UDP target port:", UDP_PORT)
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#sock.bind((UDP_IP, UDP_PORT))
#print >>sys.stderr, 'starting up on %s port %s' % sock.getsockname()
#sock.listen(1)

#HOST = '127.0.0.1'  # The server's hostname or IP address
#PORT = 5000        # The port used by the server #65432

someswtc = True;
somecounter = 0;
somecountermax =10;
somecounterinit = 0;
somecounterinitmax = 100;
somecounterinitswtc = 0;

while someswtc == True:
    
    if somecounterinitswtc == 0:
        if somecounterinit >= somecounterinitmax:
            somecounterinitswtc = 1
            somecounterinit = 0
        somecounterinit+=1
    else:
        
        if somecounter >= somecountermax:
            with sock as s:
                s.connect((UDP_IP, UDP_PORT))
                s.sendall(b'Hello, world')
                
                data = s.recv(1024)
                #message = bytearray([0,1,2,3,4,5,6,7,8,9])
                #s.sendto(message, ('127.0.0.1',5000))
        
            #print('Received', repr(data))
            somecounter = 0;
        somecounter+=1
        
        
    
    
    
