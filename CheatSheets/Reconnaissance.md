## Reconnaissance Cheat Sheet
<hr>

### __Map Out the Attack Surface__ Parts of the site may be hidden. These techniques will help you find them.

#### Check robots.txt
The robots.txt file, found in a site's web root, tells well-behaved web crawlers what parts of the site to ignore. You're not a well-behaved web crawler, so you can look at those pages. You may find pages the rest of the site doesn't link to.

#### Try some common URLs
By guessing common page and directory names, you might be able to discover even more content. A tool like dirbuster can help (but it's probably overkill here).

#### Look for HTML comments &amp; hidden elements
Look for forms, form fields and links that appear in the page source, but aren't visible on the page. The CSS style `display: none;` hides an element; remove the styling to make it visible again. Take a look at the HTML comments too!

### System Fingerprinting Identify what components the system is using.
#### Questions to ask
- Which web server - Apache, nginx, IIS?
- Which web framework - .NET, Django, Struts?
- Which database - MSSQL, MySQL...?
- Version numbers for web server and other components - are they up to date?
- How do they handle session management? Did they use a framework or roll their own?

#### Where to look
- __HTTP response headers__ - look for `Server` and `X-Powered-By`
- __Error messages__ - look for version Info and stack traces.
- __Cookies__ - cookie names can reveal framework info. If they're managing cookies themselves, think about how they're being generated. Are they predictable? How are they processed on the server?

### Open Source Intelligence (OSINT)Gather information on the public internet
#### What to look for
- Known vulnerabilities in frameworks/other components
- Default credentials
- Employee contact info/personal information

#### How to find it
- Google error messages, cookie names, version headers, password hashes...
- Read framework/component documentation
- Read framework/component security advisories
- Look up company employees on social media


>Your Google searches aren't private! When testing real applications, don't Google password hashes or other highly sensitive information - not even in incognito mode.