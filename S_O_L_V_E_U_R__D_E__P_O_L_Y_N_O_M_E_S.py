from re import I
import socket
import math
from xml.sax.handler import DTDHandler

def atoi(str):
    num = ""
    for char in str:
        if char == "-" or char == "+":
            num = num + char
        elif char.isnumeric() == True:
            num = num + char
        else:
            print("====" + num)
            return (float(num))
    print("====" + num)
    return (float(num))


def client_program():
    host = 'challenge01.root-me.org'
    port = 52018
    client_socket = socket.socket()
    client_socket.connect((host, port))
    i = 0
    while (i < 27):
        data = ""
        data = client_socket.recv(1024).decode()
        print(data)
        if i == 9:
            return
        data = data[data.find("please:") + 8:]
        data = data.split(' ')
        a = atoi(data[0])
        b = atoi(data[2])
        c = atoi(data[4])
        d = atoi(data[6])
        op1 = data[1]
        op2 = data[3]
        if op1 == "-":
            b = -b
        if op2 == "-":
            c = -c
        if d > 0:
            c -= d
        else:
            c += d
        delta = (b * b) - (4 * a * c)
        print("delta == ")
        print(delta)
        if delta > 0:
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)
            x1 = float(format(x1, '.4f'))
            x1 = round(x1, 3)
            x1 = format(x1, '.3f')
            print(x1)
            x2 = float(format(x2, '.4f'))
            # print(x1)
            x2 = round(x2, 3)
            x2 = format(x2, '.3f')
            # print(x2)
            res = "x1: " + x1 + " ; x2: " + x2
        elif delta == 0:
            x = - (b / (2 * a))
            res = "x: " + x
        else:
            res = "Not possible"  
        print(res)     
        res += '\n'
        client_socket.send(res.encode())
        i += 1

if __name__ == '__main__':
    client_program()