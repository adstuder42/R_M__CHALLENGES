import socket
import requests
# import urllib.request
# import urllib3


def get_question():
    HOST = 'ctf19.root-me.org'
    PORT = 4444
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    print('Connexion to ' + HOST + ':' + str(PORT) + ' successful.')
    datas = client.recv(4096)
    datas = client.recv(4096)
    # print('no question :', datas)
    datas = client.recv(4096)
    print('Recu :', datas)
    datas = datas.decode('UTF-8')
# url

    print(datas)
    split = datas.split("\"")
    cookie = split[9]
    url = split[3]
    url = url.replace('XX', '19')
    question = split[13]
    question = question.replace('?', '')
    question = question.replace("What\'s the ", "")
    print(url)
    print(question)
    words = question.split(" ")
    print(words)









    
    return 
    i = 9
    url = ""
    while (datas[i] != "\""):
        if datas[i] == 'X':
            url = url + "03"
            i += 2
        else:
            url = url + datas[i]
            i += 1

# cookie
    cookie = ""
    i = datas.find("random")
    i += 10
    while (datas[i] != "\""):
        cookie += datas[i]
        i += 1


    datas = datas[datas.find("question"):]




    first = dict(innerText = 0, innerHTML = 0, outerHTML = 0, lastChild = 0, firstChild = 0, parent = 0, random = 0, _class = 0, nonce = 0, footer = 0, td = 0, h3 = 0, tr = 0, id = 0, br = 0)




    first = dict(innerText = 0, innerHTML = 0, outerHTML = 0, lastChild = 0, firstChild = 0, parent = 0, div = 0, i = 0)
    second = dict(nonce = 0, id = 0, random = 0, lang = 0, _class = 0, tag = 0)
    third = dict(ul = 0, strong = 0, footer = 0, p = 0, div = 0, h1 = 0)
    
    keywords = dict(of = 0)

    of_first = dict(element = 0, a = 0, footer = 0, ul = 0, td = 0, li = 0, h1 = 0, br = 0, p = 0)
    of_second = dict(footer = 0, ul = 0, strong = 0, div = 0)
    # si of [1 2 3] IN 
    if (datas.find("of ")) != -1:
        keywords["of"] = 1
 
 
 
    if datas[0:i].find("innerText") != -1:
        first["innerText"] = 1
    if datas[0:i].find("innerHTML") != -1:
        first["innerHTML"] = 1
    if datas[0:i].find("outerHTML") != -1:
        first["outerHTML"] = 1
    if datas[0:i].find("last child") != -1:
        first["lastChild"] = 1
    if datas[0:i].find("first child") != -1:
        first["firstChild"] = 1
    if datas[0:i].find("parent") != -1:
        first["parent"] = 1
    if datas[0:i].find("div") != -1:
        first["div"] = 1
    if datas[0:i].find("i's") != -1:
        first["i"] = 1


    if datas[0:i].find("nonce") != -1:
        second["nonce"] = 1
    if datas[0:i].find("id") != -1:
        second["id"] = 1
    if datas[0:i].find("random") != -1:
        second["random"] = 1
    if datas[0:i].find("lang") != -1:
        second["lang"] = 1
    if datas[0:i].find("class") != -1:
        second["_class"] = 1



    if datas[0:i].find("ul") != -1:
        third["ul"] = 1
    if datas[0:i].find("strong") != -1:
        third["strong"] = 1
    if datas[0:i].find("footer") != -1:
        third["footer"] = 1
    if datas[0:i].find("p") != -1:
        third["p"] = 1    
    if datas[0:i].find("div") != -1:
        third["div"] = 1
    if datas[0:i].find("h1") != -1:
        third["h1"] = 1
    if datas[0:i].find("h3") != -1:
        third["h3"] = 1
    if datas[0:i].find("h1") != -1:
        third["h1"] = 1
    if datas[0:i].find("h1") != -1:
        third["h1"] = 1



    print(first)
    print(second)
    print(third)
    return 

# identifier
    identifier = ""
    i = datas.find("with")
    if i != -1:
        i += 5
        while (datas[i] != "\""):
            identifier += datas[i]
            i += 1

# child
    child = ""
    i = datas.find("child")
    if i != -1:
        if datas.find("first") != -1:
            child = "first"
        elif datas.find("last") != -1:
            child = "last"

# parent
    parent = ""
    if child == "":
        parent = "parent"

# location
    location = ""
    if child == "":
        i = datas.find("s the")
        if i != -1:
            i += 6
            while (datas[i] != ' '):
                location += datas[i]
                i += 1

# page_location
    page_location = ""
    if location == "page":
        i = datas.find("page")
        i += 5
        while (datas[i] != '?'):
            page_location += datas[i]
            i += 1


# target_type
    target_type = ""
    if child == "child":
        i = datas.find("child")
        i += 8

    print("url = " + url)
    print("cookie == " + cookie)
    print("child == " + child)
    print("parent == " + parent)
    print("location == " + location)
    print("page_location == " + page_location)
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
