#made by ninekorn

#import statements start
#-------------------------------------------------------------------------------------
import socket
import tqdm
import os
import time
import sys
#https://stackoverflow.com/questions/1271320/resetting-generator-object-in-python
import more_itertools as mit
#-------------------------------------------------------------------------------------
#import statements end


#initializing some variables start
#-------------------------------------------------------------------------------------
# device's IP address
PC_HOST = "192.168.0.107"
PC_PORT = 5000
# device's IP address
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5000
# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = "<SEPARATOR>"
clientfilename = "sccsmsgPiToPc.txt"
# get the file size
clientfilesize = os.path.getsize(clientfilename)
# create the server socket
# TCP socket
#s = socket.socket()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)                           
# bind the socket to our local address
s.bind((SERVER_HOST, SERVER_PORT))
# enabling our server to accept connections
# 5 here is the number of unaccepted connections that
# the system will allow before refusing new connections
s.listen(0)
print("Listening " + str(SERVER_HOST) + " " + str(SERVER_PORT)) #f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}"
# accept connection if there is any
client_socket, address = s.accept()
# if below code is executed, that means the sender is connected
print(str(address) + " is connected" ) #f"[+] {address} is connected."
# receive the file infos
# receive using client socket, not server socket
received = client_socket.recv(BUFFER_SIZE).decode()
#filename = received
#filesize = 0          
filename, filesize = received.split(SEPARATOR)
# remove absolute path if there is
filename = os.path.basename(filename)
# convert to integer
#filesize = int(filesize)
try:
    print(filesize)
    filesize, junk = filesize.split("#")
    filesize = int(filesize)
except:
    print(filesize)
    filesize = int(filesize)
                
somecounter = 0
somecountermax = 1;
# start receiving the file from the socket
# and writing to the file stream
#f"Receiving {filename}"
progress = tqdm.tqdm(range(filesize), "Receiving " + str(filename), unit="B", unit_scale=True, unit_divisor=1024,mininterval=0,miniters=1,smoothing=1)
someswtc = 0
somefinalcounter = 0;
#-------------------------------------------------------------------------------------
#initializing some variables end





#UPDATE FUNCTION START
#-------------------------------------------------------------------------------------
#GENERATOR FOR AN UPDATE FUNCTION
def generator():  
  while True: 
    yield #x #"yield-return-generator is alive."#"frame"
    #yield
    #print("test0")
    #time.sleep(1)
#GENERATOR FOR AN UPDATE FUNCTION    
    
#ITERABLE FOR AN ITERABLE UPDATE FUNCTION     
y = mit.seekable(generator())
#ITERABLE FOR AN ITERABLE UPDATE FUNCTION

somereceivingframecounter = 0
somereceivingframecounterswtc = 0
#somereceivingframecountermax = 5


somefilesentcounter = 0
somefilesentcountermax = 10

