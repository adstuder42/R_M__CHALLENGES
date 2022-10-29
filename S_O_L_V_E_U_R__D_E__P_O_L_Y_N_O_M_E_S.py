import socket
import math

def atoi(str):
    num = ""
    for char in str:
        if char == "-" or char == "+":
            num = num + char
        elif char.isnumeric() == True:
            num = num + char
        else:
            return (float(num))
    return (float(num))


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
        # break ;
        data = data[data.find("please:") + 8:]
        print(data)
        data = data.split(' ')
        # for i in data:
            # print(i)
        a = atoi(data[0])
        b = atoi(data[2])
        c = atoi(data[4])
        d = atoi(data[6])
        op1 = data[1]
        op1 = data[3]

        if d > 0:
            c -= d
        else:
            c += d

        delta = (b * b) - 4 * a * c
        if delta > 0:
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)
            x1 = float(format(x1, '.4f'))
            # print(x1)
            x1 = round(x1, 3)
            x1 = format(x1, '.3f')
            print(x1)
            x2 = float(format(x2, '.4f'))
            # print(x1)
            x2 = round(x2, 3)
            x2 = format(x2, '.3f')
            print(x2)
        elif delta == 0:
            x = - (b / (2 * a))
        # elif delta < 0:

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