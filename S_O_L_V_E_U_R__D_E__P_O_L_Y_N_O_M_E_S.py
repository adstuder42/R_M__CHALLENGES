import socket
import base64

def atoi(str):
    num = ""
    for char in str:
        if char == "-" or char == "+":
            num = num + char
        elif char.isnumeric() == True:
            num = num + char
        else:
            return (int(num))


def client_program():
    host = 'challenge01.root-me.org'
    port = 52018
    client_socket = socket.socket()
    client_socket.connect((host, port))
    i = 0

    while (i < 10):
        data = ""
        data = client_socket.recv(1024).decode()
        data = data[data.find("please:") + 8:]
        print(data)
        data = data.split(' ')
        for i in data:
            print(i)
        val1 = atoi(data[0])
        val2 = atoi(data[2])
        val3 = atoi(data[4])
        val4 = atoi(data[6])
        op1 = data[1]
        op1 = data[3]

        if val4 > 0:
            val3 -= val4
        else:
            val3 += val4

        delta = (val2 * val2) + 4 * val1 * val3
        if
        # val1 = atoi(data)
        # while data[i] == "+" or data[i]
        # val2
        # print(data) 
        # print(atoi(data)) 
        
        # print(rep)
        # rep = rep + '\n'
        # client_socket.send(rep.encode())

if __name__ == '__main__':
    client_program()