# Address Resolution Protocol (ARP)

Address Resolution Protocol (ARP) is a protocol or procedure that connects an IP address to a fixed physical machine address, also known as a media access control (MAC) address, in a local-area network (LAN). 

The ARP works between the Network Layer (responsible for forwarding packets of data through different routers) and the Data Link layer (establishes and terminates a connection between two physically connected devices) in the OSI model. 
The Data link layer requires MAC addresses for the physical communication, and the Network layer uses IP addresses.

Without ARP, a host would not be able to figure out the hardware address of another host. The LAN keeps a table or directory that maps IP addresses to MAC addresses of the different devices, including both endpoints and routers on that network. This table or directory is not maintained by users or even by IT administrators. Instead, the ARP protocol creates entries on the fly. If a user's device does not know the hardware address of the destination host, the device will send a message to every host on the network asking for this address. When the proper destination host learns of the request, it will reply back with its hardware address, which will then be stored in the ARP directory or table.  If ARP is not supported, manual entries can be made to this directory. 

## What Does ARP Do and How Does It Work?
When a new computer joins a local area network (LAN), it will receive a unique IP address to use for identification and communication. 

Packets of data arrive at a gateway, destined for a particular host machine. The gateway, or the piece of hardware on a network that allows data to flow from one network to another, asks the ARP program to find a MAC address that matches the IP address. The ARP cache keeps a list of each IP address and its matching MAC address. The ARP cache is dynamic, but users on a network can also configure a static ARP table containing IP addresses and MAC addresses.

ARP caches are kept on all operating systems in an IPv4 Ethernet network. Every time a device requests a MAC address to send data to another device connected to the LAN, the device verifies its ARP cache to see if the IP-to-MAC-address connection has already been completed. If it exists, then a new request is unnecessary. However, if the translation has not yet been carried out, then the request for network addresses is sent, and ARP is performed.

An ARP cache size is limited by design, and addresses tend to stay in the cache for only a few minutes. It is purged regularly to free up space. This design is also intended for privacy and security to prevent IP addresses from being stolen or spoofed by cyberattackers. While MAC addresses are fixed, IP addresses are constantly updated.

In the purging process, unutilized addresses are deleted; so is any data related to unsuccessful attempts to communicate with computers not connected to the network or that are not even powered on.

## What Are the Types of ARP?
There are different versions and use cases of ARP. Let us take a look at a few.

### Proxy ARP
Proxy ARP is a technique by which a proxy device on a given network answers the ARP request for an IP address that is not on that network. The proxy is aware of the location of the traffic's destination and offers its own MAC address as the destination. 

### Gratuitous ARP
Gratuitous ARP is almost like an administrative procedure, carried out as a way for a host on a network to simply announce or update its IP-to-MAC address. Gratuitous ARP is not prompted by an ARP request to translate an IP address to a MAC address.

### Reverse ARP (RARP)
Host machines that do not know their own IP address can use the Reverse Address Resolution Protocol (RARP) for discovery.

### Inverse ARP (IARP)
Whereas ARP uses an IP address to find a MAC address, IARP uses a MAC address to find an IP address.

## ARP Spoofing/ARP Poisoning Attack
An ARP spoofing, also known as ARP poisoning, is a Man in the Middle (MitM) attack that allows attackers to intercept communication between network devices. The attack works as follows:

1. The attacker must have access to the network. They scan the network to determine the IP addresses of at least two devices⁠—let’s say these are a workstation and a router. 
2. The attacker uses a spoofing tool, such as Arpspoof or Driftnet, to send out forged ARP responses. 
3. The forged responses advertise that the correct MAC address for both IP addresses, belonging to the router and workstation, is the attacker’s MAC address. This fools both router and workstation to connect to the attacker’s machine, instead of to each other.
4. The two devices update their ARP cache entries and from that point onwards, communicate with the attacker instead of directly with each other.
5. The attacker is now secretly in the middle of all communications.

The ARP spoofing attacker pretends to be both sides of a network communication channel

Once the attacker succeeds in an ARP spoofing attack, they can:
* Continue routing the communications as-is⁠—the attacker can sniff the packets and steal data, except if it is transferred over an encrypted channel like HTTPS. 
* Perform session hijacking⁠—if the attacker obtains a session ID, they can gain access to accounts the user is currently logged into.
* Alter communication⁠—for example pushing a malicious file or website to the workstation.
* Distributed Denial of Service (DDoS)⁠ - the attackers can provide the MAC address of a server they wish to attack with DDoS, instead of their own machine. If they do this for a large number of IPs, the target server will be bombarded with traffic.

### Mitigation - 

* Use a Virtual Private Network (VPN)⁠ - a VPN allows devices to connect to the Internet through an encrypted tunnel. This makes all communication encrypted, and worthless for an ARP spoofing attacker.
* Use static ARP⁠ - the ARP protocol lets you define a static ARP entry for an IP address, and prevent devices from listening on ARP responses for that address. For example, if a workstation always connects to the same router, you can define a static ARP entry for that router, preventing an attack.
* Use packet filtering⁠ - packet filtering solutions can identify poisoned ARP packets by seeing that they contain conflicting source information, and stop them before they reach devices on your network.
* Run a spoofing attack⁠ - check if your existing defenses are working by mounting a spoofing attack, in coordination with IT and security teams. If the attack succeeds, identify weak points in your defensive measures and remediate them.