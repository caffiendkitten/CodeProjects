# !/user/bin/python3
# This program will encrypt the input with the Ceasar Cipher


def cipher1(inputz, shift):
    alphabetLower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    alphabetUpper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    for x in alphabet:
        print(x.upper()+ ",")
    print("hit")

















inputz = input("Please enter input to the ciper: ") 
inputz = int(inputz) # Given number
shift = input("Please enter shift value: ") 
shift = int(shift) # Given shift value
cipher1(inputz, shift)




