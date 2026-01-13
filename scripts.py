# Start of the ex. 
# open file
print()

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

print("Monthly precipitation for the area in units")
print()

for measurement in seattle:
    date = measurement['date']
    month = date.split('-')[1]
        
    if month in totalmonthly:
        totalmonthly[month] += measurement['value']
    else:
        totalmonthly[month] = measurement['value']
           
print(totalmonthly)

print()

# save to json

import json

with open('ucaccmet2j_python/results.json', 'w', encoding='utf-8') as file:
    json.dump(totalmonthly, file, indent=4)

## plot bonus did not work, continue

# Calculate total yearly preci, 
# the sum of preci in a year for location

print("Total yearly precipitation for the area")

# this could be done just with total monthly but oh well
totalyearly = 0
for measurement in seattle:
    totalyearly += measurement['value']
print(totalyearly)

print()
# relative monthly precipitation
# per month
# dictionary, key = month, value = percentage 

print("Relative monthly precipitation for the area as a percentage of yearly total")
print()

relativemonthly = {}
for month in totalmonthly.values():
    relativemonthly[month] = (month/ totalyearly) * 100
    relativemonthly[month] = round(relativemonthly[month], 2)

listrm= (list(relativemonthly.values()))
print(listrm)

print()

# save to alr existing json file!

with open('ucaccmet2j_python/results.json', "a", encoding='utf-8') as file:
    json.dump(listrm, file, indent=4)

# Intercity rains
# ask user for which station they want?


