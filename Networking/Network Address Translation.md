# Network Address Translation (NAT)

Network Address Translation is a way to map multiple local private addresses to a public one before transferring the information. Organizations that want multiple devices to employ a single IP address use NAT, as do most home routers. It is used by a device (firewall, router or computer) that sits between an internal network and the rest of the world. 

## How Does NAT Work?

Let’s say there is a laptop connected to a home router. Someone uses the laptop to search for directions to their favorite restaurant. The laptop sends this request in a packet to the router, which passes it along to the web. But first, the router changes the outgoing IP address from a private local address to a public address.

If the packet keeps a private address, the receiving server won’t know where to send the information back to — this is akin to sending physical mail and requesting return service but providing a return address of anonymous. By using NAT, the information will make it back to the laptop using the router’s public address, not the laptop’s private one.

## NAT Types

NAT has many forms and can work in several ways:

<ins>Static NAT</ins> - Mapping an unregistered IP address to a registered IP address on a one-to-one basis. This means there will be a consistent public IP address associated with that router or NAT device. Particularly useful when a device needs to be accessible from outside the network.

<ins>Dynamic NAT</ins> - Maps an unregistered IP address to a registered IP address from a group of registered IP addresses. Instead of choosing the same IP address every time, this NAT goes through a pool of public IP addresses. This results in the router or NAT device getting a different address each time the router translates the local address to a public address.

<ins>Overloading</ins> - A form of dynamic NAT that maps multiple unregistered IP addresses to a single registered IP address by using different ports. This is known also as PAT (Port Address Translation), single address NAT or port-level multiplexed NAT.

<ins>Overlapping</ins> - When the IP addresses used on your internal network are registered IP addresses in use on another network, the router must maintain a lookup table of these addresses so that it can intercept them and replace them with registered unique IP addresses. It is important to note that the NAT router must translate the "internal" addresses to registered unique addresses as well as translate the "external" registered addresses to addresses that are unique to the private network. This can be done either through static NAT or by using DNS and implementing dynamic NAT.

The internal network is usually a LAN (Local Area Network), commonly referred to as the stub domain. A stub domain is a LAN that uses IP addresses internally. Most of the network traffic in a stub domain is local, so it doesn't travel outside the internal network. A stub domain can include both registered and unregistered IP addresses. Of course, any computers that use unregistered IP addresses must use Network Address Translation to communicate with the rest of the world.

## Why Use NAT?

<ins>IP Conservation </ins> 

IP addresses identify each device connected to the internet. The existing IP version 4 (IPv4) uses 32-bit numbered IP addresses, which allows for 4 billion possible IP addresses, which seemed more than enough when it launched in the 1970s.

However, the internet has exploded, and while not all 7 billion people on the planet access the internet regularly, those that do often have multiple connected devices: phones, personal desktop, work laptop, tablet, TV, even refrigerators.

Therefore, the number of devices accessing the internet far surpasses the number of IP addresses available. Routing all of these devices via one connection using NAT helps to consolidate multiple private IP addresses into one public IP address. This helps to keep more public IP addresses available even while private IP addresses proliferate.

IP version 6 (IPv6) was officially launched in 2012 to accommodate the need for more IP addresses. IPv6 uses 128-bit numbered IP addresses, which allow for exponentially more potential IP addresses. It will take many years before this process finishes; so until then, NAT will be a valuable tool.

<ins>NAT Security</ins>

Additionally, NAT provides security and privacy. Because NAT transfers packets of data from public to private addresses, it also prevents anything else from accessing the private device. The router sorts the data to ensure everything goes to the right place, making it more difficult for unwanted data to get by. It’s not foolproof, but it often acts as the first means of defense for your device. 
NAT also allows you to display a public IP address while on a local network, helping to keep data and user history private.