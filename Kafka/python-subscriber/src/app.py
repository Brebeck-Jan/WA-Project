# Install: pip3 install kafka-python
from kafka import KafkaConsumer
from GroupService.groupservice import *
# The bootstrap server to connect to
bootstrap = 'my-cluster-kafka-bootstrap:9092'

# Create a comsumer instance
# cf.
print('Starting KafkaConsumer')
consumer = KafkaConsumer('big_data_demo',  # <-- topics
                         bootstrap_servers=bootstrap)

# Print out all received messages
for msg in consumer:
    
    if "g" in msg["reciever_id"]:

        # message goes to a group
        recievers = get_group_members(msg["reciever_id"], msg["sender_id"])

        for reciever in recievers:
            
            # pseudio - later send to server instead
            print("user:", msg["sender_id"], "send message", msg["message"], "to", reciever)
    
    else:

        print("user:", msg["sender_id"], "send message", msg["message"], "to", msg["reciever_id"])