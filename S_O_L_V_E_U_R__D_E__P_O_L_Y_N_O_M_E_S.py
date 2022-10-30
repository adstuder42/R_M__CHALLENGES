import socket
import math
import time

def atoi(strr):
    num = ""
    for char in strr:
        if char == "-" or char == "+":
            num = num + char
        elif char.isnumeric() == True:
            num = num + char
        else:
            return (float(num))
    return (float(num))


def client_program():
    host = 'challenge01.XXXXX.org'
    port = 52018
    client_socket = socket.socket()
    client_socket.connect((host, port))
    i = 0
    while (i < 26):
        data = ""
        data = client_socket.recv(1024).decode()
        print(data)
        if data.find("Wrong") != -1:
            i = 0;
            client_program()
            return
        if data.find("job") != -1:
            print(data)
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
        
        c -= d
        delta = (b * b) - (4 * a * c)
        res = ""
        if delta > 0:
            deltasqrt = math.sqrt(delta)
            x1 = (-b - deltasqrt) / (2 * a)
            x2 = (-b + deltasqrt) / (2 * a)
            x1 = round(x1, 3)
            x1 = format(x1, '.3f')
            x2 = round(x2, 3)
            x2 = format(x2, '.3f')
            res = "x1: " + x1 + " ; x2: " + x2
        elif delta == 0:
            x = - (b / (2 * a))
            res = "x: " + x
        else:
            res = "Not possible"  
        print(res)     
        res += '\n'
        res = str(res)
        client_socket.send(res.encode())
        i += 1
        # time.sleep(0.2)

if __name__ == '__main__':
    client_program()