import socket
import tqdm
import os
import time
import math

# device's IP address
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5000
# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"

# create the server socket
# TCP socket
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
somecountermax = 1000;
somecountermaxtwo = 10000;
# start receiving the file from the socket
# and writing to the file stream

someswtc = 0

while True:
    
    
    if someswtc ==0:     
        progress = tqdm.tqdm(range(filesize), f"Receiving {filename}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(filename, "wb") as f:
            while True:
                # read 1024 bytes from the socket (receive)
                bytes_read = client_socket.recv(BUFFER_SIZE)
                
                if not bytes_read:
                    # nothing is received
                    # file transmitting is done
                    #break
                    if somecounter >= somecountermax:
                        print("download is over.")
                        someswtc = 1
                        somecounter = 0
                        break
                    somecounter+=1
                else:
                    # write to the file the bytes we just received
                    f.write(bytes_read)
                    # update the progress bar
                    progress.update(len(bytes_read))
                
        # close the client socket
        client_socket.close()
        # close the server socket
        s.close()
    else if someswtc == 1:
        
        if somecounter >= somecountermaxtwo:
            print("download is over. program is still alive")
            someswtc = 1
            somecounter = 0
            time.sleep(5)
            #break
        somecounter+=1
    time.sleep(0)