#!/bin/bash

mongo --eval 'db.user.insert({"public_id" : "352cdb4e-58b9-406a-b463-e964a9438f5f", "email": "eliot@gmail.com", "password": "pbkdf2:sha256:260000$i0bQKydzIBm0ihLK$56fe084874b69092fd9463ec628f60fac10684e561b3c48a03df7866e7b6ed3f", "role": "ADMIN"});' f_database