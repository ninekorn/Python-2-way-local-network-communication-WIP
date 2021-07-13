import socket
import tqdm
import os
import time

# device's IP address
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5000
# receive 4096 bytes each timenigh
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

# create the server socket
# TCP socket
s = socket.socket()
#s.setblocking(1)

# bind the socket to our local address
s.bind((SERVER_HOST, SERVER_PORT))

# enabling our server to accept connections
# 5 here is the number of unaccepted connections that
# the system will allow before refusing new connections
s.listen(5)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

# accept connection if there is any
client_socket, address = s.accept() 
# if below code is executed, that means the sender is connected
print(f"[+] {address} is connected.")

# receive the file infos
# receive using client socket, not server socket
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(SEPARATOR)

# remove absolute path if there is
filename = os.path.basename(filename)
# convert to integer
filesize = int(filesize)

# start receiving the file from the socket
# and writing to the file stream
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024,mininterval=0 ,miniters=1,smoothing = 1, position=0) #,mininterval=0 ,miniters=1,smoothing = 1  #leave=True #total=total<=undefined 

somecounter = 0
somecountermax = 100

somecountersleeping = 0
somecountersleepingmax = 1000

#f = open(filename, f"wb") 

bytesreadswtc = 0

#with open(filename, f"wb") as f:

#https://stackoverflow.com/questions/45808140/using-tqdm-progress-bar-in-a-while-loop
def generator():
    while True:
        yield
    
def foo_():
    time.sleep(0.3)

while True:        
            # read 1024 bytes from the socket (receive)

    if bytesreadswtc == 0:
        with client_socket as soc:          
            bytes_read = soc.recv(BUFFER_SIZE) 
            if not bytes_read:
                if somecounter >= somecountermax:
                    bytesreadswtc = 1
                    #f.close()
                    # close the client socket
                    soc.close()
                    # close the server socket
                    s.close()
                    # nothing is received
                    # file transmitting is done
                    #break
                    
                    bytes_read = [] 
        
                    somecounter = 0
                somecounter+=1
            else:
                # write to the file the bytes we just received
                #f.write(bytes_read)
                # update the progress bar
                for _ in tqdm.tqdm(generator()):
                    progress.update(len(bytes_read))
                           
                #range_ = range(0, 10)
                #total = len(bytes_read)
                
                #with tqdm.tqdm(total=total, position=0, leave=True) as pbar:
                #   for i in tqdm.tqdm((foo_, range_ ), position=0,leave=True):
                #    pbar.update()
    else:
        
               
        if somecountersleeping >= somecountersleepingmax:
            
            s = socket.socket()
            
            # bind the socket to our local address
            s.bind((SERVER_HOST, SERVER_PORT))

            # enabling our server to accept connections
            # 5 here is the number of unaccepted connections that
            # the system will allow before refusing new connections
            s.listen(5)
            print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

            # accept connection if there is any
            client_socket, address = s.accept()          
            bytes_read = [] 
            #bytes_read = client_socket.reutokcv(BUFFER_SIZE)
            
            #if not bytes_read:
            #    client_socket.close()
            #    s.close()
            #    bytesreadswtc = 1
            #else:
            #    bytesreadswtc = 0 
            bytesreadswtc = 1
            somecountersleeping = 0
        somecountersleeping+=1
                
                
                
                
    time.sleep(0)
  
  
  
#while True:
# close the client socket
#client_socket.close()
# close the server socket
#s.close()  

