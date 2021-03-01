# This cipher was created for the HTB Bank Hist.
# It takes two strings that are created from the numbers on a phone and translates them to text.
# It then takes the output of the second one that is still garbled and deciphers it again via its location in the alphabet.
# This will disclose the word which is the flag for this box.


from itertools import product
import string

dictionary={
    '2':'A', '22':'B', '222':'C',
    '3':'D', '33':'E', '333':'F',
    '4':'G', '44':'H', '444':'I',
    '5':'J', '55':'K', '555':'L',
    '6':'M', '66':'N', '666':'O',
    '7':'P', '77':'Q', '777':'R', '7777':'S',
    '8':'T', '88':'U', '888':'V',
    '9':'W', '99':'X', '999':'Y', '9999':'Z'
}

cipherText1="444333 99966688 277733 7773323444664 84433 22244474433777 99966688 277733 666552999 99966688777 777744277733 666333 84433 443344477778 4447777 44466 99966688777 4466688777733 84433 5533999 8666 84433 55566622255 4447777 22335556669 4666 8666 727774447777"
cipherText2="47777888 995559888 4555 47777888 44999988 666555997  8555444888477744488866888648833369"

cipherText1=cipherText1.split()
cipherText2=cipherText2.split()

def get_word(number):
    word=number[0]
    plain=""
    for i in range(1, len(number)):
        if number[i]==number[i-1]:
            word+=number[i]
        else:
            plain+=dictionary[word]
            word=number[i]
    plain+=dictionary[word]
    return plain
plain_text=""
for ele in cipherText1:
    plain_text+=get_word(ele)
    plain_text+=' '
print(plain_text+".")
plain_text=""
for ele in cipherText2:
    plain_text+=get_word(ele)
    plain_text+=' '
print(plain_text+".")




lower= list(string.ascii_lowercase)
# vocab="GSV XLWV GL GSV HZU OLXP TLIVGRIVNVMGUFMW"
flag=plain_text.split()
FLAG=""
for each in flag:
    for char in each:
        number=25-lower.index(char.lower())
        FLAG+=lower[number].upper()
    FLAG+=" "
print(FLAG)