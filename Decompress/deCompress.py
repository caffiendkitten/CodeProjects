# !/user/bin/python3
# This script was built to decompress (Git) files that are imported to it.
import zlib

# Examples of file paths/names
# filename = '\05\\480569507a37df7731115a5888f91b145c189d'
# filename = \objects\\8e\\8fa0346aacb508d314990b6677d60ddb73839c'
# filename = '\objects\\05\\480569507a37df7731115a5888f91b145c189d'
# filename = '../PTLFiles/8529a63a01fad516905bce9ccf1c3df9a14d06'

# The chosen file to decompress.
filename = '6d09bae474eb6887cf5f4c9e5c9018fecac28d'

# Opens the file to read it.
compressed_contents = open(filename, 'rb').read()

# Decompresses the contents of the file.
decompressed_contents = zlib.decompress(compressed_contents)

# Prints the decompressed contents of the file to the screen.
print(decompressed_contents)