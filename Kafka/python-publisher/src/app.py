import time

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="my-cluster-kafka-bootstrap:9092")


def publisher(sender_id, receiver_id, message):
    next_msg = {"sender_id": sender_id, "receiver_id": receiver_id, "message": message}
    producer.send("What´s App", next_msg.encode())
