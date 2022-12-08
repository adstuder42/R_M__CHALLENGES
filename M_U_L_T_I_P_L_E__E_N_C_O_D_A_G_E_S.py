import socket
import base64

morse_code = {".-":'a', "-...":'b', "-.-.":'c',  "-..":'d',  ".":'e', "..-.":'f', "--.":'g', "....":'h',
 "..":'i', ".---":'j', "-.-":'k', ".-..":'l', "--":'m', "-.":'n', "---":'o', ".--.":'p', "--.-":'q',
 ".-.":'r', "...":'s', "-":'t',"..-":'u', "...-":'v', ".--":'w', "-..-":'x', "-.--":'y', "--..":'z'}

def morse_decode(encoded):
    # encoded = "---/.--./../---/.--./..../.-/--./-.--"
    decoded = ""
    print("morse")
    characters = encoded.split('/')
    for char in characters:
        decoded += morse_code[char]
    return (decoded)

def base85_decode(encoded):
    # encoded = "Wo~q3a&K*AXJKr4"
    print("b85")
    decoded = base64.b85decode(encoded.encode("UTF-8"))
    plaintext = decoded.decode("UTF-8")
    return plaintext

def base64_decode(encoded):
    # encoded = "bm9uc2FsZQ=="
    try:
        decoded = base64.b64decode(encoded.encode("UTF-8"))
        plaintext = decoded.decode("UTF-8")
    except:
        return base85_decode(encoded)
    print("b64")
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
    decoded = bytes.fromhex(encoded).decode('UTF-8')
    return (decoded)

def client_program():
    host = 'challenge01.XXXXXXXXX.org'
    port = 52017
    last = 0

    client_socket = socket.socket()
    client_socket.connect((host, port))

    while (1):
        
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
