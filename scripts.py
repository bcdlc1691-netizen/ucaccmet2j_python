# Start of the ex. 
# open file
print()

import json

with open('ucaccmet2j_python/precipitation.json') as file:
    data= json.load(file)


# Manually looking up seattle code
# US1WAKG0038
# creating a new dict with only seattle values

# now changing not only to seattle but to option user wants

ask=input("Which city? Cincinnati=1, Seattle=2, Maui=3, San Diego=4 ")

if ask== '1':
    code= "GHCND:USW00093814"
    name= "Cincinnati"
elif ask== '2':
    code= "GHCND:US1WAKG0038"
    name= "Seattle"
elif ask== '3':
    code= "GHCND:USC00513317"
    name= "Maui"
elif ask=='4':
    code= 'GHCND:US1CASD0032'
    name= 'San Diego'
else:
    exit()

city= []
print(name)

for measurement in data:
    if measurement["station"]==(f"{code}"):
        city.append(measurement)
# added

# total monthly precipitation 
# creating a list with the total preci x month, 
# add every day of the month into a month value
# and a list with those month values


totalmonthly = {}
# I was doing it a very different way that apparently worked according to both TAs
# but it actually didn't
# so then eduardo helped me #thankssomuch

print(f"Monthly precipitation for {name} in units")
print()

for measurement in city:
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

print(f"Total yearly precipitation for {name}")

# this could be done just with total monthly but oh well
totalyearly = 0
for measurement in city:
    totalyearly += measurement['value']
print(totalyearly)

print()

# relative monthly precipitation
# per month
# dictionary, key = month, value = percentage 

print(f"Relative monthly precipitation for {name} as a percentage of yearly total")
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


