from pwnlib.util.fiddling import *
# http://docs.pwntools.com/en/stable/util/fiddling.html
# Working with the pwnlib fiddling utility to break the XOR ciphertext when part of it is known.

# Base64 decodes a string
b64edCiphertext = b64d("CQQSAhheX1RQTjdYAUgtX19eH1M9FQ==")
print(b64edCiphertext)

# Part of the b64edCiphertext that is known
cipher_front = 'flag{'

# Flattens its arguments using pwnlib.util.packing.flat() and then xors them together.
# xor(*args, cut = 'max') → str
candidate_key = xor(b64edCiphertext, cipher_front)[:len(cipher_front)]
print(candidate_key)
flag = xor(b64edCiphertext, candidate_key)

print(flag)
# print(f'{flag}')

