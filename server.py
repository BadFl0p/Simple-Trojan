#!/usr/bin/python3
from os import popen
import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # creates a socket instance which is going to use IPv4 and
                                                             # a connection-oriented protocol (TCP)
    host = socket.gethostname() # getting the host name
    port = 12345
    print(f"IP is {socket.gethostbyname(host)}")

    sock.bind((host, port)) # binds the socket to the IP related to host and port specified to listen to incoming requests
    sock.listen(2) # listen for incoming connection (maximum 2)
    
    while True:
        clientSocket, addr = sock.accept() # allows the client to connect to the server
        print(f"Received connection from {addr}")
        
        msg = clientSocket.recv(4096)
        # popen(msg.decode())

        clientSocket.close()

        break
    sock.close()
    return 0


if __name__ == '__main__':
    main()
