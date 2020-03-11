From the file where the JWT is run 
`hashcat --stdout Tools/hashcat/example.dict -r Tools/hashcat/rules/best64.rule | hashcat -m 16500 -d 2 jwt`
this will check the example.dict file for the matching signature of the known JWT file

Then running `hashcat --show jwt -m 16500` and this will show the original JWT and attatch the key that is used to sign this token
==>>>>
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjpudWxsfQ.Tr0VvdP6rVBGBGuI_luxGCOaz6BbhC6IxRTlKOW8UjM:__pentesterlab__