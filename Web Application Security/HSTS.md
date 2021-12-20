# HSTS (HTTP Strict-Transport-Security)
The HTTP Strict-Transport-Security response header lets a website tell browsers that it should only be accessed using HTTPS, instead of using HTTP.
Note: The Strict-Transport-Security header is ignored by the browser when your site is accessed using HTTP; this is because an attacker may intercept HTTP connections and inject the header or remove it. When your site is accessed over HTTPS with no certificate errors, the browser knows your site is HTTPS capable and will honor the Strict-Transport-Security header. A domain instructs browsers that it has enabled HSTS by returning an HTTP header over an HTTPS connection.

When a browser knows that a domain has enabled HSTS, it does two things:
- Always uses an https:// connection, even when clicking on an http:// link or after typing a domain into the location bar without specifying a protocol.
- Removes the ability for users to click through warnings about invalid certificates.

In its simplest form, the policy tells a browser to enable HSTS for that exact domain or subdomain, and to remember it for a given number of seconds:
`Strict-Transport-Security: max-age=31536000;`
 
In its strongest and recommended form, the HSTS policy includes all subdomains, and indicates a willingness to be “preloaded” into browsers:
`Strict-Transport-Security: max-age=31536000;`\
`includeSubDomains; preload`

An example scenario - You log into a free WiFi access point at an airport and start surfing the web, visiting your online banking service to check your balance and pay a couple of bills. Unfortunately, the access point you're using is actually a hacker's laptop, and they're intercepting your original HTTP request and redirecting you to a clone of your bank's site instead of the real thing. Now your private data is exposed to the hacker. Strict Transport Security resolves this problem; as long as you've accessed your bank's web site once using HTTPS, and the bank's web site uses Strict Transport Security, your browser will know to automatically use only HTTPS, which prevents hackers from performing this sort of man-in-the-middle attack.

How the browser handles it - The first time your site is accessed using HTTPS and it returns the Strict-Transport-Security header, the browser records this information, so that future attempts to load the site using HTTP will automatically use HTTPS instead. When the expiration time specified by the Strict-Transport-Security header elapses, the next attempt to load the site via HTTP will proceed as normal instead of automatically using HTTPS. Whenever the Strict-Transport-Security header is delivered to the browser, it will update the expiration time for that site, so sites can refresh this information and prevent the timeout from expiring. Should it be necessary to disable Strict Transport Security, setting the max-age to 0 (over an https connection) will immediately expire the Strict-Transport-Security header, allowing access via http.