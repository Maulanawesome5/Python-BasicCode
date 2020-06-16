# JSON is a syntax for storing and exchanging data
# JSON is text, written with JavaScript Object Notation

import json

# if you have a JSON string, you can parse it using the json.loads() method
# some JSON :
x = '{"name":"Chuck", "age":"50", "city":"New York"}'

# parse X:
y = json.loads(x)

# the result is a Python dictionary :
print(y["age"])

# If you have a Python object, you can convert it into a JSON string
# by using the json.dumps() method

# a Python object (dict):
x = {
    "name" : "Chuck",
    "age" : 30,
    "city" : "new york"
}
#convert into JSON :
y = json.dumps(x)

#the result is a JSON string :
print(y)

# You can convert Python object into JSON strings, and print the value
print(json.dumps({"name": "Chuck", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hallo"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))