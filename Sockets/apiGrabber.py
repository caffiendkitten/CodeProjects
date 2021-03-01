# !/user/bin/python3

import urllib.request
import string
import requests
import sys
import json
import os
import xml.etree.ElementTree as ET
import time
from datetime import datetime



# Makes list of all journal entried and saves them to file
def create(file):
    print("\nFile does not exist and will be created and filled... \r ")
    jsonData = ""

    for num in range(1, 543):
        try:
            # Define the main URL that is needed for the user. You should just need to replace 
            URL = "http://x.x.x.x/api/v1/user/string here later/{}".format(num)


            print("Trying to connect to: ",URL)





            #Performs a POST on the specified url to get the service ticket
            response = requests.get(URL)
            responseContent = response.content
            decodedResponseContent = responseContent.decode('utf-8', errors="ignore")
            # print("decodedResponseContent",decodedResponseContent)
            if len(decodedResponseContent) > 10:
                decodedResponseContentString = str(responseContent).replace("b'", "")
                decodedResponseContentString = decodedResponseContentString.replace("'", '')
                # print("\r response: ", decodedResponseContentString, "\r")
                jsonData += decodedResponseContentString
            else:
                print("user num {} is empty".format(num))
            print("\rDone appending the jsonData: ", jsonData)
        except Exception as err:
            print("error is ", err)
    print("\r all data collected. now writing file")
    file.write(jsonData)
    print("Done creating file\n")



# Separate out entries for better formatting of the XML
def separate(file):
    data = file.read()
    data = str(data)

    # temp = "["
    # temp += data
    # temp += "]"

    # data = temp



    # res = json.loads(data)
    



    # split at "\n" char if there
    splitData1 = data.replace('\\n', "n")
    splitData1 = data.split('n')
    print("data is: ", splitData1)

    # # get jsonz data
    userID, userData = [], []
    for num in range(1, 543):
        userID.append(num)
    try:
        # for key, value in returnedData:
        #     print(key, value)
        
        for line in splitData1:
            line1 = json.loads(line)
            print("\n \nreturnedData line here: ", json.loads(line))
            print("type of line: ", typeof(line))
            userData.append(line1)

        score_userData = [{ "UserID": s, "UserData": t} for t, s in zip(userData, userID)]
        print("\n\nScored Data: ",score_userData, "\n\n")
        # Printing in JSON format
        # print("Json Dumped data:", json.dumps(score_userData))
    except Exception as err:
        print("nope", err)


    # try:
    #     for y in splitData2:
    #         # print("\nsplit: "+ y)
    #     # jsonedData = JSON.parse(returnedData)
    #         # print("type of returned data is: ", type(y))
    #         print("hit in 2nd try")
    # except Exception as err:
    #     print("didnt work ", err)

    # # for jsonedData 
    # # myObj = { "name":"John", "age":30, "car":null };
    # returnedData = ""
    # for x in jsonedData:
    #     returnedData += x["apikey"]
    # print(returnedData)
    

    # This will clear the existing file to a blank slate
    tempd = "       "
    for x in data:
        x = " "
        tempd = tempd + x
    file.seek(0)
    file.write(tempd)

    # The next two lines will replace the existing text in the file with the new processed text
    file.seek(0)
    file.write(data)

def readIt(file):
    try:
        data = file.read()
        root = ET.fromstring(data)
        
        count = 0
        for entry in root.findall("entry"):
            count += 1
        print("\nThere are {} entries currently".format(count))#, rank)
    
        entryLocation = int(input("which entry would you like to read?: ")) - 1

        print("\nitemid: ",root[entryLocation][0].text)
        print("eventtime: ",root[entryLocation][1].text)
        print("logtime: ",root[entryLocation][2].text)
        print("subject: ",root[entryLocation][3].text)
        print("event: ",root[entryLocation][4].text)
    except ET.ParseError as err:
        print("error:", err)

def addto(data, file_name):
    dateTimeObj = datetime.now()
    eventTime = dateTimeObj.strftime("%F %H:%M:%S")

    try:
        root = ET.fromstring(data)

        count = 0
        for entry in root:
                count += 1                
        print("\nYou currently have {} entries.".format(count))

        entry = ET.Element("entry")

        itemid = ET.SubElement(entry, "itemid")
        itemid.text = str(count + 1)

        eventtime = ET.SubElement(entry, "eventtime")
        eventtime.text = str(eventTime)

        dateTimeObj2 = datetime.now()
        logTime = dateTimeObj2.strftime("%F %H:%M:%S")
        logtime = ET.SubElement(entry, "logtime")
        logtime.text = str(logTime)

        subject = ET.SubElement(entry, "subject")
        subject.text = input("Enter the subject of the entry: ")

        entryData = ET.SubElement(entry, "event")
        entryData.text = input("What would you like to say? : ")

        security = ET.SubElement(entry, "security")
        security.text = "usemask"

        allowmask = ET.SubElement(entry, "allowmask")
        allowmask.text = str(1)

        currentMusic = ET.SubElement(entry, "current_music")
        currentMusic.text = input("What are you listening to? : ")

        currentMood = ET.SubElement(entry, "current_mood")
        currentMood.text = input("What is your current mood? : ")


        print(ET.dump(entry))

        root.append(entry)
        tree = ET.ElementTree(root)
        tree.write(file_name, encoding="utf-8")

        return 

    except ET.ParseError as err:
        print("errors:", err)




menuList = '''
~~~~~~~~~~~~~~~~~~~~~~~~
Enter your value:
1 = Create journal file
2 = Seperate data in file
3 = Read Journal File
4 = Add Entry
0 = Quit
~~~~~~~~~~~~~~~~~~~~~~~~\n'''

val = int(input(menuList))

while val > 0:
    if val == 1:
        print("#1: Create file\r\n")
        file_name = input("Enter a file name to check existance:\r\n" )
        if os.path.exists(file_name):
            print(file_name + " already exists\r\n")
        else:
            file = open(file_name, "a")
            create(file)
            file.close()
        val = int(input(menuList))
        print(val,"chosen \n") 
    
    elif val == 2:
        # sets file up to be added to
        print("\r\n#2: Format file")
        file_name = input("Enter a file name to process:\r\n" )
        if os.path.exists(file_name):
            file = open(file_name, "r+", encoding="utf-8")
            separate(file)
            file.close()
        else:
            print(file_name + "does not exist")
        val = int(input(menuList))
        print(val, "chosen \n")
    
    elif val == 3:
        # sets file up to be processed
        print("\r\n#3: Read File")
        file_name = input("Enter a file name to reading:\r\n" )
        if os.path.exists(file_name):
            file = open(file_name, "r", encoding="utf-8")
            readIt(file)
            file.close()
        else:
            print("not found")
        val = int(input(menuList))
        print(val, "chosen \n")

    elif val == 4:
        # sets file up to be processed
        print("\r\n#4: Add Entry")
        file_name = input("Enter a file name to add entry to:\r\n" )
        if os.path.exists(file_name):
            with open(file_name) as file_in:
                lines = ""
                for line in file_in:
                    lines = lines + line
                file_in.close()
            file = open(file_name, "a+")
            addto(lines, file_name)
        else:
            print("not found")
        val = int(input(menuList))
        print(val, "chosen \n")
else:
    print("bye")
