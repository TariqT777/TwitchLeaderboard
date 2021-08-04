server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'twitchChatReader'
token = 'oauth:qai92v51z01253epp7cpacy833uljy'
channel = '#Otzdarva'



import socket

sock = socket.socket()
sock.connect((server,port))

sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"Nick {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))


resp = sock.recv(2048).decode('utf-8')
print(resp)
