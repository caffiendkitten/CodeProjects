
import binascii
import hashlib
import json

cookie = {"user": 'hacker', "password": 'password', "admin": True}
cookie["digest"] = 'hackshackshackshackshackshackshackshackshackshackshackshackshack'
print(binascii.hexlify(json.dumps(cookie).encode("utf8")))