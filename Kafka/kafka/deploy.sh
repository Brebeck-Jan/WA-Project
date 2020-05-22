#!/bin/bash

helm install --wait my-kafka-operator strimzi/strimzi-kafka-operator

kubectl apply -f kafka-cluster-def.yaml