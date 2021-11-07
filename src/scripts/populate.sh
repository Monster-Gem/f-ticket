#!/bin/bash

podname=$(kubectl get pods --no-headers -o=name | grep mongodb  | sed "s/^.\{4\}//")

kubectl cp ./src/scripts/mongo $podname:.

kubectl exec $podname -- bash -c 'cd ./mongo && sh ./mongo_script.sh'