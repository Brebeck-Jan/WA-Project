import socket
import pickle

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(200)
    #buf.decode()
    buf = pickle.loads(buf)
    if len(buf) > 0:
        print('sender_id: ' + buf['sender_id'])
        print('message: ' + buf['message'])
        print('receiver_id: ' + buf['receiver_id'])
    break