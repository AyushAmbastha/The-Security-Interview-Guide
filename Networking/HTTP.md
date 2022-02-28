# Hypertext Transfer Protocol (HTTP)

The Hypertext Transfer Protocol (HTTP) is the foundation of the World Wide Web, and is used to load web pages using hypertext links. HTTP is an application layer protocol designed to transfer information between networked devices and runs on top of other layers of the network protocol stack. A typical flow over HTTP involves a client machine making a request to a server, which then sends a response message.

## What’s in an HTTP request?
An HTTP request is the way internet communications platforms such as web browsers ask for the information they need to load a website. Each HTTP request made across the Internet carries with it a series of encoded data that carries different types of information. A typical HTTP request contains:
- HTTP version type
- a URL
- an HTTP method
- HTTP request headers
- Optional HTTP body

### What’s an HTTP method?
An HTTP method, sometimes referred to as an HTTP verb, indicates the action that the HTTP request expects from the queried server. For example, two of the most common HTTP methods are ‘GET’ and ‘POST’; a ‘GET’ request expects information back in return (usually in the form of a website), while a ‘POST’ request typically indicates that the client is submitting information to the web server (such as form information, e.g. a submitted username and password).

### What are HTTP request headers?
HTTP headers contain text information stored in key-value pairs, and they are included in every HTTP request and response. These headers communicate core information, such as what browser the client is using what data is being requested.

### What’s in an HTTP request body?
The body of a request is the part that contains the ‘body’ of information the request is transferring. The body of an HTTP request contains any information being submitted to the web server, such as a username and password, or any other data entered into a form.

## What’s in an HTTP response?
An HTTP response is what web clients (often browsers) receive from an Internet server in answer to an HTTP request. These responses communicate valuable information based on what was asked for in the HTTP request.

A typical HTTP response contains:
- an HTTP status code
- HTTP response headers
- optional HTTP body

### What’s an HTTP status code?
HTTP status codes are 3-digit codes most often used to indicate whether an HTTP request has been successfully completed. Status codes are broken into the following 5 blocks:
- 1xx Informational
- 2xx Success
- 3xx Redirection
- 4xx Client Error
- 5xx Server Error

The “xx” refers to different numbers between 00 and 99.

Status codes starting with the number ‘2’ indicate a success. For example, after a client requests a web page, the most commonly seen responses have a status code of ‘200 OK’, indicating that the request was properly completed.

If the response starts with a ‘4’ or a ‘5’ that means there was an error and the webpage will not be displayed. A status code that begins with a ‘4’ indicates a client-side error (It’s very common to encounter a ‘404 NOT FOUND’ status code when making a typo in a URL). A status code beginning in ‘5’ means something went wrong on the server side. Status codes can also begin with a ‘1’ or a ‘3’, which indicate an informational response and a redirect, respectively.

### What are HTTP response headers?
Much like an HTTP request, an HTTP response comes with headers that convey important information such as the language and format of the data being sent in the response body.

### What’s in an HTTP response body?
Successful HTTP responses to ‘GET’ requests generally have a body which contains the requested information. In most web requests, this is HTML data which a web browser will translate into a web page.

## Can DDoS attacks be launched over HTTP?
Keep in mind that HTTP is a “stateless” protocol, which means that each command runs independent of any other command. In the original spec, HTTP requests each created and closed a TCP connection. In newer versions of the HTTP protocol (HTTP 1.1 and above), persistent connection allows for multiple HTTP requests to pass over a persistent TCP connection, improving resource consumption. In the context of DoS or DDoS attacks, HTTP requests in large quantities can be used to mount an attack on a target device, and are considered part of application layer attacks or layer 7 attacks.