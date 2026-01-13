# Start of the ex. 
# open file

import json

with open('ucaccmet2j_python/precipitation.json') as file:
    data= json.load(file)


# Manually looking up seattle code
# US1WAKG0038
# creating a new dict with only seattle values

seattle= []

for measurement in data:
    if measurement["station"]=="GHCND:US1WAKG0038":
        seattle.append(measurement)
# added

#print(seattle)

# total monthly precipitation 
# creating a list with the total preci x month, 
# add every day of the month into a month value
# and a list with those month values


totalmonthly = {}
# I was doing it a very different way that apparently worked according to both TAs
# but it actually didn't
# so then eduardo helped me #thankssomuch


for measurement in seattle:
    date = measurement['date']
    month = date.split('-')[1]
        
    if month in totalmonthly:
        totalmonthly[month] += measurement['value']
    else:
        totalmonthly[month] = measurement['value']
           
print(totalmonthly)


# save to json

import json

with open('ucaccmet2j_python/results.json', 'w', encoding='utf-8') as file:
    json.dump(totalmonthly, file, indent=4)