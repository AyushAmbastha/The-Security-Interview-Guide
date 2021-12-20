# Same Origin Policy

The same-origin policy is a critical security mechanism that restricts how a document or script loaded by one origin can interact with a resource from another origin.  It restricts scripts on one origin from accessing data from another origin.

The same-origin policy aims to prevent websites from attacking each other and helps isolate potentially malicious documents, reducing possible attack vectors. 

An origin consists of a URI scheme, domain and port number. \
Ex: http://www.example.com:8080/\
Here `http` is the scheme, `www.example.com` is the hostname or domain, and `8080` is the port number. 

* When no port is specified, the browser defaults to port 80. 
* The endpoints (such as /index.html/messages) are not part of the origin. 

Two URLs have the same origin if the protocol, port (if specified), and host are the same for both. The following table gives examples of origin comparisons with the URL http://store.company.com/dir/page.html:

| URL |	Outcome	| Reason |
|-----|---------|--------|
|http://store.company.com/dir2/other.html|Same origin|Only the path differs|
|http://store.company.com/dir/inner/another.html|	Same origin	|Only the path differs|
|https://store.company.com/page.html|	Failure|	Different protocol|
|http://store.company.com:81/dir/page.html|	Failure|	Different port (http:// is port 80 by default)|
|http://news.company.com/dir/page.html|	Failure	|Different host|



### Why is the same-origin policy necessary?
When a browser sends an HTTP request from one origin to another, any cookies, including authentication session cookies, relevant to the other domain are also sent as part of the request. This means that the response will be generated within the user's session, and include any relevant data that is specific to the user. Without the same-origin policy, if you visited a malicious website, it would be able to read your emails from Gmail, private messages  from Facebook, etc. 
Now if websites could not interact with each other, then the internet would be rather dull. How could any site interact with other sites ? How could google or facebook interact with each other and share data? This is where CORS comes into play.

