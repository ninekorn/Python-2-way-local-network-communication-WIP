import time
import math
import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 5000

# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
serversocket.bind((UDP_IP, UDP_PORT))
# become a server socket
serversocket.listen() #5

#conn, addr = serversocket.accept()

someswtc = 0

#while someswtc ==0:
#    data = conn.recv(1024)
    #if not data:
    #    break
    #print('Received', repr(data))
    #conn.sendall(data)
 #   conn.sendall(b'Hello, from, server')
 #   print('Received', repr(data))
  #  time.sleep(1)
    
    
#while True:
    # accept connections from outside
 #   (clientsocket, address) = serversocket.accept()
    # now do something with the clientsocket
    # in this case, we'll pretend this is a threaded server
  #  ct = client_thread(clientsocket)
   # ct.run()
    #print('test')
    #time.sleep(1)




def __init__ (self):
    threading.Thread.__init__ (self)

def run(self):
    global data_queue
    mysock.listen(5)
    print("waiting for data")
    while True:
        sleep(0.1)
        conn, addr = mysock.accept()
        print("received connection from client")
        self.talk_to_client(conn)

def talk_to_client(self, conn):
    data = conn.recv(1000)
    while data != 'quit':
        reply = prepare_reply_to_client(data)
        data_queue.put(reply)
    conn.close()     # if we're done with this connection






# create an INET, STREAMing socket
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
#s.connect(("www.python.org", 80))s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)