# This file will decompress files that are imported to it.

import zlib

#filename = 'C:\\Users\\jtmchung\\Documents\\testz\\dest-dir\\.git\\objects\\05\\480569507a37df7731115a5888f91b145c189d'
#filename = 'C:\\Users\\jtmchung\\Documents\\testz\\dest-dir\\.git\\objects\\8e\\8fa0346aacb508d314990b6677d60ddb73839c'
filename = 'C:\\Users\\DaNeil\\Documents\\0x00CTF\\0df3efe45d6cc67321193204f1649a57a36c83'
#filename = 'C:\\Users\\jtmchung\\Documents\\testz\\dest-dir\\.git\\objects\\05\\480569507a37df7731115a5888f91b145c189d'
compressed_contents = open(filename, 'rb').read()
decompressed_contents = zlib.decompress(compressed_contents)

print(decompressed_contents)