import socket
import tqdm
import os

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096 # send 4096 bytes each time step

# the ip address or hostname of the server, the receiver #"192.168.1.101"
host = "192.168.0.121" #192.168.0.107
# the port, let's use 5001
port = 5000 
# the name of file we want to send, make sure it exists
filename = "sccsmsgUToK.txt"
# get the file size
filesize = os.path.getsize(filename)

# create the client socket
s = socket.socket()

#print(f"[+] Connecting to {host}:{port}")
print(f"[+] Connecting to ip/port ", (host,port))

s.connect((host, port))
print("[+] Connected.")

# send the filename and filesize
s.send(f"{filename}{SEPARATOR}{filesize}".encode())

# start sending the file
progress = tqdm.tqdm(range(filesize), filename, unit="B", unit_scale=True, unit_divisor=1024)

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




