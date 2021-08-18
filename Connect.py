import socket
from types import resolve_bases
server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'doctor_remarkable'
token = 'oauth:qai92v51z01253epp7cpacy833uljy'
channel = '#wildez'





sock = socket.socket()
sock.connect((server,port))

sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))


#resp = sock.recv(4096).decode('utf-8')
#resp = sock.read(4096).decode('utf-8')
#print(resp)


def joinchat():
    dictOfNames = {}
    Loading = True
    while Loading:
        readbuffer_join = sock.recv(1024)
        readbuffer_join = readbuffer_join.decode()
        for line in readbuffer_join.split("\n"):
            name = str(line[1:10])
            if name == 'tmi.twitc' or '':
                break
            if name in dictOfNames:
                dictOfNames[name] += 1
            else:
                dictOfNames[name] = 1
        print(dictOfNames)    
           

joinchat()

'''
        for line in readbuffer_join.split("/n"):
            print(line)
            Loading = loadingComplete(line)

def loadingComplete(line):
    if ("End of /NAMES list" in line):
        return False
    else:
        return True
'''


