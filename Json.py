From Python to JSON (Serialization, Encode)
# Convert Python objects into a JSON string with the json.dumps() method.

import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# convert into JSON:
person_json = json.dumps(person)
# use different formatting style
person_json2 = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True)

# the result is a JSON string:
print(person_json) 
print(person_json2) 

Output:
{"name": "John", "age": 30, "city": "New York", "hasChildren": false, "titles": ["engineer", "programmer"]}
{
    "age"= 30; 
    "city"= "New York"; 
    "hasChildren"= false; 
    "name"= "John"; 
    "titles"= [
        "engineer"; 
        "programmer"
    ]
}


# We can also create a custom Encoder class, and overwrite the default() method. Use this for the cls argument in the json.dump() method, or use 
# the encoder directly.

from json import JSONEncoder
class ComplexEncoder(JSONEncoder):
    
    def default(self, o):
        if isinstance(z, complex):
            return {z.__class__.__name__: True, "real":z.real, "imag":z.imag}
        # Let the base class default method handle other objects or raise a TypeError
        return JSONEncoder.default(self, o)
    
z = 5 + 9j
zJSON = json.dumps(z, cls=ComplexEncoder)
print(zJSON)
# or use encoder directly:
zJson = ComplexEncoder().encode(z)
print(zJSON)

Output:
{"complex": true, "real": 5.0, "imag": 9.0}
{"complex": true, "real": 5.0, "imag": 9.0}


Decoder

# Possible but decoded as a dictionary
z = json.loads(zJSON)
print(type(z))
print(z)

def decode_complex(dct):
    if complex.__name__ in dct:
        return complex(dct["real"], dct["imag"])
    return dct

# Now the object is of type complex after decoding
z = json.loads(zJSON, object_hook=decode_complex)
print(type(z))
print(z)

Output:
<class 'dict'>
{'complex': True, 'real': 5.0, 'imag': 9.0}
<class 'complex'>
(5+9j)













