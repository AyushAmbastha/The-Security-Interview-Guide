# Border Gateway Protocol

Border Gateway Protocol (BGP) is the routing protocol of the Internet. When someone submits data via the Internet, BGP is responsible for looking at all of the available paths that data could travel and picking the best route, which usually means hopping between autonomous systems. Thus, BGP is a standardized exterior gateway protocol designed to exchange routing and reachability information among autonomous systems (AS) on the Internet.

BGP used for routing within an autonomous system is called Interior Border Gateway Protocol, Internal BGP (iBGP). In contrast, the Internet application of the protocol is called Exterior Border Gateway Protocol, External BGP (eBGP).

Each BGP router stores a routing table with the best routes between autonomous systems. These are updated almost continually as each AS – often an Internet service provider (ISP) – broadcasts new IP prefixes that they own. BGP always favors the shortest and most direct path from AS to AS in order to reach IP addresses via the fewest possible hops across networks.

**Autonomous System** - An autonomous system is a large network or group of networks managed by a single organization. An AS may have many subnetworks, but all share the same routing policy. Usually an AS is either an ISP or a very large organization with its own network and multiple upstream connections from that network to ISPs (this is called a 'multihomed network'). Each AS is assigned its own Autonomous System Number, or ASN, to identify them easily. 

## BGP Hijacking
BGP hijacking is when attackers maliciously reroute Internet traffic. Attackers accomplish this by falsely announcing ownership of groups of IP addresses, called IP prefixes, that they do not actually own, control, or route to. This announcement, if not filtered, can spread and be added to routing tables in BGP routers across the Internet. From then until somebody notices and corrects the routes, traffic to those IPs will be routed to that Attacker AS.

BGP always favors the shortest, most specific path to the desired IP address. In order for the BGP hijack to be successful, the route announcement must either:
1) Offer a more specific route by announcing a smaller range of IP addresses than other ASes had previously announced.
2) Offer a shorter route to certain blocks of IP addresses. Additionally, not just anyone can announce BGP routes to the larger Internet. In order for a BGP hijack to occur, the announcement must be made by the operator of an AS, or by a threat actor who has compromised an AS (the second case is more rare).

There have been many real-world examples of deliberate BGP hijacking. In April 2018, a Russian provider announced a number of IP prefixes (groups of IP addresses) that actually belong to Route53 Amazon DNS servers. In short, the end result was that users attempting to log in to a cryptocurrency site were redirected to a fake version of the website controlled by hackers. The hackers were thus able to steal approximately $152,000 in cryptocurrency. 

In 2008, the Pakistani government-owned Pakistan Telecom attempted to censor Youtube within Pakistan by updating its BGP routes for the website. Seemingly on accident, the new routes were announced to Pakistan Telecom's upstream providers, and from there broadcast to the whole Internet. Suddenly, all web requests for Youtube were directed to Pakistan Telecom, resulting in an hours-long outage of the website for almost the entire Internet, and overwhelming the ISP.

Incidents like these can happen because the route-sharing function of BGP relies on trust, and autonomous systems implicitly trust the routes that are shared with them. When peers announce incorrect route information (intentionally or not), traffic goes where it is not supposed to, potentially with malicious results.

Fortunately, some progress has been made in securing BGP. Most notably, a security framework for routing called Resource Public Key Infrastructure (RPKI) was introduced in 2008. RPKI uses cryptographically signed records called Route Origin Authorization (ROAs) to validate which network operator is allowed to announce an organization’s IP addresses using BGP. This ensures that only authorized parties are announcing an organization’s prefixes.

### Preventing BGP Hijacks
Aside from constant monitoring of how Internet traffic is routed, users and networks can do very little to prevent BGP hijacks.

- IP prefix filtering is one method where networks should only accept IP prefix declarations if necessary, and should only declare their IP prefixes to certain networks, not the entire Internet. Doing so helps prevent accidental route hijacking and could keep the AS from accepting bogus IP prefix declarations; however, in practice this is difficult to enforce.

### BGP hijacking detection
Increased latency, degraded network performance, and misdirected Internet traffic are all possible signs of a BGP hijack. Many larger networks will monitor BGP updates to ensure their clients do not face latency issues, and a few security researchers do in fact monitor Internet traffic and publish their findings.