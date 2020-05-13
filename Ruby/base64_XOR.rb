# Electronic Code Book Exercise

require 'base64'
require 'uri'
require 'cgi'

flag_prefix = "flag{"
ciphertext = "CQQSAhheX1RQTjdYAUgtX19eH1M9FQ=="


def xor(str1, flag)
    ret = ""
    str1.split(//).each do | i|
        ret[i] = (str1[i].ord ^ flag[i].ord)
    end
    return ret
end

DecodedCiphertext = Base64.decode64(ciphertext)
DecodedCiphertext2 = DecodedCiphertext.chr
puts "DecodedCiphertext1:" + DecodedCiphertext
puts "DecodedCiphertext2:" + DecodedCiphertext2

xored_key = xor(ciphertext, flag_prefix)
puts "XORed:" + xored_key

xored = xor(ciphertext, xored_key)
puts "XORedfinal:" + xored


# run irb
# 2.6.1 :001 > 0x55^'a'.ord^'b'.ord
#  => 86 
# 2.6.1 :002 > "%2x" % 86
#  => "56" 


# 'a' is the byte we want 
# 'b' is the byte we registered as

# flag{17'5-X0r-N07-z0R}-22
#:      ^_TPN7XH-__^S=:-20