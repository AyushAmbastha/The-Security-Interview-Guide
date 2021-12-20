# Cryptographic Failures

## Description

Previously known as Sensitive Data Exposure, Cryptographic Failures deals with the protection of data at rest and in transit. This type of flaw occurs when an application or a company inadvertently exposes 
sensitive data. It's different from a data breach in the sense that in a data breach, the attacker steals 
information from the database whereas a Cryptographic Failure occurs when the data is not adequently 
protected. It can be the result of weak encryption, software flaws, storing passwords without hashes etc. 
Also, if the data falls under any privacy laws such as GDPR or PCI DSS (TODO), there are additional things 
to consider while deciding the protection mechanisms to use.

## Example Attack Scenarios

<ins>Scenario 1: Data at Rest</ins>

An application stores passwords without salts, which means that the password can be easily decrypted. 
A directory browsing flaw allows the attacker to retrieve the passwords stored in the system. 
All the unsalted hashes can be exposed with a rainbow table of pre-calculated hashes. 

Additionally, even if the system used salts to store the passwords but used simple/fast hash functions, 
they can be cracked by most GPUs. 

To read more on how passwords should be stored and used, read this (TODO).

<ins>Scenario 1: Data in Transit</ins>

A website doesn't enforce TLS on all pages. The attacker can not only monitor the network traffic but 
also alter them, causing a man-in-the-middle attack (TODO).

The attacker can also hijack the user session by stealing the user's session cookie and replaying it to 
the server to impersonate the user. He can then view and modify sensitive information.