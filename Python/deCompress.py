# This file will decompress files that are imported to it.

import zlib

#filename = '\05\\480569507a37df7731115a5888f91b145c189d'
#filename = \objects\\8e\\8fa0346aacb508d314990b6677d60ddb73839c'
# filename = '0df3efe45d6cc67321193204f1649a57a36c83'
#filename = '\objects\\05\\480569507a37df7731115a5888f91b145c189d'

# filename = '../PTLFiles/8529a63a01fad516905bce9ccf1c3df9a14d06'
filename = '../PTLFiles/646db7f9c7e6f126c75900fdcce16d50e1da82'



compressed_contents = open(filename, 'rb').read()
decompressed_contents = zlib.decompress(compressed_contents)

print(decompressed_contents)