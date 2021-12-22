# MAC Filtering

All computers use a piece of hardware called a network interface controller (also called a network card) to connect to all networks, local and wide. A Media Access Control (MAC) address is a unique identifier assigned to each network card — and by extension, the PC to which it belongs — in a computer network. 

A MAC address is formatted as a series of 12 hexadecimal digits arranged as “00-00-00-00-00-00-00.”

Access rights to a network can be managed easily using these MAC addresses. Any PC whose MAC address is on a whitelist is allowed access to the network ports, while those on blacklists are denied access or blocked. This process is called MAC filtering.

If the PC has both Ethernet and Wi-Fi capabilities, that means that it has two separate adapters — one wired and the other wireless. If virtualization software is being used, there can be even more! Since MAC addresses are tied to network cards and not their PCs, it is quite common to see one PC host multiple MAC addresses.

## How MAC filtering is useful
A MAC address is like a government ID or Social Security number given to citizens. It is a permanent address for a device in a network that doesn’t change under normal circumstances, ever. In contrast, IP addresses of network devices are constantly changing unless they are set as “static” by the system administrator. 

Thus, a MAC address gives the network admins a reliable address to keep track of known devices within the system. They are an effective form of enforcing access control.

In personal and home networks, MAC filtering is less useful unless there are multiple networks and many users/devices involved. The best use case for MAC filtering is often in an enterprise or institutional setting. In large, complex networks with multiple gateways and access points, administrators can use MAC filtering to restrict user access to specific networks. It largely serves as an organizational or administrative purpose.

## Disadvantages of MAC filtering
MAC filtering is a useful network administration tool with limited security potential. It can be used as an extra layer of protection above the basic layers like WPA2-AES security protocols. But as a standalone security measure, it is woefully inadequate. 

It is only effective if the hacker does not have access to either of the two pieces of information:

1. The MAC address whitelist of the network
2. At least one of the MAC addresses of a device connected to the network (in case of a blacklisted MAC filtering system)
   
If a hacker can gain access to a MAC address that has access to the network, they can masquerade as that device and compromise the network security. And they can easily find the MAC addresses by monitoring the network traffic using toolsets like Kali Linux and Wireshark. This is useful to a hacker because they can use a technique called “spoofing” to easily change the MAC address of their device. Even ordinary users with admin access to a Windows PC can change its MAC addresses.