# Python program to implement server side of chat room. 
import socket 
import select 
import sys 
import json
import time
from _thread import *

# import publisher
import importlib.util
spec = importlib.util.spec_from_file_location("app.publisher", "./python-publisher/src/app.py")
publisher_app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(publisher_app)
  
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
  
# checks whether sufficient arguments have been provided 
# if len(sys.argv) != 3: 
#     print("Correct usage: script, IP address, port number")
#     exit() 
  
# # takes the first argument from command prompt as IP address 
# IP_address = str(sys.argv[1]) 
  
# # takes second argument from command prompt as port number 
# Port = int(sys.argv[2]) 

# takes the first argument from command prompt as IP address 
IP_address = "127.0.0.1"
  
# takes second argument from command prompt as port number 
Port = 8080 
  

server.bind((IP_address, Port)) 
  
server.listen(100) #change the number if you want more then 100 connections
  
list_of_clients = []

print("Exectuted")
  
def clientthread(conn, addr): 
    id = str(addr[1])
    #sends the clients his id
    conn.send(id.encode("UTF-8"))
    while True: 
            try: 
                message = conn.recv(2048)
                message = message.decode("UTF-8").replace("'", "\"")
                message = json.loads(message)
                message["message"] = message["message"].rstrip() 
                print(message)
                print(message["receiver"])

                if message["clienttype"] == "client":
                    print("client")
                    publisher_app.publisher(sender_id=id,receiver_id=message["receiver"],message=message["message"])
                    # for testing purpose:
                    # sender(sender=id,receivers=[id],message=message["message"])
                    
                elif message["clienttype"] == "server":
                    print("server")
                    sender(sender=message["sender"],receiver=message["receiver"],message=message["message"])
                else:
                    print("no valid clienttype: "+message[clienttype])
            except: 
                continue

def sender(sender, receivers, message):
    print("sender")
    message_to_send = json.dumps({"sender":sender,"message":message})
    print(message_to_send)
    print(receivers)
    for client in list_of_clients: 
        print(str(client.getpeername()[1]))
        if client!=sender and str(client.getpeername()[1]) in receivers:
            try: 
                print("Message to send: "+message_to_send)
                client.send(message_to_send.encode("UTF-8")) 
            except: 
                print("Exception in broadcast occures")
                client.close() 

def send_to_one_receiver(message, receiver_id): 
    # deprecated
    print(list_of_clients)
    for clients in list_of_clients: 
        if receiver_id.strip() == str(clients.getpeername()[1]):
            try:
                print("message to send: (send_to_one)"+message)
                clients.send(message.encode("UTF-8"))
            except: 
                print("Exception in broadcast occures")
                clients.close() 
                # if the link is broken, we remove the client 
                remove(clients) 
        else:
            print("no receiver was found")
  
def broadcast(message, connection): 
    # deprecated
    for clients in list_of_clients: 
        if clients!=connection: 
            try: 
                print("Message to send: "+message)
                clients.send(message.encode("UTF-8")) 
            except: 
                print("Exception in broadcast occures")
                clients.close() 
                # if the link is broken, we remove the client 
                remove(clients) 
  
  
def remove(connection): 
    if connection in list_of_clients: 
        list_of_clients.remove(connection) 
  
while True: 
    conn, addr = server.accept() 
    list_of_clients.append(conn) 
    # prints the address of the user that just connected 
    print(addr[0] + " connected")
  
    # creates and individual thread for every user  
    # that connects 
    start_new_thread(clientthread,(conn,addr))     
  
conn.close() 
server.close()