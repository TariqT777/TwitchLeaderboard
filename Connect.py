from flask import Flask,make_response,request, render_template
from flask_socketio import SocketIO,send
import socket
from types import resolve_bases
server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'doctor_remarkable'
token = 'oauth:qai92v51z01253epp7cpacy833uljy'
channel = '#jay3'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

sock = socket.socket()
sock.connect((server,port))

sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))


#resp = sock.recv(4096).decode('utf-8')
#resp = sock.read(4096).decode('utf-8')
#print(resp)

dictOfNames = {}
def joinchat():
    
    dataToReturn = []
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
            elif name not in dictOfNames:
                dictOfNames[name] = 1
            if len(dictOfNames) >= 1:
                sortDict = dict(sorted(dictOfNames.items(), key=lambda item: item[1],reverse=True))
                nameItems = sortDict.items()
                yield list(nameItems)[0:10]
        #print(dict(sorted(dictOfNames.items(), key=lambda item: item[1],reverse=True)))

winner = joinchat()
def display():
    while winner:
        test = next(winner)
        print(test)
        yield test

dataDisplay = display()
@app.route('/')
def Index():
    printedDictionary = "hi"
    return render_template('index.html', data = next(dataDisplay))    

@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast = True)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html')

if __name__ == '__main__':
    socketio.run(app)
    #app.run(debug=True)



     

#joinchat()
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


