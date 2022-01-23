bioDict =	{
  "name": "javed",
  "rollno": 25,
  "year": 1964
}
print(bioDict)
# getting the value of key from dictonary
print(bioDict["name"]) 
# with get method we can also find value
x=bioDict.get('name')
print(x)
# The keys() method will return a list of all the keys in the dictionary.
x=bioDict.keys()
print(x)
# if same key is present than new key overwrite it
bioDict =	{
  "name": "javed",
  "rollno": 25,
  "year": 1964,
  'year':1992,
  'box':['pen','pencil']
}
print(bioDict)
print(bioDict["box"])
# The items() method will return each item in a dictionary, as tuples in a list.
print(bioDict.items())

