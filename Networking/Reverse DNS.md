# Reverse DNS

A reverse DNS lookup is a DNS query for the domain name associated with a given IP address. This accomplishes the opposite of the more commonly used forward DNS lookup, in which the DNS system is queried to return an IP address.
As reverse lookups are not critical to the normal function of the Internet, they are not a hard requirement. As such, reverse DNS lookups are not universally adopted.

## How does reverse DNS work?
Reverse DNS lookups query DNS servers for a PTR (pointer) record; if the server does not have a PTR record, it cannot resolve a reverse lookup. PTR records store IP addresses with their segments reversed, and they append ".in-addr.arpa" to that. For example if a domain has an IP address of 192.0.2.1, the PTR record will store the domain's information under 1.2.0.192.in-addr.arpa.

In IPv6, the latest version of the Internet Protocol, PTR records are stored within the ".ip6.arpa" domain instead of ".in-addr.arpa."

## What is a DNS PTR record?
DNS correlates domain names with IP addresses. A DNS pointer record (PTR for short) provides the domain name associated with an IP address. A DNS PTR record is exactly the opposite of the 'A' record, which provides the IP address associated with a domain name.

DNS PTR records are used in reverse DNS lookups - a query that starts with the IP address and looks up the domain name.

## How are DNS PTR records stored?
In IPv4:

While DNS A records are stored under the given domain name, DNS PTR records are stored under the IP address — reversed, and with ".in-addr.arpa" added. For example, the PTR record for the IP address 192.0.2.255 would be stored under "255.2.0.192.in-addr.arpa".

"in-addr.arpa" has to be added because PTR records are stored within the .arpa top-level domain in the DNS. .arpa is a domain used mostly for managing network infrastructure, and it was the first top-level domain name defined for the Internet. 
in-addr.arpa is the namespace within .arpa for reverse DNS lookups in IPv4.

In IPv6:

IPv6 PTR records exist in a different namespace within .arpa. IPv6 PTR records are stored under the IPv6 address, reversed and converted into four-bit sections (as opposed to 8-bit sections, as in IPv4), plus ".ip6.arpa".

## What are reverse DNS lookups and PTR records used for?
PTR records are used in reverse DNS lookups; common uses for reverse DNS include:

* Anti-spam: Some email anti-spam filters use reverse DNS to check the domain names of email addresses and see if the associated IP addresses are likely to be used by legitimate email servers. Many email servers will reject messages from any server that does not support reverse lookups or from a server that is highly unlikely to be legitimate. Spammers often use IP addresses from hijacked machines, which means there will be no PTR record. Or, they may use dynamically assigned IP addresses that lead to server domains with highly generic names.

* Troubleshooting email delivery issues: Because anti-spam filters perform these checks, email delivery problems can result from a misconfigured or missing PTR record. If a domain has no PTR record, or if the PTR record contains the wrong domain, email services may block all emails from that domain.

* Logging: System logs typically record only IP addresses; a reverse DNS lookup can convert these into domain names for logs that are more human-readable.