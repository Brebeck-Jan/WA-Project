import socket
import pickle

def client(sender_id, receiver_id, message):
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('localhost', 8089))
    st={'sender_id':str(sender_id), 'message':message, 'receiver_id':str(receiver_id)}
    serialized_st = pickle.dumps(st)
    clientsocket.send(serialized_st)

client(98765,56789,'hallo')

