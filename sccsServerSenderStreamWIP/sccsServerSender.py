import socket
import tqdm
import os
import time
import sys
#from tqdm import tqdm
#from time import sleep
#from tqdm import tqdm

SEPARATOR = "<SEPARATOR>" 
BUFFER_SIZE = 4096 # send 4096 bytes each time step

# the ip address or hostname of the server, the receiver##
host = "192.168.0.121"
# the port, let's use 5001
port = 5000
# the name of file we want to send, make sure it exists
filename = "sccsmsgPcToPi.txt"
# get the file size
filesize = os.path.getsize(filename)

# create the client socket
#s = socket.socket()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

"""
print("[+] Connecting to {host}:{port}")
s.connect((host, port))
print("[+] Connected.")

a_string =  '{} {} {} '
formatted_string = a_string.format(filename, SEPARATOR,filesize)
# send the filename and filesize
s.send(formatted_string.encode())

# start sending the file
progress = tqdm.tqdm(range(filesize), "Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024,mininterval=0,miniters=1,smoothing=1)
"""


somecounter = 0
somecountermax = 5

def generator():
  while True:
    yield

#with client_socket as cs:google.ca
    
#for _ in tqdm(generator()):

#with open(<your data>, mode='r', encoding='utf-8') as f:
#with s as soc:   
#for _ in tqdm(generator()):

somefiledownloadedcounter = 0
somefiledownloadedcountermax = 5
somefiledownloadedcounterswtc = 1

someprintcounter = 0
someprintcountermax = 5

someconnectswtc = 0

#while True:
for _ in tqdm.tqdm(generator()):    
    if somefiledownloadedcounterswtc == 0:
        
        #with s as soc:
        with open(filename, "rb") as f:
            while  somefiledownloadedcounterswtc== 0:
                # read the bytes from the file
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    # file transmitting is done
                    somefiledownloadedcounterswtc = 1
                    print("file uploaded to rasppi.")                  
                    break
                # we use sendall to assure transimission in 
                # busy networks
                s.sendall(bytes_read)
                # update the progress bar
                progress.update(len(bytes_read))
                time.sleep(0)
                print("uploading to rasppi.")   
        # close the socket
        s.close()
    else:
        
        if somefiledownloadedcounter >= somefiledownloadedcountermax:
            
           
            # create the client socket
            
            #s = socket.socket()
            #print("[+] Connecting to {host}:{port}")
            someconnectswtc = 0
            try:
                print("[+] Creating socket.")
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                print("[+] Connecting to {host}:{port}")
                s.connect((host, port))
                print("[+] Connected.")

                a_string =  '{} {} {} '
                formatted_string = a_string.format(filename, SEPARATOR,filesize)
                # send the filename and filesize
                s.send(formatted_string.encode())

                # start sending the file
                progress = tqdm.tqdm(range(filesize), "Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024,mininterval=0,miniters=1,smoothing=1)

                
                
                #s.send(formatted_string.encode())
                someconnectswtc = 1
            except:
                #s = socket.socket()
                
                
                print("[+] cannot connect to client RaspPi")
                time.sleep(1)
                #print("[+] Connected.")
                #s.createconnection((host, port))
                #a_string =  '{} {} {} '
                #formatted_string = a_string.format(filename, SEPARATOR,filesize)
                # send the filename and filesize
                #s.send(formatted_string.encode())
                someconnectswtc = 0
                
            if someconnectswtc == 1:
                try:
                    print("[+] Connecting to {host}:{port}")
                    s.connect((host, port))
                    print("[+] Connected.")
                    someconnectswtc = 1
                except:
                    someconnectswtc = 0
            
            
            if someconnectswtc == 1:
                #s.setblocking(1)
                #client_socket,address = s.accept()
                
                #print("accepted connection from rasppi.")
                #a_string =  '{} {} {} '
                #formatted_string = a_string.format(filename, SEPARATOR,filesize)
                # send the filename and filesize
                #s.send(formatted_string.encode())
                # start sending the file
                #progress = tqdm.tqdm(range(filesize), "Sending {filename}", unit="B", unit_scale=True, unit_divisor=1024,mininterval=0,miniters=1,smoothing=1)
                somefiledownloadedcounterswtc = 0
                
                
            somefiledownloadedcounter = 0;
        somefiledownloadedcounter+=1
        time.sleep(0)
        
    if someprintcounter >= someprintcountermax:
        print("server program is still alive.")
        someprintcounter =0
    someprintcounter+=1
    
    
    time.sleep(0)


"""
with open(filename, "rb") as f:
    #while True:       
    with s as soc:
        for _ in tqdm.tqdm(generator()):
            
            #if somefiledownloadedcounterswtc == 0:
         
            #do your stuff here
            # read the bytes from the file
            bytes_read = f.read(BUFFER_SIZE)
            if not bytes_read:
                if somecounter >= somecountermax:
                    # file transmitting is done
                    # close the socket
                    f.close()
                    #soc.close()
                    bytes_read = []
                    #break
                    somefiledownloadedcounterswtc = 1
                    #time.sleep(0)
                    somecounter = 0
                somecounter+=1
            else:
                # we use sendall to assure transimission in 
                # busy networks
                soc.sendall(bytes_read)
                # update the progress bar
                
                #progress.update(len(bytes_read))
                print(len(bytes_read))
                #for i in tqdm.tqdm(bytes_read):
                #    time.sleep(10)
            
            else:
                if somefiledownloadedcounter >= somefiledownloadedcountermax:
                    somefiledownloadedcounterswtc = 1
                    somefiledownloadedcounter = 0
                somefiledownloadedcounter+=1
            
        time.sleep(0)

#while True:
"""
        






