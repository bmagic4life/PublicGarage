'''Create a server.py that has a password.

When clients connect they should first send a password that the user on the client types.

Your server should check to ensure that this password matches.

If the password does not match then close the connection after sending a message stating 'access denied'

if the password DOES match, allow that client access to chat with the server like in the example I showed in the lectures with a few additional features.

When a message is displayed on the client the message should be 'SERVER>>' + msg and vice versa'''

import socket
#create socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9001
# connect
s.connect((host, port))

while True:
    msg = s.recv(1024).decode()
    if not msg:
        break
    print(msg)
    data = input('Enter a message: ')
    s.sendall(str.encode(data))

s.close()
