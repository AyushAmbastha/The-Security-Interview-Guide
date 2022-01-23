# HTTP Parameter Pollution

HTTP Parameter Pollution (HPP) is an attack technique that allows an attacker to craft a HTTP request in order to manipulate or retrieve hidden information. This evasion technique is based on splitting an attack vector between multiple instances of a parameter with the same name. Since none of the relevant HTTP RFCs define the semantics of HTTP parameter manipulation, each web application delivery platform may deal with it differently. In particular, some environments process such requests by concatenating the values taken from all instances of a parameter name within the request. This behavior is abused by the attacker in order to bypass pattern-based security mechanisms.

Information transfer using the HTTP protocol can be done in various ways, such as:

1. Within the URI – using the GET parameters
2. Within the request body – using the POST parameters
3. In the HTTP headers – using the COOKIE header

The adopted technique depends on the application and on the type and amount of data that has to be transferred. Examples are -

```
GET /somePage.jsp?param1=value1& param2=value2 HTTP/1.1 Host: www.someHost.co.il User-Agent: Safari/535.1 Accept: text/html,application/xhtml+xml
```

```
POST /somePage.asp HTTP/1.1 Host: www.someHost.co.il User-Agent: Safari/535.1 Accept: text/html,application/xhtml+xml Content-Type: application/x-www-form-urlencoded Content-Length: 27param1=value1& param2=value2
```

In HPP, the attacker introduces multiple parameters with the same name into a single HTTP request, whereas the attack vector is split across all instances. Since RFC3986 does not specify a standard behavior in this situation, the exact processing semantics are dependent upon the specific application delivery environment. The IIS web server uses all occurrences of the parameter; Apache-based servers use the last occurrence of the parameter while Tomcat based servers use the first occurrence of the parameter.

## Mitigation

All user-supplied data, which is reflected in the HTML source code of the HTTP response, should be encoded according to the context in which they are reflected. For example by using URL-encoding in attributes that input is reflected, instead of HTML entities. 