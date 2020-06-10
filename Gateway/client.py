# Python program to implement client side of chat room. 
import socket 
import select 
import sys 
import json
  
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
if len(sys.argv) != 3: 
    print("Correct usage: script, IP address, port number")
    exit() 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
server.connect((IP_address, Port)) 
ID = 0
while True: 
  
    # maintains a list of possible input streams 
    sockets_list = [sys.stdin, server] 
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[]) 
  
    for socks in read_sockets: 
        if socks == server: 
            message = socks.recv(2048)
            if ID == 0:
                print(message)
                ID = message
            else:
                message = json.loads(message)
                print(f"Message from {message['sender']}: {message['message']}")
        else: 
            input_message = sys.stdin.readline()
            receiver, message = input_message.split(":")
            message_to_send = json.dumps({"clienttype":"client","receiver":receiver,"message":message[1:]})
            server.send(message_to_send.encode('utf-8'))
            # sys.stdout.write("<You>") 
            # sys.stdout.write(message)
            sys.stdout.flush()
server.close()
