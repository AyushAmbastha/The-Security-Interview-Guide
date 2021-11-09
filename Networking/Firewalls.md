# Firewalls

A firewall is a network security perimeter device that inspects traffic entering and leaving the network. Depending on the security rules assigned specifically to it, the firewall either permits safe traffic or denies traffic it deems as dangerous.

A firewall’s main objective is to establish a barrier (or “wall”) that separates an internal network from incoming external traffic (such as the internet) for the purpose of blocking malicious network packets like malware and hacking.
When discussing firewalls, it is critical to clear up any confusion regarding what constitutes a firewall and what does not. For instance, intrusion detection systems, routers, proxy servers, VPNs and antivirus solutions are not firewalls. Many firewall architectures are built into other security solutions, and many security solutions are built into firewalls.

## How does firewall technology work? 

Firewalls carefully analyze incoming traffic arriving on a computer’s entry point, called a port, which determines how external devices communicate with each other and exchange information. Firewalls operate using specific firewall rules. A firewall rule will typically include a source address, a protocol, a port number and a destination address.
The way a firewall provides greater protection relies on the firewall itself and on the policies that are configured on it. 

The main firewall technologies available today are:

<ins>Hardware firewall </ins> - This is preferred when a firewall is required on more than one machine. It provides an additional layer of security to the physical network. The disadvantage of this approach is that if one firewall is compromised, all the machines that it serves are vulnerable.

<ins>Software firewall</ins> - This is a second layer of security and secures the network from malware, worms, viruses and email attachments. It looks like any other program and can be customized based on network requirements. Software firewalls can be customized to include antivirus programs and to block sites and images.

<ins>Packet-filter firewall</ins> - This filters at the network or transport layer. It provides network security by filtering network communications based on the information contained in the TCP/IP header of each packet. The firewall examines these headers and uses the information to decide whether to accept and route the packets along to their destinations or deny the packet by dropping them. This firewall type is a router that uses a filtering table to decide which packets must be discarded. Packer filtering makes decisions based upon the following header information:
- The source IP address
- The destination IP address
- The network protocol in use (TCP, ICMP or UDP)
- The TCP or UDP source port
- The TCP or UDP destination port
- If the protocol is ICMP, then its message type

<ins>Proxy firewall</ins> - The packet-filtering firewall is based on information available in the network and transport layer header. However, sometimes we need to filter a message based on the information available in the message itself (at the application layer). 
For example, assume that an organization only allows those users who have previously established business relations with the company, then access to other users must be blocked. In this case, a packet-filtering firewall is not feasible because it can’t distinguish between different packets arriving at TCP port 80.
Here, the proxy firewall came into light as a solution: install a proxy computer between the customer and the corporation computer. When the user client process sends a message, the proxy firewall runs a server process to receive the request. The server opens the packet at the application level and confirms whether the request is legitimate or not. If it is, the server acts as a client process and sends the message to the real server. Otherwise, the message is dropped. In this way, the requests of the external users are filtered based on the contents at the application layer.

<ins>Application gateways</ins> - These firewalls analyze the application level information to make decisions about whether or not to transmit the packets. Application gateways act as an intermediary for applications such as email, FTP, Telnet, HTTP and so on. An application gateway verifies the communication by asking for authentication to pass the packets. It can also perform conversion functions on data if necessary.
For example, an application gateway can be configured to restrict FTP commands to allow only get commands and deny put commands.
Application gateways can be used to protect vulnerable services on protected systems. A direct communication between the end user and destination service is not permitted. These are the common disadvantages when implementing application gateway:
- Slower performance
- Lack of transparency
- Need for proxies for each application
- Limits to application awareness

<ins>Circuit-level gateways</ins> - work at the session layer of the OSI model or the TCP layer of the TCP/IP model. It forwards data between the networks without verifying it. It blocks incoming packets on the host but allows the traffic to pass through itself. Information passed to remote computers through it appears to have originated from gateway. 
Circuit-level gateways operate by relaying TCP connections from the trusted network to the untrusted network. This means that a direct connection between the client and server never occurs.
The main advantage of a circuit-level gateway is that it provides services for many different protocols and can be adapted to serve an even greater variety of communications. A SOCK proxy is a typical implementation of circuit-level gateway.

<ins>Stateful packet inspection</ins> - SPI firewall permits and denies packets based on a set of rules very similar to that of a packet filter. However, when a firewall is state-aware, it makes access decisions not only on IP addresses and ports but also on the SYN, ACK, sequence numbers and other data contained in the TCP header. While packet filters can pass or deny individual packets and require permissive rules to permit two-way TCP communications, SPI firewalls track the state of each session and can dynamically open and close ports as specific sessions require.

## Firewall identification
Normally, firewalls can be identified for offensive purposes. Firewalls are usually a first line of defense in the virtual perimeter; to breach the network from a hacker perspective, it is required to identify which firewall technology is used and how it’s configured. Some popular tactics are:

<ins>Port scanning</ins> - 
Hackers use it for investigating the ports used by the victims.
Nmap is probably the most famous port-scanning tool available.

<ins>Firewalking</ins> - The process of using traceroute-like IP packet analysis in order to verify if a data packet will be passed through the firewall from source to host of the attacker to the destination host of the victim.

<ins>Banner grabbing</ins> - This is a technique to enable a hacker to spot the type of operation system or application running on a target server. It works through a firewall by using what looks like legitimate connections.
