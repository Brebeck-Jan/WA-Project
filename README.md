# README des WhatsApp projektes von AlphaFinTech

### Kafka

Start minikube
In directory kafka:
	run: bash -x deploy.sh

In root directory:
	run: skaffold dev


### Gateway

schritt 1: server.py ausführen
	dieser wartet dann auf eine message
schritt 2: in client.py die function client(sender_id, receiver_id, message) aufrufen
schritt 3: schauen, was beim server.py angekommen ist

