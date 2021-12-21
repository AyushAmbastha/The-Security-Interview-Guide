# DNS Exfiltration

DNS or Domain Name System is a protocol that is a pivotal service at the core of every network. But in the modern world, DNS faces challenges that it's original designers couldn't have even concieved of. It is estimated that upto 92% of malware leverages DNS as an attack mechanism. One of these mechanisms is the use of DNS as a pathway for Data Exfiltration. 

Let's say we have some sensitive data, such as credit card numbers or personal information. Now let's say one of the workstations in our environment is infected by malware that has access to this sensitive data. Having access is bad, but it becomes a much bigger problem if the malware can move the sensitive data out of the environment to where it can be exploited. To do this, the malware can try to send the data directly out, but chances are there is a firewall in place to prevent that. But because of the importance of DNS in network communications, and its need to reach external DNS servers to do its job, almost all firewalls have holes to allow DNS traffic. To take advantage of this, the malware packages the senstive data up as DNS queries and sends it to the local DNS server. The queries are designed so that the local DNS server can't directly respond and will therefore forward the query through the firewall to an external DNS server for an answer. 

For example, the credit card information such as "8478239820193456" would be encoded into "26856485f6476a567567c6576e678", and a domain would be appended to it -> "26856485f6476a567567c6576e678.badguy.com".

The external DNS server may or may not return an answer, but it will most certainly collect the information contained in the DNS query - this is the exfiltrated data. This external DNS server would be the server that the attacker has control over. The attacker can now take the encoded bits, decode them and put them together to get the sensitive data.

### Mitigation
* Implementing network inspection via security products where DNS traffic can be analyzed
* Limiting clients DNS traffic and creating rules triggered when a specific threshold is reached
* Setting-up dedicated DNS servers
* Creating network segmentation
* Blocking unauthorized channels