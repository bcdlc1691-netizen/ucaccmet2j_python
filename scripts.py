# Start of the ex. 
# open file

import json

with open('ucaccmet2j_python/precipitation.json') as file:
    data= json.load(file)

print(data)

# Manually looking up seattle code
# US1WAKG0038
# creating a new dict with only seattle values

seattle= []

for measurement in data:
    if measurement["station"]=="GHCND:US1WAKG0038":
        print(measurement)
        seattle.append(measurement)
# added
