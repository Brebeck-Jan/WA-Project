# Install: pip3 install kafka-python
import socket
import sys
from kafka import KafkaConsumer
from GroupService.groupservice import *
# The bootstrap server to connect to
bootstrap = 'my-cluster-kafka-bootstrap:9092'

# Create a comsumer instance
# cf.
print('Starting KafkaConsumer')
consumer = KafkaConsumer('whats_app',  # <-- topics
                         bootstrap_servers=bootstrap, api_version=(0,10, 1))

# connect to websocket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
# if len(sys.argv) != 3: 
#     print("Correct usage: script, IP address, port number")
#     exit() 
# IP_address = str(sys.argv[1]) 
# Port = int(sys.argv[2])
IP_address = "127.0.0.1"
Port = 8080 
server.connect((IP_address, Port)) 

# Print out all received messages
for msg in consumer:
    
    if "g" in msg["reciever_id"]:

        # message goes to a group
        recievers = get_group_members(msg["reciever_id"], msg["sender_id"])

        for reciever in recievers:
            
            # pseudio - later send to server instead
            print("user:", msg["sender_id"], "send message", msg["message"], "to", reciever)

            # send message to server
            message_to_send = json.dumps({"clienttype":"server","receiver":receiver,"message":msg["message"], "sender":msg["sender_id"]})
            server.send(message_to_send.encode('utf-8'))
    
    else:

        print("user:", msg["sender_id"], "send message", msg["message"], "to", msg["reciever_id"])

        message_to_send = json.dumps({"clienttype":"server","receiver":receiver,"message":msg["message"], "sender":msg["sender_id"]})
        server.send(message_to_send.encode('utf-8'))