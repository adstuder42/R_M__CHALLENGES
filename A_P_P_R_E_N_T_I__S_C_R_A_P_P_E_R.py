import socket
import requests
# import urllib.request
# import urllib3


def get_question():
    HOST = 'ctf06.root-me.org'
    PORT = 4444
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print('Connexion to ' + HOST + ':' + str(PORT) + ' successful.')
    datas = client.recv(4096)
    datas = client.recv(4096)
    # print('no question :', datas)
    datas = client.recv(4096)
    print('Recu :', datas)
    datastr = datas.decode('UTF-8')

# url
    i = 9
    url = ""
    while (datastr[i] != "\""):
        if datastr[i] == 'X':
            url = url + "06"
            i += 2
        else:
            url = url + datastr[i]
            i += 1

# cookie
    cookie = ""
    i = datastr.find("random")
    i += 10
    while (datastr[i] != "\""):
        cookie += datastr[i]
        i += 1

# identifier
    identifier = ""
    i = datastr.find("with")
    if i != -1:
        i += 5
        while (datastr[i] != "\""):
            identifier += datastr[i]
            i += 1

# child
    child = ""
    i = datastr.find("child")
    if i != -1:
        if datastr.find("first") != -1:
            child = "first"
        elif datastr.find("last") != -1:
            child = "last"
# parent
    if child == "":
        parent = "parent"
# location
    location = ""
    if child == "":
        i = datastr.find("s the")
        if i != -1:
            i += 6
            while (datastr[i] != ' '):
                location += datastr[i]
                i += 1
            
# target_type
    target_type = ""
    if child == "child":
        i = datastr.find("child")
        i += 8





    print("url = " + url)
    print("cookie == " + cookie)
    print("child == " + child)
    print("parent == " + parent)
    print("location == " + location)
    print("identifier == " + identifier)

    client.close()


# url = 'http://ctf06.root-me.org:8000/partenaires'
# cookies = dict(random='931307')
# r = requests.get(url, cookies=cookies)
# print(r.text)


def main():
    get_question()


if __name__ == "__main__":
    main()
