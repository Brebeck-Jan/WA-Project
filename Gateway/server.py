# Python program to implement server side of chat room. 
import socket 
import select 
import sys 
from _thread import *
  
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
  
# checks whether sufficient arguments have been provided 
if len(sys.argv) != 3: 
    print("Correct usage: script, IP address, port number")
    exit() 
  
# takes the first argument from command prompt as IP address 
IP_address = str(sys.argv[1]) 
  
# takes second argument from command prompt as port number 
Port = int(sys.argv[2]) 
  

server.bind((IP_address, Port)) 
  
server.listen(100) #change the number if you want more then 100 connections
  
list_of_clients = [] 
  
def clientthread(conn, addr): 
  
    # sends a message to the client whose user object is conn 
    conn.send(b"Welcome to this chatroom!") 
    conn.send(str(addr[1]).encode("UTF-8"))
  
    while True: 
            try: 
                message = conn.recv(2048)

                # Calls broadcast function to send message to all 
                message_to_send = "<" + str(addr[1]) + "> " + message.decode("utf-8") 
                print(message_to_send)
                # broadcast(message_to_send, conn) 
                test_sender(message.decode("UTF-8"))

            except: 
                continue
  
def broadcast(message, connection): 
    print(list_of_clients[0])
    print(type(list_of_clients[0]))
    print(list_of_clients[0].getsockname()[1])
    print(list_of_clients[0].getpeername()[1])
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
  
def test_sender(message): 
    print(list_of_clients)
    for clients in list_of_clients: 
        # print(clients.getpeername()[1])
        # print(type(clients.getpeername()[1]))
        # print(str(clients.getpeername()[1]))
        print(message.strip())
        print(str(clients.getpeername()[1]))
        print(message.strip() == str(clients.getpeername()[1]))
        if message.strip() == str(clients.getpeername()[1]):
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