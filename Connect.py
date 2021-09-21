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
    dictEntries = 0
    dataToReturn = []
    Loading = True
    while Loading:
        readbuffer_join = sock.recv(1024)
        readbuffer_join = readbuffer_join.decode()
        for line in readbuffer_join.split("\n"):
            #print(line)
            userName = line.split("!",1)
            name = userName[0]
            if "tmi.twitch" in name or name == ':doctor_remarkable' or name == '' or 'bot' in name: 
                # Taking 'bot' out of results may cause bugs for real people that have the letters 'bot' in their name in that letter order, but it's rare and prevents a streamer's bots from skewing results.
                continue
            if name in dictOfNames:
                dictOfNames[name] += 1
            elif name not in dictOfNames:
                dictOfNames[name] = 1
            if len(dictOfNames) >= 1:
                sortDict = dict(sorted(dictOfNames.items(), key=lambda item: item[1],reverse=True))
                nameItems = sortDict.items()
                if dictEntries % 4 == 0: #This allows more entries to be stored in dictionary before printing to the client's screen.
                   # This yield is giving data to display one entry into the dictionary at a time. For fast chats (i.e chats with a lot of people talking at one time, yield only printing one entry at a time become increasingly slow and less accurate to real time.)
                    yield list(nameItems)[0:10] 
                dictEntries += 1
        #print(dict(sorted(dictOfNames.items(), key=lambda item: item[1],reverse=True)))

winner = joinchat()
'''
def display():
    while winner:
        test = next(winner)
        print(test)
        yield test

dataDisplay = display()
'''
'''
@socketio.on('connection')
def printData(data):
    print("Top chatters are:",next(dataDisplay))
    send(data, broadcast = True)
'''
@app.route('/')
def Index():
    return render_template('index.html', channelName = channel, data = next(winner)) 

  

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


