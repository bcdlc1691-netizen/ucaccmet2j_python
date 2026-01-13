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
# now to every single thing. like ever
# GIANT for loop, let us try

listofcitynames={"Cincinnati", "Seattle", 'Maui', 'San Diego'}

for cityname in listofcitynames:
    if cityname== 'Cincinnati':
        code= "GHCND:USW00093814"
        
    elif cityname== 'Seattle':
        code= "GHCND:US1WAKG0038"
    
    elif cityname== 'Maui':
        code= "GHCND:USC00513317"

    elif cityname=='San Diego':
        code= 'GHCND:US1CASD0032'
    
    else:
        exit()

    city= []


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

    print(f"Monthly precipitation for {cityname} in units")
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

    ## plot bonus did not work, continue

    # Calculate total yearly preci, 
    # the sum of preci in a year for location

    print(f"Total yearly precipitation for {cityname}")

    # this could be done just with total monthly but oh well
    totalyearly = 0
    for measurement in city:
        totalyearly += measurement['value']
    print(totalyearly)

    print()

    # relative monthly precipitation
    # per month
    # dictionary, key = month, value = percentage 

    print(f"Relative monthly precipitation for {cityname} as a percentage of yearly total")
    print()

    relativemonthly = {}
    for month in totalmonthly.values():
        relativemonthly[month] = (month/ totalyearly) * 100
        relativemonthly[month] = round(relativemonthly[month], 2)

    listrm= (list(relativemonthly.values()))
    print(listrm)

    print()

    # save to alr existing json file!


    # Intercity rains
    # ask user for which station they want?
    # now i have to save everything to the json
    # first solve json line problem that pops up 
    # done
    # i want to save everything I printed to json
    # does not work

    # import json

    # with open('ucaccmet2j_python/results.json', 'w', encoding='utf-8') as file:
    #     json.dump(totalmonthly, file, indent=4)
    # with open('ucaccmet2j_python/results.json', 'a', encoding='utf-8') as file:
    #     json.dump(listrm, file, indent=4)
# should be in this form


# finaldata= {
    # "Cincinnati": {
    # "station": "GHCND: ",
    # "state": " ",
    # "total_monthly_precipitation": [...],
    # "total_yearly_precipitation": ...,
    # "relative_monthly_precipitation": [...],
    # "relative_yearly_precipitation": ...
    # }
    # "Seattle": {
    # "station": "GHCND: ",
    # "state": " ",
    # "total_monthly_precipitation": [...],
    # "total_yearly_precipitation": ...,
    # "relative_monthly_precipitation": [...],
    # "relative_yearly_precipitation": ...
    # }
    # "Maui": {
    # "station": "GHCND:",
    # "state": " ",
    # "total_monthly_precipitation": [...],
    # "total_yearly_precipitation": ...,
    # "relative_monthly_precipitation": [...],
    # "relative_yearly_precipitation": ...
    # }
    # 'San Diego': {
    # "station": "GHCND:",
    # "state": " ",
    # "total_monthly_precipitation": [...],
    # "total_yearly_precipitation": ...,
    # "relative_monthly_precipitation": [...],
    # "relative_yearly_precipitation": ...
    # }
# }