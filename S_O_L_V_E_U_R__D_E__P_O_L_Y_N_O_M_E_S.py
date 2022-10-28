import socket
import base64

def client_program():
    host = 'challenge01.root-me.org'
    port = 52018
    client_socket = socket.socket()
    client_socket.connect((host, port))
    i = 0

    while (i < 10):
        
        
        data = ""
        data = client_socket.recv(1024).decode()
        print(data) 
        # print(rep)
        # rep = rep + '\n'
        # client_socket.send(rep.encode())

if __name__ == '__main__':
    client_program()