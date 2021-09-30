#!/bin/bash

mongoimport --db f_database --collection user --file ./seeds/user.json
mongoimport --db f_database --collection city --file ./seeds/city.json
mongoimport --db f_database --collection airport --file ./seeds/airport.json
mongoimport --db f_database --collection route --file ./seeds/route.json
mongoimport --db f_database --collection flight --file ./seeds/flight.json
mongoimport --db f_database --collection order --file ./seeds/order.json
mongoimport --db f_database --collection ticket --file ./seeds/ticket.json
echo "Database populated"