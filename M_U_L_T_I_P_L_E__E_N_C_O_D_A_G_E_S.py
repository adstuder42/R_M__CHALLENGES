import socket
import base64

def morse_code(code):
    if code == ".-":
        return 'a'
    elif code == "-...":
        return 'b'
    elif code == "-.-.":
        return 'c'
    elif code == "-..":
        return 'd'
    elif code == ".":
        return 'e'
    elif code == "..-.":
        return 'f'
    elif code == "--.":
        return 'g'
    elif code == "....":
        return 'h'
    elif code == "..":
        return 'i'
    elif code == ".---":
        return 'j'
    elif code == "-.-":
        return 'k'
    elif code == ".-..":
        return 'l'
    elif code == "--":
        return 'm'
    elif code == "-.":
        return 'n'
    elif code == "---":
        return 'o'
    elif code == ".--.":
        return 'p'
    elif code == "--.-":
        return 'q'
    elif code == ".-.":
        return 'r'
    elif code == "...":
        return 's'
    elif code == "-":
        return 't'
    elif code == "..-":
        return 'u'
    elif code == "...-":
        return 'v'
    elif code == ".--":
        return 'w'
    elif code == "-..-":
        return 'x'
    elif code == "-.--":
        return 'y'
    elif code == "--..":
        return 'z'

def morse(encoded):
    # encoded = "---/.--./../---/.--./..../.-/--./-.--"
    decoded = ""
    characters = encoded.split('/')
    for char in characters:
        decoded += morse_code(char)
    print(decoded)
    return decoded

def base85(encoded):
    # encoded = "Wo~q3a&K*AXJKr4"

    decoded = base64.b85decode(encoded.encode("UTF-8"))
    plaintext = decoded.decode("UTF-8")
    print(plaintext)























def client_program():
    base85("")
    exit()
    host = 'challenge01.root-me.org'
    port = 52017  # socket server port number
    data = ""
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    data = client_socket.recv(1024).decode()  # receive response
    data = data.split('\'')
    print(data[len(data) - 2])

    # data = data[data.find(": '") + 3]
    # x = data.split('\'')
    # print(data)
    
        # message = "2\n";  # take
    rep = str(data) + '\n'
    client_socket.send(rep.encode())  # send message 
    data = client_socket.recv(1024).decode()  # receive response

    print(data)
        # token =   ""
        # client_socket.send((token + "\n").encode())  # send message
        # data = client_socket.recv(1024).decode()  # receive response
        # data = data + client_socket.recv(1024).decode()  # receive response

if __name__ == '__main__':
    client_program()