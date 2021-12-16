# HTTP Headers

A HTTP message with a few request headers for a GET request is shown below - 

<ins>Example: </ins>\
GET /home.html HTTP/1.1 \
Host: developer.mozilla.org \
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0 \
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8 \
Accept-Language: en-US,en;q=0.5 \
Accept-Encoding: gzip, deflate, br \
Referer: https://developer.mozilla.org/testpage.html \
Connection: keep-alive \
Upgrade-Insecure-Requests: 1 \
If-Modified-Since: Mon, 18 Jul 2016 02:36:04 GMT \
If-None-Match: "c561c68d0ba92bbeb8b0fff2a9199f722e3a621a" \
Cache-Control: max-age=0 \

## Verb | Path | Version
HTTP defines a set of request methods to indicate the desired action to be performed for a given resource. These request methods are referred to as **HTTP verbs**. Each of them implements a different semantic, but some common features are shared by a group of them: e.g. a request method can be safe, idempotent, or cacheable.

GET - The GET method requests a representation of the specified resource. Requests using GET should only retrieve data.

HEAD - The HEAD method asks for a response identical to a GET request, but without the response body.

POST - The POST method submits an entity to the specified resource, often causing a change in state or side effects on the server.

PUT - The PUT method replaces all current representations of the target resource with the request payload.

DELETE - The DELETE method deletes the specified resource.

CONNECT - The CONNECT method starts two-way communications with the requested resource. It can be used to open a tunnel.

OPTIONS - The OPTIONS method describes the communication options for the target resource.

TRACE - The TRACE method performs a message loop-back test along the path to the target resource.

PATCH - The PATCH method applies partial modifications to a resource.

**Path** refers to the path to the resource on the web server.  

**Version** refers to the version of the HTTP protocol being used. 

## Domain

Domain refers to which web server is being requested. It is the domain name or authority that governs the namespace.

## Accept

The Accept request HTTP header indicates which content types, expressed as MIME types, the client is able to understand (A media type, also known as a Multipurpose Internet Mail Extensions or MIME type indicates the nature and format of a document, file, or assortment of bytes). The server uses content negotiation to select one of the proposals and informs the client of the choice with the Content-Type response header. Browsers set required values for this header based on the context of the request. For example, a browser uses different values in a request when fetches a CSS stylesheet, image, video, or a script.

Structure of a MIME type - type/subtype;parameter=value \
The type represents the general category into which the data type falls, such as video or text. The subtype identifies the exact kind of data of the specified type the MIME type represents. An optional parameter can be added to provide additional details.

