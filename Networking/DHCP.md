# Dynamic Host Configuration Protocol

DHCP is a network management protocol that can dynamically assign an IP address to a new machine added to the network so they can connect using IP (Internet Protocol). The protocol provides:

1. Subnet Mask
2. Router Address and
3. IP Address
   
DHCP is based on a client-server model. DHCP port number for server is 67 and for the client is 68. It is a Client server protocol which uses UDP services.  IP address is assigned from a pool of addresses. In DHCP, the client and the server exchange mainly 4 DHCP messages in order to make a connection, also called DORA process - Discovery, Offer, Request, and ACK, but there are 8 DHCP messages in the process.

<ins>DHCP discover message </ins>
- First message generated in the communication process between server and client.
- Generated by Client host in order to discover if there is any DHCP server/servers are present in a network or not. 
- Broadcasted to all devices present in a network to find the DHCP server. 
- 342 or 576 bytes long
- Sender IP(Client) - 0.0.0.0, Reciever IP: 255.255.255.255 (Broadcast)

<ins>DHCP offer message</ins>
- The server will respond to host in this message specifying the unleased IP address and other TCP configuration information. 
- This message is broadcasted by server. 
- Size of message is 342 bytes. 
- If there are more than one DHCP servers present in the network then client host will accept the first DHCP OFFER message it receives. 
- The server ID is specified in the packet in order to identify the server.
- Sender IP(DHCP server) - 192.168.1.1, Reciever IP: 255.255.255.255 (Broadcast)
- Also the server has provided the offered IP address 192.162.1.3 and lease time of 3600 seconds

<ins>DHCP request message<ins>
- When a client receives a offer message, it broadcasts an ARP in order to find if there is any other host present in the network with same IP address. If there is no reply by other host, then there is no host with same TCP configuration in the network.
- After this ARP request broadcast, the client broadcasts the DHCP request message for the server showing the acceptance of IP address. A Client ID is also added in this message.
- Sender IP(Client) - 0.0.0.0, Reciever IP: 255.255.255.255 (Broadcast)

<ins>DHCP acknowledgement message</ins>
- In response to the request message received, the server will make an entry with specified client ID and bind the IP address offered with lease time. Now, the client will have the IP address provided by server.
- This IP address will not be provided by server to any other machine in the future.
- Sender IP(DHCP server) - 192.168.1.1, Reciever IP: 255.255.255.255 (Broadcast)

## Security Issues with DHCP

If attackers are able to compromise a DHCP server on the network, they might disrupt network services, preventing DHCP clients from connecting to network resources. By gaining control of a DHCP server, attackers can configure DHCP clients with fraudulent TCP/IP configuration information, including an invalid default gateway or Domain Name System (DNS) server configuration.

The following threats exist when you implement DHCP on your network:

- Unauthorized DHCP servers can issue incorrect TCP/IP configuration information to DHCP clients.

- DHCP servers can overwrite valid DNS resource records with incorrect information.

- DHCP can create DNS resource records without ownership defined.

- Unauthorized DHCP clients can obtain IP addresses

## DHCP Starvation Attack
In a DHCP Starvation attack, the attacker sends a ton of bogus DISCOVER packets until the DHCP server thinks they've expended their available pool. Clients looking for IP addresses find that there are no IP addresses for them, and they're denied service. Additionally, they may look for a different DHCP server, one which the attacker may provide. And using a hostile or dummy IP address, the attacker can now read all the traffic that client sends and receives (man-in-the-middle attack).

## Mitigation against DHCP Starvation Attacks
DHCP starvation attacks are a real and present danger for a network. Understanding how a hostile actor dupes a DHCP server with bogus DISCOVER packets and overwhelms it from being able to supply legitimate clients with IP addresses is key to preventing such attacks and keeping your network secure. To help mitigate this type of attack, there's an approach called port security.