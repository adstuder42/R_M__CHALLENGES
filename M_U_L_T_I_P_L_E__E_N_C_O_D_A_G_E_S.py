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

def morse_decode(encoded):
    # encoded = "---/.--./../---/.--./..../.-/--./-.--"
    decoded = ""
    print("morse")
    characters = encoded.split('/')
    for char in characters:
        decoded += morse_code(char)
    return (decoded)

def base85_decode(encoded):
    # encoded = "Wo~q3a&K*AXJKr4"
    print("b85")
    decoded = base64.b85decode(encoded.encode("UTF-8"))
    plaintext = decoded.decode("UTF-8")
    return plaintext

def base64_decode(encoded):
    # encoded = "bm9uc2FsZQ=="
    print("b64")
    try:
        decoded = base64.b64decode(encoded.encode("UTF-8"))
        plaintext = decoded.decode("UTF-8")
    except:
        return base85_decode(encoded)
    return (plaintext)

def base32_decode(encoded):
    # encoded = "MFZGCYTBNZQQ===="
    print("b32")
    decoded = base64.b32decode(encoded.encode("UTF-8"))
    plaintext = decoded.decode("UTF-8")
    return (plaintext)

def hex_decode(encoded):
    # encoded = "707465726f636c69646165"
    print("hex")
    decoded = bytes.fromhex(encoded).decode('utf-8')
    return (decoded)

def client_program():
    host = 'xxxxxxxxxxxx'
    port = 52017
    client_socket = socket.socket()
    client_socket.connect((host, port))
    i = 0
    last = 0

    while (i < 10):
        
        ishex = 1
        ismorse = 1
        isb64 = 1
        isb32 = 1
        
        data = ""
        data = client_socket.recv(1024).decode()
        print(data)
        if last == 1:
            exit()
        if data.find("100/100") != -1:
            last = 1

        data = data.split('\'')
        cypher = data[len(data) - 2]
        print("decoding: [" + cypher + ']')
        # print(data[len(data) - 2])
        
        for char in cypher:
            if char.isupper() == True or char.isalnum == False:
                ishex = 0
            if char.isupper() == False and char.isnumeric() == False and char != "=":
                isb32 = 0
            if char.isalnum() == False and char != "=":
                isb64 = 0
            if char != '-' and char != '.' and char != '/':
                ismorse = 0

        if ismorse == 1:
            rep = morse_decode(cypher) 
        elif ishex == 1:
            rep = hex_decode(cypher)
        elif isb32 == 1:
            rep = base32_decode(cypher)
        elif isb64 == 1:
            rep = base64_decode(cypher)
        else:
            rep = base85_decode(cypher)
            
        print(rep)
        rep = rep + '\n'
        client_socket.send(rep.encode())

if __name__ == '__main__':
    client_program()