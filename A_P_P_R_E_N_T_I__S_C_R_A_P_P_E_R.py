import socket
import requests
import urllib.request
import urllib3


HOST = 'ctf06.root-me.org'
PORT = 4444

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print('Connexion vers ' + HOST + ':' + str(PORT) + ' reussie.')

donnees = client.recv(4096)
donnees = client.recv(4096)
donnees = client.recv(4096)
print('Recu :', donnees)




url = 'http://ctf06.root-me.org:8000/partenaires'
cookies = dict(random='931307')
r = requests.get(url, cookies=cookies)
print(r.text)


# webpage = requests.get('http://ctf06.root-me.org:8000/partenaires', cookies={'random': 731309}).text
# webpage = requests.get('http://ctf06.root-me.org:8000/partenaires', cookies={'required_cookie': 731309}, headers={'User-Agent': 'Mozilla/5.0'}).text

# cookies = {'required_cookie': 731309}
# headers = {'User-Agent': 'Mozilla/5.0'}
# response = requests.get('http://ctf06.root-me.org:8000/partenaires', cookies=cookies, headers=headers)

# webpage = response.text

# print(webpage)


# with urllib.request.urlopen('http://ctf06.root-me.org:8000/partenaires') as f:
#     print(f.read())
# print('Deconnexion.')


client.close()
