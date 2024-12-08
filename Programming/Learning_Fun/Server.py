'''Create a server.py that has a password.

When clients connect they should first send a password that the user on the client types.

Your server should check to ensure that this password matches.

If the password does not match then close the connection after sending a message stating 'access denied'

if the password DOES match, allow that client access to chat with the server like in the example I showed in the lectures with a few additional features.

When a message is displayed on the client the message should be 'SERVER>>' + msg and vice versa'''



import socket
#Create Socket Object (Always this way)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9001
#bind IP address and Port number over 1024
s.bind((host, port))
#listen
s.listen()
#accept
client, addr = s.accept() #returns two objects
#We not have a connection
print(f'Connection received from: {addr}')

while True:
    data = input('Enter a message: ')
    client.sendall(str.encode(data)) #send all data in messages data and encode to byte
    msg = client.recv(1024).decode()
    if not msg:
         break
    print(msg)
client.close()
