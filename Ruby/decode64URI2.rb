# wfencode -e md5 test
require 'base64'
require 'uri'
require 'cgi'

first = Base64.decode64(URI.decode("3jFSCwN2SRAb0SRS6BEBuQ%3D%3D"))
puts first


second  = CGI.escape(Base64.strict_encode64("\xF4\xA1\xBBV\xBE\vZZ\xA3\x06C\xF6\xC5\xBC$j"))
puts second


# ---------

# test1
# test
# 3jFSCwN2SRAb0SRS6BEBuQ%3D%3D
# => "\xDE1R\v\x03vI\x10
# \e\xD1$R\xE8\x11\x01\xB9"

# test2
# test
# YSuUIzzTsAcb0SRS6BEBuQ%3D%3D
# => "a+\x94#<\xD3\xB0\a
# \e\xD1$R\xE8\x11\x01\xB9" 



# aaaaaaaaadmin
# test
# 9KG7Vr4LWlqjBkP2xbwkahvRJFLoEQG5
#  => "\xF4\xA1\xBBV\xBE\vZZ\xA3\x06C\xF6\xC5\xBC$j
# \e\xD1$R\xE8\x11\x01\xB9

# =>>> "\xF4\xA1\xBBV\xBE\vZZ\xA3\x06C\xF6\xC5\xBC$j
# 9KG7Vr4LWlqjBkP2xbwkag%3D%3D

# \e\xD1$R\xE8\x11\x01\xB9
# =>>>G9EkUugRAbk%3D




# aAdmin
# CcZpiCmxn6uzokAGzq4MXw%3D%3D
#  => "\t\xC6i\x88)\xB1\x9F\xAB\xB3\xA2@\x06\xCE\xAE\f_" 


# Aaaaaaaaaaaaaaaaadmin
# 9KG7Vr4LWlr0obtWvgtaWqMGQ%2FbFvCRqG9EkUugRAbk%3D
# URL decode  => "9KG7Vr4LWlr0obtWvgtaWqMGQ/bFvCRqG9EkUugRAbk=
# Base 64 decode => "\xF4\xA1\xBBV\xBE\vZZ\xF4\xA1\xBBV\xBE\vZZ\xA3\x06C\xF6\xC5\xBC$j\e\xD1$R\xE8\x11\x01\xB9" 
# \xF4\xA1\xBBV\xBE\vZZ
# \xF4\xA1\xBBV\xBE\vZZ
# \xA3\x06C\xF6\xC5\xBC$j\e\xD1$R\xE8\x11\x01\xB9

# Cgi  => "owZD9sW8JGob0SRS6BEBuQ%3D%3D" 

# CGI.escape(Base64.strict_encode64("\xE0Vd.)r\xEBz\aO\xC6d\x19\xE3+\xE3"))
