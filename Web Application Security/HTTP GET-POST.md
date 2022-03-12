# HTTP GET vs.POST

HTTP GET is not encrypted, it can be intercepted by a network sniffer, by a proxy or leaked in the logs of the server with a customised logging level. GET is somehow less secure than POST when transmitted over the wire. The major security issues with GET are -
- The data will be seen in the address bar of a browser and recorded in the browser history.
- The URL (including query parameters) are logged on the server.

Is a POST secure enough to send login credentials over? No! SSL is a must. 
HTTP POST is not encrypted as well. It can be intercepted by a network sniffer or by a proxy. Yes, POST is better than GET because POST data is not usually logged by a proxy or server, but it is not secure. 

To secure a password or other confidential data you must use SSL or encrypt the data before you use GET or POST. SSL will cover the whole HTTP communication and encrypt the HTTP data being transmitted between the client and the server.

The only difference between HTTP GET and HTTP POST is the manner in which the data is encoded. In both cases it is sent as plain-text. In order to provide any sort of security for login credentials, HTTPS is a must. 