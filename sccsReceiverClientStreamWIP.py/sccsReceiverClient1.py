import socket
import tqdm
import os
import time
# device's IP address
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5000
# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

# create the server socket
# TCP socket
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
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

somecounter = 0
somecountermax = 5;
# start receiving the file from the socket
# and writing to the file stream
progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)

someswtc = 0
somefinalcounter = 0
someinitswtc = 0


def generator():
  while True:
    yield
    
someconnectswtc = 0    
    
somereconnectcounter = 0
somereconnectcountermax = 5

dbugprint = 1

#while True:
for _ in tqdm.tqdm(generator()):
    if someswtc == 0:
        
        if someinitswtc ==0:      
            
            """
            # create the server socket
            # TCP socket
            s = socket.socket()
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # bind the socket to our local address
            s.bind((SERVER_HOST, SERVER_PORT))

            # enabling our server to accept connections
            # 5 here is the number of unaccepted connections that
            # the system will allow before refusing new connections
            s.listen(0)
            print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
            s.setblocking(1)
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
            """
            #if dbugprint == 1:
                #print("[+] trying to reconnect to server pc ubuntu.")
            
            someconnectswtc = 0
            
            try:
                # recreate the socket and reconnect
                #someinitswtc = 1
                #someswtc = 0
                
                if dbugprint == 1:
                    print("[+] Creating new socket.")
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if dbugprint == 1:
                    print("[+] Created new socket.")
                
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)              
                s.bind((SERVER_HOST, SERVER_PORT))
                s.listen(0)
                if dbugprint == 1:
                    print("[+] Socket options set.")
                #s.setblocking(1)
                #s.connect((SERVER_HOST, SERVER_PORT))
                #s.send("some more data")print(f"[+] Connecting to ip/port ", (SERVER_HOST,SERVER_PORT))
                """
                try:
                    print("[+] Trying to connect to pc ubuntu.")
                    s.send("xornotsha256keywip") #somesenderkeythatasksifpcisreadytosendtopi
                    print("[+] Message sent so a connection is possible.")
                    someconnectswtc = 1
                except:
                    print("[+] Exception. Connection is ! currently possible.")
                    someconnectswtc = 0
                    someinitswtc = 0
                    someswtc = 0
                """  
                #s.send("xornotsha256keywip") #somesenderkeythatasksifpcisreadytosendtopi
                someinitswtc = 1
                someconnectswtc = 1
                
            except:
                print("[+] Exception during creation of the socket.")
                someconnectswtc = 0
                
                
            """
            try:
                print("[+] Connecting to server host.")
                s.connect((SERVER_HOST, SERVER_PORT))
                
                someconnectswtc = 1
            except:
                print("[+] Failed to connect to server host.")
                someconnectswtc = 0        
            """
            
            if someconnectswtc == 1:           
                #s.connect((SERVER_HOST, SERVER_PORT))
                
                try:
                    client_socket, address = s.accept()
                    if dbugprint == 1:
                        print("[+] Connected.")
                    someinitswtc = 1
                except:
                    if dbugprint == 1:
                        print("[+] Failed Connection.")
                    someinitswtc = 0
                #somecounter = 0
                #somecountermax = 1000;
                # start receiving the file from the socket
                # and writing to the file stream
                #progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
                #someconnectswtc = 1
                

            
                


            #someswtc = 0
            #somefinalcounter = 0;
            
            
        else:
            if someconnectswtc == 1:
                with client_socket as soc:             
                    with open(filename, "wb") as f:
                        print("receiving new file.")
                        while True:
                            # read 1024 bytes from the socket (receive)
                            bytes_read = soc.recv(BUFFER_SIZE)
                            
                            if not bytes_read:
                                # nothing is received
                                # file transmitting is done
                                #break
                                if somecounter >= somecountermax:
                                    if dbugprint == 1:
                                        print("download is over.")
                                    someswtc = 1
                                    somecounter = 0 
                                    someinitswtc = 0
                                    break
                                somecounter+=1
                                
                            # write to the file the bytes we just received
                            f.write(bytes_read)
                            # update the progress bar
                            progress.update(len(bytes_read))
                    # close the client socket
                    
                #simulate a closed socket or simply closing the socket after each complete download
                soc.close()
                #close the server socket
                s.close()
    else:
        if somecounter >= somecountermax:
          
            if dbugprint == 1:
                print("download is over. program still alive")
            someswtc = 0
            #somefinalcounter+=1
            somecounter = 0
            someinitswtc = 0
        somecounter+=1
        
    if somereconnectcounter >= somereconnectcountermax:
        
        if dbugprint == 1:
            print("program still alive")       
        someswtc = 0
        #somefinalcounter+=1
        somecounter = 0
        #someinitswtc = 0
        somereconnectcounter = 0
    somereconnectcounter += 1
    time.sleep(0)
    