Types can be - 
* application (any kind of binary data that doesn't fall explicitly into one of the other types)
* audio (audio or music)
* example (only used in sample codes and listings)
* font (font or typeface data)
* image (image or graphical data)
* model (model data for a 3d object or scene)
* text (text-only data including any human-readable content, source code, or textual data such as a CSV)
* video (video data or files)
* message (multipart - a message that encapsulates other messages)
* multipart (data that is comprised of multiple components which may individually have different MIME types)

Important MIME types for Web developers - 

* application/octet-stream - default for binary files
* text/plain - default for textual files
* text/css - css files used to style a web page
* text/html - html files
* text/javascript - javascript files

## Accept-language

The Accept-Language header indicates the natural language and locale that the client prefers. The server uses content negotiation to select one of the proposals and informs the client of the choice with the Content-Language response header. Browsers set required values for this header according to their active user interface language. Users rarely change it, and such changes are not recommended because they may lead to fingerprinting.

This header serves as a hint when the server cannot determine the target content language otherwise (for example, use a specific URL that depends on an explicit user decision). The server should never override an explicit user language choice. The content of Accept-Language is often out of a user's control (when traveling, for instance). A user may also want to visit a page in a language different from the user interface language.

The server possibly can send back a 406 (Not Acceptable) error code when unable to serve content in a matching language. However, such a behavior is rarely implemented for a better user experience, and servers often ignore the Accept-Language header in such cases.

\* - used for any language; '*' is used as a wildcard.

;q= (q-factor weighting) - Any value placed in an order of preference expressed using a relative quality value called weight.

## Accept-charset

Warning: Do not use this header. Browsers omit this header and servers should ignore it.

The Accept-Charset request HTTP header was a header that advertised a client's supported character encodings. It is no longer widely used.

UTF-8 is well-supported and the most preferred choice for character encoding. To guarantee better privacy through less configuration-based entropy, all browsers omit the Accept-Charset header. Chrome, Firefox, Internet Explorer, Opera, and Safari abandoned this header.

## Accept-encoding (compression type)

The Accept-Encoding request HTTP header indicates the content encoding (usually a compression algorithm) that the client can understand. The server uses content negotiation to select one of the proposal and informs the client of that choice with the Content-Encoding response header.

Even if both the client and the server support the same compression algorithms, the server may choose not to compress the body of a response if the identity value is also acceptable. Two common cases lead to this:

1. The data to be sent is already compressed, therefore a second compression will not reduce the transmitted data size. This is true for pre-compressed image formats (JPEG, for instance);
2. The server is overloaded and cannot allocate computing resources to perform the compression. For example, Microsoft recommends not to compress if a server uses more than 80% of its computational power.

As long as the identity;q=0 or *;q=0 directives do not explicitly forbid the identity value that means no encoding, the server must never return a 406 Not Acceptable error.

Accept-encoding values: gzip, compress, deflate, br, identity. One can set quality value syntax

## Connection - close or keep-alive

The Connection header controls whether the network connection stays open after the current transaction finishes. If the value sent is keep-alive, the connection is persistent and not closed, allowing for subsequent requests to the same server to be done.

Warning: Connection-specific header fields such as Connection and Keep-Alive are prohibited in HTTP/2. Chrome and Firefox ignore them in HTTP/2 responses, but Safari conforms to the HTTP/2 spec requirements and does not load any response that contains them.

Except for the standard hop-by-hop headers (Keep-Alive, Transfer-Encoding, Connection, Trailer, Upgrade, Proxy-Authorization and Proxy-Authenticate), any hop-by-hop headers used by the message must be listed in the Connection header, so that the first proxy knows it has to consume them and not forward them further. Standard hop-by-hop headers are also required to be listed.

close - Indicates that either the client or the server would like to close the connection. This is the default on HTTP/1.0 requests.

keep-alive - Indicates that the client would like to keep the connection open. Keeping a connection open is the default on HTTP/1.1 requests.

## Referrer

The Referrer header contains an absolute or partial address of the page that makes the request. This data can be used for analytics, logging, optimized caching, and more.

When you follow a link, the Referrer contains the address of the page that owns the link. When you make resource requests to another domain, the Referrer contains the address of the page that uses the requested resource.

The Referrer header can contain an origin, path, and querystring, and may not contain URL fragments (i.e. "#section") or "username:password" information. The request's referrer policy defines the data that can be included. 

# HTTP Response Headers

A response header is an HTTP header that can be used in an HTTP response and that doesn't relate to the content of the message. Response headers, like Age, Location or Server are used to give a more detailed context of the response.

Not all headers appearing in a response are categorized as response headers by the specification. For example, the Content-Type header is a representation header indicating the original type of data in the body of the response message (prior to the encoding in the Content-Encoding representation header being applied). However, "conversationally" all headers are usually referred to as response headers in a response message.

The following shows a few response and representation headers after a GET request.

200 OK \
Access-Control-Allow-Origin: * \
Connection: Keep-Alive \
Content-Encoding: gzip \
charset=utf-8 \
Date: Mon, 18 Jul 2016 16:06:00 GMT \
Etag: "c561c68d0ba92bbeb8b0f612a9199f722e3a621a" \
Keep-Alive: timeout=5, max=997 \
Last-Modified: Mon, 18 Jul 2016 02:36:04 GMT \
Server: Apache \
Set-Cookie: mykey=myvalue; expires=Mon, 17-Jul-2017 16:06:00 GMT; Max-Age=31449600; Path=/; secure \
Transfer-Encoding: chunked \
Vary: Cookie, Accept-Encoding \
X-Backend-Server: developer2.webapp.scl3.mozilla.com \
X-Cache-Info: not cacheable; meta data too large \
X-kuma-revision: 1085259 \
x-frame-options: DENY 

Most of the HTTP Response headers are similar to the HTTP Request headers. A major difference from an HTTP request is the Response Status Code. HTTP response status codes indicate whether a specific HTTP request has been successfully completed. Responses are grouped in five classes:

1. 1xx - Informational response
2. 2xx - Successful responses
3. 3xx - Redirection messages
4. 4xx - Client error responses
5. 5xx - Server error responses

## Information responses
* 100 Continue - This interim response indicates that the client should continue the request or ignore the response if the request is already finished.

* 101 Switching Protocols - This code is sent in response to an Upgrade request header from the client and indicates the protocol the server is switching to.

* 102 Processing (WebDAV) - This code indicates that the server has received and is processing the request, but no response is available yet.

* 103 Early Hints - This status code is primarily intended to be used with the Link header, letting the user agent start preloading resources while the server prepares a response.

## Successful responses
* 200 OK - The request succeeded. The result meaning of "success" depends on the HTTP method:

  - GET: The resource has been fetched and transmitted in the message body.
  - HEAD: The representation headers are included in the response without any message body.
  - PUT or POST: The resource describing the result of the action is transmitted in the message body.
  - TRACE: The message body contains the request message as received by the server.

* 201 Created - The request succeeded, and a new resource was created as a result. This is typically the response sent after POST requests, or some PUT requests.

* 202 Accepted - The request has been received but not yet acted upon. It is noncommittal, since there is no way in HTTP to later send an asynchronous response indicating the outcome of the request. It is intended for cases where another process or server handles the request, or for batch processing.

* 203 Non-Authoritative Information - This response code means the returned metadata is not exactly the same as is available from the origin server, but is collected from a local or a third-party copy. This is mostly used for mirrors or backups of another resource. Except for that specific case, the 200 OK response is preferred to this status.

* 204 No Content - There is no content to send for this request, but the headers may be useful. The user agent may update its cached headers for this resource with the new ones.

* 205 Reset Content - Tells the user agent to reset the document which sent this request.

* 206 Partial Content - This response code is used when the Range header is sent from the client to request only part of a resource.

* 207 Multi-Status (WebDAV) - Conveys information about multiple resources, for situations where multiple status codes might be appropriate.

* 208 Already Reported (WebDAV) - Used inside a <dav:propstat> response element to avoid repeatedly enumerating the internal members of multiple bindings to the same collection.

* 226 IM Used (HTTP Delta encoding) - The server has fulfilled a GET request for the resource, and the response is a representation of the result of one or more instance-manipulations applied to the current instance.

## Redirection messages
* 300 Multiple Choice - The request has more than one possible response. The user agent or user should choose one of them. (There is no standardized way of choosing one of the responses, but HTML links to the possibilities are recommended so the user can pick.)

* 301 Moved Permanently - The URL of the requested resource has been changed permanently. The new URL is given in the response.

* 302 Found - This response code means that the URI of requested resource has been changed temporarily. Further changes in the URI might be made in the future. Therefore, this same URI should be used by the client in future requests.

* 303 See Other - The server sent this response to direct the client to get the requested resource at another URI with a GET request.

* 304 Not Modified - This is used for caching purposes. It tells the client that the response has not been modified, so the client can continue to use the same cached version of the response.

* 305 Use Proxy - Defined in a previous version of the HTTP specification to indicate that a requested response must be accessed by a proxy. It has been deprecated due to security concerns regarding in-band configuration of a proxy.

* 306 unused - This response code is no longer used; it is just reserved. It was used in a previous version of the HTTP/1.1 specification.

* 307 Temporary Redirect - The server sends this response to direct the client to get the requested resource at another URI with same method that was used in the prior request. This has the same semantics as the 302 Found HTTP response code, with the exception that the user agent must not change the HTTP method used: if a POST was used in the first request, a POST must be used in the second request.

* 308 Permanent Redirect - This means that the resource is now permanently located at another URI, specified by the Location: HTTP Response header. This has the same semantics as the 301 Moved Permanently HTTP response code, with the exception that the user agent must not change the HTTP method used: if a POST was used in the first request, a POST must be used in the second request.

## Client error responses
* 400 Bad Request - The server could not understand the request due to invalid syntax.

* 401 Unauthorized - Although the HTTP standard specifies "unauthorized", semantically this response means "unauthenticated". That is, the client must authenticate itself to get the requested response.

* 402 Payment Required - This response code is reserved for future use. The initial aim for creating this code was using it for digital payment systems, however this status code is used very rarely and no standard convention exists.

* 403 Forbidden - The client does not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource. Unlike 401 Unauthorized, the client's identity is known to the server.

* 404 Not Found - The server can not find the requested resource. In the browser, this means the URL is not recognized. In an API, this can also mean that the endpoint is valid but the resource itself does not exist. Servers may also send this response instead of 403 Forbidden to hide the existence of a resource from an unauthorized client. This response code is probably the most well known due to its frequent occurrence on the web.

* 405 Method Not Allowed - The request method is known by the server but is not supported by the target resource. For example, an API may not allow calling DELETE to remove a resource.

* 406 Not Acceptable - This response is sent when the web server, after performing server-driven content negotiation, doesn't find any content that conforms to the criteria given by the user agent.

* 407 Proxy Authentication Required - This is similar to 401 Unauthorized but authentication is needed to be done by a proxy.

* 408 Request Timeout - This response is sent on an idle connection by some servers, even without any previous request by the client. It means that the server would like to shut down this unused connection. This response is used much more since some browsers, like Chrome, Firefox 27+, or IE9, use HTTP pre-connection mechanisms to speed up surfing. Also note that some servers merely shut down the connection without sending this message.

* 409 Conflict - This response is sent when a request conflicts with the current state of the server.

* 410 Gone - This response is sent when the requested content has been permanently deleted from server, with no forwarding address. Clients are expected to remove their caches and links to the resource. The HTTP specification intends this status code to be used for "limited-time, promotional services". APIs should not feel compelled to indicate resources that have been deleted with this status code.

* 411 Length Required - Server rejected the request because the Content-Length header field is not defined and the server requires it.

* 412 Precondition Failed - The client has indicated preconditions in its headers which the server does not meet.

* 413 Payload Too Large - Request entity is larger than limits defined by server. The server might close the connection or return an Retry-After header field.

* 414 URI Too Long - The URI requested by the client is longer than the server is willing to interpret.

* 415 Unsupported Media Type - The media format of the requested data is not supported by the server, so the server is rejecting the request.

* 416 Range Not Satisfiable - The range specified by the Range header field in the request cannot be fulfilled. It's possible that the range is outside the size of the target URI's data.

* 417 Expectation Failed - This response code means the expectation indicated by the Expect request header field cannot be met by the server.

* 418 I'm a teapot - The server refuses the attempt to brew coffee with a teapot.

* 421 Misdirected Request - The request was directed at a server that is not able to produce a response. This can be sent by a server that is not configured to produce responses for the combination of scheme and authority that are included in the request URI.

* 422 Unprocessable Entity (WebDAV) - The request was well-formed but was unable to be followed due to semantic errors.

* 423 Locked (WebDAV) - The resource that is being accessed is locked.

* 424 Failed Dependency (WebDAV) - The request failed due to failure of a previous request.

* 425 Too Early - Indicates that the server is unwilling to risk processing a request that might be replayed.

* 426 Upgrade Required - The server refuses to perform the request using the current protocol but might be willing to do so after the client upgrades to a different protocol. The server sends an Upgrade header in a 426 response to indicate the required protocol(s).

* 428 Precondition Required - The origin server requires the request to be conditional. This response is intended to prevent the 'lost update' problem, where a client GETs a resource's state, modifies it and PUTs it back to the server, when meanwhile a third party has modified the state on the server, leading to a conflict.

* 429 Too Many Requests - The user has sent too many requests in a given amount of time ("rate limiting").

* 431 Request Header Fields Too Large - The server is unwilling to process the request because its header fields are too large. The request may be resubmitted after reducing the size of the request header fields.

* 451 Unavailable For Legal Reasons - The user agent requested a resource that cannot legally be provided, such as a web page censored by a government.

## Server error responses
* 500 Internal Server Error - The server has encountered a situation it does not know how to handle.

* 501 Not Implemented - The request method is not supported by the server and cannot be handled. The only methods that servers are required to support (and therefore that must not return this code) are GET and HEAD.

* 502 Bad Gateway - This error response means that the server, while working as a gateway to get a response needed to handle the request, got an invalid response.

* 503 Service Unavailable - The server is not ready to handle the request. Common causes are a server that is down for maintenance or that is overloaded. Note that together with this response, a user-friendly page explaining the problem should be sent. This response should be used for temporary conditions and the Retry-After HTTP header should, if possible, contain the estimated time before the recovery of the service. The webmaster must also take care about the caching-related headers that are sent along with this response, as these temporary condition responses should usually not be cached.

* 504 Gateway Timeout - This error response is given when the server is acting as a gateway and cannot get a response in time.

* 505 HTTP Version Not Supported - The HTTP version used in the request is not supported by the server.

* 506 Variant Also Negotiates - The server has an internal configuration error: the chosen variant resource is configured to engage in transparent content negotiation itself, and is therefore not a proper end point in the negotiation process.

* 507 Insufficient Storage (WebDAV) - The method could not be performed on the resource because the server is unable to store the representation needed to successfully complete the request.

* 508 Loop Detected (WebDAV) - The server detected an infinite loop while processing the request.

* 510 Not Extended - Further extensions to the request are required for the server to fulfill it.

* 511 Network Authentication Required - Indicates that the client needs to authenticate to gain network access.