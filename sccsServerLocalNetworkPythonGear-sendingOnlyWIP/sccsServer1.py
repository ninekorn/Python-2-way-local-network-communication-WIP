import socket
import tqdm
import os

#https://www.thepythoncode.com/article/send-receive-files-using-sockets-python
#From the Python Code: I've initialized some parameters we gonna use, notice that I've used "0.0.0.0" as the server IP address, this means all IPv4 addresses on the local machine. You may wonder, why we don't just use our local IP address or "localhost" or "127.0.0.1" ? Well, if the server has two IP addresses, let's say "192.168.1.101" on a network, and "10.0.1.1" on another, and the server listens on "0.0.0.0", it will be reachable at both of those IPs.
# device's IP address
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5000
# receive 4096 bytes each time
BUFFER_SIZE = 4096
SEPARATOR = '<SEPARATOR>'

# create the server socket
# TCP socket
s = socket.socket()

# bind the socket to our local address
s.bind((SERVER_HOST, SERVER_PORT))

# enabling our server to accept connections
# 5 here is the number of unaccepted connections that
# the system will allow before refusing new connections
s.listen(5)
#print('[*] Listening as, ' + string(SERVER_HOST) + "," + stringString(SERVER_PORT))
#print("[*] Listening as {{SERVER_HOST}}:{{SERVER_PORT}}")
print("[*] Listening ip/port",(SERVER_HOST,SERVER_PORT))
#print("[*] Listening port",SERVER_PORT)

# accept connection if there is any
client_socket, address = s.accept() 
# if below code is executed, that means the sender is connected
print('[+]connected.',address)

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
progress = tqdm.tqdm(range(filesize), filename, unit='B', unit_scale=True, unit_divisor=1024)
with open(filename, 'wb') as f:
    while True:
        # read 1024 bytes from the socket (receive)
        bytes_read = client_socket.recv(BUFFER_SIZE)
        if not bytes_read:    
            # nothing is received
            # file transmitting is done
            break
        # write to the file the bytes we just received
        f.write(bytes_read)
        # update the progress bar
        progress.update(len(bytes_read))

# close the client socket
client_socket.close()
# close the server socket
s.close()










