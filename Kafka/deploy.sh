helm repo add strimzi http://strimzi.io/charts/                                                               
                                                                                                              
helm install --wait my-kafka-operator strimzi/strimzi-kafka-operator                                          

kubectl apply -f ./kafka/kafka-cluster-def.yaml