#MAIN UPDATE
if __name__ == "__main__":
    for x in y:      
        
        #CONFIRMATION RECEIPT WAS SENT TO THE SERVER.CREATING A NEW SOCKET TO RECEIVE NEW DATA.
        if someswtc == -1:
            
            s.close()
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)                  
                            
            # bind the socket to our local address
            s.bind((SERVER_HOST, SERVER_PORT))

            # enabling our server to accept connections
            # 5 here is the number of unaccepted connections that
            # the system will allow before refusing new connections
            s.listen(0)
            print("Listening " + str(SERVER_HOST) + " " + str(SERVER_PORT)) #f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}"

            # accept connection if there is any
            client_socket, address = s.accept()
            # if below code is executed, that means the sender is connected
            print(str(address) + " is connected" ) #f"[+ {address} is connected."
            
            
            # receive the file infos
            # receive using client socket, not server socket
            received = client_socket.recv(BUFFER_SIZE).decode()
            #filename, filesize = received.split(SEPARATOR)
            #filename = received
            #filesize = 0
            
            filename, filesize = received.split(SEPARATOR)
            # remove absolute path if there is
            filename = os.path.basename(filename)
            
            try:
                print(filesize)
                filesize, junk = filesize.split("#")
                filesize = int(filesize)
            except:
                print(filesize)
                filesize = int(filesize)
                      
            # convert to integer
            #filesize = int(junk)
            
            
            
            

            somecounter = 0
            somecountermax = 1;
            # start receiving the file from the socket
            # and writing to the file stream
            #f"Receiving {filename}"
            #progress = tqdm.tqdm(range(filesize), "Receiving " + str(filename), unit="B", unit_scale=True, unit_divisor=1024,mininterval=0,miniters=1,smoothing=1)
            someswtc = 0
        #CONFIRMATION RECEIPT WAS SENT TO THE SERVER. CREATING A NEW SOCKET TO RECEIVE NEW DATA.
        
        
        
        #READING THE BUFFER UNTIL IT EMPTIES WHATS IN THE SOCKET AND WRITES IT DOWN TO THE HARD DRIVE
        if someswtc == 0:
            
            somereceivingframecounterswtc = 1
            
            with open(filename, "wb") as f:
                while True:
                    # read 1024 bytes from the socket (receive)
                    bytes_read = client_socket.recv(BUFFER_SIZE)
                    
                    if not bytes_read:
                        # nothing is received
                        # file transmitting is done
                        #break
                        if somecounter >= somecountermax:
                            somereceivingframecounterswtc = 2
                            print("download is over.")
                            someswtc = 1
                            somecounter = 0 
                      
                            break
                        somecounter+=1
                        
                    # write to the file the bytes we just received
                    f.write(bytes_read)
                    # update the progress bar
                    #progress.update(len(bytes_read))
                        
                """
                else:
                    if somecounter >= somecountermax:
                        print("download is over. program still alive")
                        #somefinalcounter+=1
                        somecounter = 0
                    somecounter+=1
                """
            # close the client socket
            #client_socket.close()
            # close the server socket
            s.close()
        #READING THE BUFFER UNTIL IT EMPTIES WHATS IN THE SOCKET AND WRITES IT DOWN TO THE HARD DRIVE
        
        #if somereceivingframecounterswtc == 1:          
        #    somereceivingframecounter +=1
        
        #if somereceivingframecounterswtc == 2:
            #print("counter " + str(somereceivingframecounter))
        
        
        
        #CREATING A NEW SOCKET THE MOMENT "someswtc == 0" FINISHES WRITING THE FILE ON DISK WITH "f.write(bytes_read)" AND IMMEDIATELY SENDING THE FRAME IN THIS SWITCH FOR ANOTHER TASK FOR BACK TO BACK GEAR/LADDER WORK.
        if someswtc == 1:      
            if somecounter >= somecountermax:
                
                print("creating socket")
                
                # create the server socket
                # TCP socket
                s = socket.socket()
                #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                #s.setblocking(1)                
                          
                
                """
                # create the client socket
                #s = socket.socket()
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                
                s.setblocking(1)
                #print(f"[+] Connecting to {host}:{port}")
                #print(f"[+] Connecting to ip/port ", (SERVER_HOST,SERVER_PORT))
                print("Connecting to ip/port ", (SERVER_HOST,SERVER_PORT))
                
                
                
                s.connect((SERVER_HOST, SERVER_PORT))
                print("[+] Connected.")

                # send the filename and filesize
                s.send(("PiToPc-received-" + str(filename)).encode()) #{filename}{SEPARATOR}{filesize}

                # start sending the file
                progress = tqdm.tqdm(range(filesize), filename, unit="B", unit_scale=True, unit_divisor=1024,mininterval=0,miniters=1,smoothing=1)

                with open(filename, "rb") as f:
                    while True:
                        # read the bytes from the file
                        bytes_read = f.read(BUFFER_SIZE)
                        if not bytes_read:
                            # file transmitting is done
                            break
                        # we use sendall to assure transimission in 
                        # busy networks
                        s.sendall(bytes_read)
                        # update the progress bar
                        progress.update(len(bytes_read))
                # close the socket
                s.close()
                
                #print(f"[+] Connecting to ip/port ", (SERVER_HOST,SERVER_PORT))
                #s.connect((SERVER_HOST, SERVER_PORT))
                #print("[+] Connected.")
                # send the filename and filesize
                #s.send("file successfully downloaded. sending confirmation to server".encode())  
                
                """
                someswtc = 2
                somecounter = 0
            somecounter+=1
        #CREATING A NEW SOCKET THE MOMENT "someswtc == 0" FINISHES WRITING THE FILE ON DISK WITH "f.write(bytes_read)" AND IMMEDIATELY SENDING THE FRAME IN THIS SWITCH FOR ANOTHER TASK FOR BACK TO BACK GEAR/LADDER WORK.

        
        
        #THE FILE WAS SENT AND A NEW SOCKET IS CREATED TO SEND A CONFIRMATION OF RECEIPT. TRYING TO CONNECT FIRST TO SERVER
        if someswtc == 2:
            print("ready to receive another file. advising server.")    
              
            if somefilesentcounter >= somefilesentcountermax:
                print("task to get 10 files is over. ") 
                someswtc = -9
            
            else:
                # bind the socket to our local addres
                #s.bind((PC_HOST, PC_PORT)) <= NOT USED HERE.
                try:           
                    print("[+] Connecting.")
                    s.connect((PC_HOST, PC_PORT))
                    print("[+] Connected.")
                    someswtc = 3 #-9 to receive only one file.
                except Exception as ex:
                    print(ex)
            
            #s.send(("PiToPc-received-" + str(filename)).encode())
            #someswtc = 0
        #THE FILE WAS SENT AND A NEW SOCKET IS CREATED TO SEND A CONFIRMATION OF RECEIPT. TRYING TO CONNECT FIRST TO SERVER      
                
        
                
                
        #SENDING CONFIRMATION RECEIPT OF FILE AND ASKING FOR NEW FILES OR NOT ENCODED.
        if someswtc == 3:
            
            try:
                #print("wait for the programmer ninekorn to insert code here.")
                print("sending confirmation receipt file to server with request for another file or not.")
                #s.send(("PiToPc-received-" + str(filename)).encode())
                #s.setblocking(1)         
                somefilename = str(somefilesentcounter) + clientfilename
                
                s.send(f"{somefilename}{SEPARATOR}{clientfilesize}".encode()) #{SEPARATOR}{clientfilesize}
                somefilesentcounter+=1
                #s.send("PiToPcReceipt".encode())
                #s.close()
                #s = socket.socket()
                #s.bind()
                #s.listen(5)
                print("sent confirmation receipt file to server with request for another file or not.")
                # start sending the file
                progress = tqdm.tqdm(range(clientfilesize), somefilename, unit="B", unit_scale=True, unit_divisor=1024,mininterval=0,miniters=1,smoothing=1)

                with open(clientfilename, "rb") as f:
                    while True:
                        # read the bytes from the file
                        bytes_read = f.read(BUFFER_SIZE)
                        if not bytes_read:
                            # file transmitting is done
                            break
                        # we use sendall to assure transimission in 
                        # busy networks
                        s.sendall(bytes_read)
                        # update the progress bar
                        progress.update(len(bytes_read))
                # close the socket
                s.close()
            except Exception as ex:
                print(ex)
            
            
            someswtc = -1
        #SENDING CONFIRMATION RECEIPT OF FILE AND ASKING FOR NEW FILES OR NOT ENCODED.
            
            
            
            
            
            
            
        time.sleep(0)

#-------------------------------------------------------------------------------------
#UPDATE FUNCTION END
        
        