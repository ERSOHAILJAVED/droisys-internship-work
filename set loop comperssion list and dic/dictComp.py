# dictinoaries compression
cites=['bareilly','newyork','paris']
countries=['india','usa','france']
# first we use zip function to convert it pair (a,b) i.e tuples
z=zip(cites,countries)
# checking the pairs
for val in z:
    print(val)

dcites_Country={cities:country for cities,country in zip(cites,countries)}
print(dcites_Country)
print(type(dcites_Country))