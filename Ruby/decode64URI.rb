require 'base64'
require 'uri'
require 'cgi'

first = Base64.decode64(URI.decode("9KG7Vr4LWlq%2BezPUf74w6jIknlbv8qFO"))
puts "first" + first