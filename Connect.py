from flask import Flask,make_response,request, render_template
import socket
from types import resolve_bases
server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'doctor_remarkable'
token = 'oauth:qai92v51z01253epp7cpacy833uljy'
channel = '#swehyt'

app = Flask(__name__)
@app.route('/')

def Index():
    
    sock = socket.socket()
    sock.connect((server,port))
    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {nickname}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))
    
    dictOfNames = {}
    Loading = True
    printedDictionary = "hi"
    '''while Loading:
        readbuffer_join = sock.recv(1024)
        readbuffer_join = readbuffer_join.decode()
        for line in readbuffer_join.split("\n"):
            #print(line)
            userName = line.split("!",1)
            name = userName[0]
            if "tmi.twitch" in name or name == ':doctor_remarkable' or name == '':
                continue
            if name in dictOfNames:
                dictOfNames[name] += 1
            else:
                dictOfNames[name] = 1
        # dict(sorted(dictOfNames.items(), key=lambda item: item[1],reverse=True))
'''    
    return render_template('index.html', data = printedDictionary)

if __name__ == '__main__':
    app.run(debug=True)


'''
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
            #print(line)
            userName = line.split("!",1)
            name = userName[0]
            if "tmi.twitch" in name or name == ':doctor_remarkable' or name == '':
                continue
            if name in dictOfNames:
                dictOfNames[name] += 1
            else:
                dictOfNames[name] = 1
        print(dict(sorted(dictOfNames.items(), key=lambda item: item[1],reverse=True)))
           

joinchat()
'''


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


