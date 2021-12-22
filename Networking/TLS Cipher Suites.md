# TLS Cipher Suites

Cipher suites are sets of instructions that enable secure network connections through Transport Layer Security (TLS). Behind the scenes, these cipher suites provide a set of algorithms and protocols required to secure communications between clients and servers. Cipher suites are required because of the variety of servers, operating systems and browsers. There needs to be a way to accommodate all these combinations, so cipher suites come in handy to ensure compatibility.

To initiate an HTTPS connection, the two parties – the web server and the client – perform an SSL handshake. During the handshake process the two parties agree on a mutual cipher suite. The cipher suite is then used to negotiate a secure HTTPS connection. A cipher suite consists of - 

1. A **key exchange algorithm**, to determine how symmetric keys will be exchanged.
2. An **authentication** or **digital signature algorithm**, which dictates how server authentication and client authentication (if required) will be implemented.
3. A **bulk encryption cipher**, which is used to encrypt the data.
4. A **hash/MAC function**, which determines how data integrity checks will be carried out.

The decision on which cipher suite will be used depends on the web server. The agreed cipher suite is a combination of:

- Key exchange algorithms, such as RSA, DH, ECDH, DHE, ECDHE, or PSK.
- Authentication/Digital Signature Algorithm, like RSA, ECDSA, or DSA.
- Bulk encryption algorithms, like AES, CHACHA20, Camellia, or ARIA.
- Message Authentication Code algorithms, such as SHA-256, and POLY1305.

An example of a Cipher Suite -

<p align="center">
  <img src="../images/cipher.png" width="400">
</p>

Starting from left to right, ECDHE determines that during the handshake the keys will be exchanged via ephemeral Elliptic Curve Diffie Hellman (ECDHE). ECDSA or Elliptic Curve Digital Signature Algorithm is the authentication algorithm. AES128-GCM is the bulk encryption algorithm: AES running Galois Counter Mode with 128-bit key size. Finally, SHA-256 is the hashing algorithm.

## Why are cipher suites important?
Cipher suites are important for ensuring the security, compatibility, and performance of HTTPS connections.

As mentioned before, it is the web server that finally determines which cipher suite will be used. Therefore, the prioritized list of cipher suites on the web server is very important. Choosing the correct ciphers to be listed on any web server is a vital exercise for any administrator and it is largely determined by the type of users connecting to the server and the technology they are using.

Users are also responsible for ensuring secure connections. Since browser vendors update their list of supported cipher suites after a vulnerability is discovered, users must install the latest browser patches to reduce the likelihood of encountering compatibility issues when weak cipher suites are deprecated on the server side.

## Supported cipher suites in TLS 1.2
All TLS protocols prior to TLS 1.2 (i.e. TLS 1.0 and TLS 1.1) have been deprecated for various security reasons. Currently, the only acceptable TLS protocols are TLS 1.2 and TLS 1.3.

Starting with TLS 1.2, the protocol supports 37 different cipher suites. Of all the supported cipher suites in TLS 1.2, it is advised that we use the ones with ephemeral Diffie-Hellman algorithm. So, the advisable cipher suites are down to the following:

TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256\
TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384\
TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256\
TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384\
TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256\
TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384\
TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256\
TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384\
TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256\
TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384\
TLS_DHE_RSA_WITH_AES_128_GCM_SHA256\
TLS_DHE_RSA_WITH_AES_256_GCM_SHA384\
TLS_DHE_RSA_WITH_AES_128_CBC_SHA\
TLS_DHE_RSA_WITH_AES_256_CBC_SHA\
TLS_DHE_RSA_WITH_AES_128_CBC_SHA256\
TLS_DHE_RSA_WITH_AES_256_CBC_SHA256\
TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256\
TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305\
TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256\
TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305\

## Identifying weak ciphers
With the introduction of TLS 1.3, many things changed to improve the security of the protocol. To start with, old, insecure ciphers have been deprecated, including:

RC4\
DSA\
MD5\
SHA-1\
Weak Elliptic Curves\
RSA Key Exchange\
Static Diffie-Hellman (DH, ECDH)\
Block ciphers (CBC)\
Non-AEAD ciphers\

## Support cipher suites in TLS 1.3
In addition, TLS 1.3 cipher suites are now much shorter than the respective TLS 1.2 suites. The cipher suites do not list the type of certificate – either RSA or ECDSA – and the key exchange mechanism – DHE or ECDHE. Therefore, the number of negotiations required to determine the encryption parameters has been reduced from four to two. Cipher suites in TLS 1.3 look like this:

<p align="center">
  <img src="../images/cipher2.png" width="400">
</p>

The client initiates the handshake knowing that Ephemeral Diffie-Hellman algorithm will be used for the key exchange process, and it can send its portion of the key share during the Client Hello message. The benefit of it is that the TLS 1.3 handshake is shortened down to a single roundtrip, where the server responds with all the required information for the two parties to derive the session key and begin communicating securely.

The supported cipher suites in TLS 1.3 have now dropped to just five and are the following:

TLS_AES_256_GCM_SHA384\
TLS_CHACHA20_POLY1305_SHA256\
TLS_AES_128_GCM_SHA256\
TLS_AES_128_CCM_8_SHA256\
TLS_AES_128_CCM_SHA256\

## Choosing cipher suites
TLS 1.3 cipher suites are not interoperable with older TLS versions, because their structure is different. This means that site administrators will need to configure their web servers in such a way to allow compatibility with both versions of supported cipher suites, TLS 1.2 and TLS 1.3. Opting for support of only TLS 1.3 is not a wise solution, because a lot of companies rely still on TLS 1.2.