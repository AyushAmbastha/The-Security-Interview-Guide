# DNS cache poisoning
Imagine that, as a senior-year prank, high school seniors change out all the room numbers on their high school campus, so that the new students who don't know the campus layout yet will spend the next day getting lost and showing up in the wrong classrooms. Now imagine that the mismatched room numbers get recorded in a campus directory, and students keep heading to the wrong rooms until someone finally notices and corrects the directory.

DNS cache poisoning is the act of entering false information into a DNS cache, so that DNS queries return an incorrect response and users are directed to the wrong websites. DNS cache poisoning is also known as 'DNS spoofing.' IP addresses are the 'room numbers' of the Internet, enabling web traffic to arrive in the right places. DNS resolver caches are the 'campus directory,' and when they store faulty information, traffic goes to the wrong places until the cached information is corrected. (Note that this does not actually disconnect the real websites from their real IP addresses.)

Because there is typically no way for DNS resolvers to verify the data in their caches, incorrect DNS information remains in the cache until the time to live (TTL) expires, or until it is removed manually. A number of vulnerabilities make DNS poisoning possible, but the chief problem is that DNS was built for a much smaller Internet and based on a principle of trust (much like BGP). A more secure DNS protocol called DNSSEC aims to solve some of these problems, but it has not been widely adopted yet.

## What do DNS resolvers do?
DNS resolvers provide clients with the IP address that is associated with a domain name. In other words, they take human-readable website addresses and translate them into machine-readable IP addresses. When a user attempts to navigate to a website, their operating system sends a request to a DNS resolver. The DNS resolver responds with the IP address, and the web browser takes this address and initiates loading the website.

## How does DNS caching work?
A DNS resolver will save responses to IP address queries for a certain amount of time. In this way, the resolver can respond to future queries much more quickly, without needing to communicate with the many servers involved in the typical DNS resolution process. DNS resolvers save responses in their cache for as long as the designated time to live (TTL) associated with that IP address allows them to.

## How do attackers poison DNS caches?
Attackers can poison DNS caches by impersonating DNS nameservers, making a request to a DNS resolver, and then forging the reply when the DNS resolver queries a nameserver. This is possible because DNS servers use UDP instead of TCP, and because currently there is no verification for DNS information.

DNS Cache Poisoning Process:
<p align="center">
  <img src="../images/dns-cache-poisoning.png" height = "300" width="500">
</p>

Poisoned DNS Cache:
<p align="center">
  <img src="../images/poisoned-cache.png" height = "300" width="350">
</p

Instead of using TCP, which requires both communicating parties to perform a 'handshake' to initiate communication and verify the identity of the devices, DNS requests and responses use UDP. With UDP, there is no guarantee that a connection is open, that the recipient is ready to receive, or that the sender is who they say they are. Thus, if a DNS resolver receives a forged response, it accepts and caches the data uncritically because there is no way to verify if the information is accurate and comes from a legitimate source. 

DNS was created in the early days of the Internet, when the only parties connected to it were universities and research centers. There was no reason to expect that anyone would try to spread fake DNS information. 
Despite these major points of vulnerability in the DNS caching process, DNS poisoning attacks are not easy. Because the DNS resolver does actually query the authoritative nameserver, attackers have only a few milliseconds to send the fake reply before the real reply from the authoritative nameserver arrives.

Attackers also have to either know or guess a number of factors to carry out DNS spoofing attacks:

* Which DNS queries are not cached by the targeted DNS resolver, so that the resolver will query the authoritative nameserver
* What port the DNS resolver is using – they used to use the same port for every query, but now they use a different, random port each time
* The request ID number
* Which authoritative nameserver the query will go to
Attackers could also gain access to the DNS resolver in some other way. If a malicious party operates, hacks, or gains physical access to a DNS resolver, they can more easily alter cached data.

## DNS spoofing and censorship
Several governments have intentionally poisoned DNS caches within their countries in order to deny access to certain websites or web resources.

## How will DNSSEC help prevent DNS poisoning?
DNSSEC is short for Domain Name System Security Extensions, and it is a means of verifying DNS data integrity and origin. DNS was originally designed with no such verification, which is why DNS poisoning is possible.

Much like TLS/SSL, DNSSEC uses public key cryptography (a way of digitally signing information) to verify and authenticate data. DNSSEC extensions were published in 2005, but DNSSEC is not yet mainstream, leaving DNS still vulnerable to attacks.