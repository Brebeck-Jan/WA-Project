import time

import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

install("kafka-python")

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="my-cluster-kafka-bootstrap:9092", api_version=(0,10, 1))


def publisher(sender_id, receiver_id, message):
    next_msg = {"sender_id": sender_id, "receiver_id": receiver_id, "message": message}
    producer.send("whats_app", next_msg.encode())
