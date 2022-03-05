# Classful IP addressing
Classful addressing divides the IPv4 address space (0.0.0.0-255.255.255.255) into 5 classes: A, B, C, D, and E. However, only A, B, and C are used for network hosts. Class D, which covers the 224.0.0.0-239.255.255.255 IP address range, is reserved for multicasting, and class E (240.0.0.0-255.255.255.255) is reserved for “future use.”

The table below details the default network mask (subnet mask), IP address ranges, number of networks, and number of addresses per network of each address class.

| IPv4 address class | Network Mask |	Number of IPv4 Networks | Number of IPv4 addresses per network | IPv4 address range |
|-----|-----|-----|------|-------|
| A	| 255.0.0.0	| 128 | 16,777,216|	0.0.0.0 - 127.255.255.255 |
| B	| 255.255.0.0 |	16,384 | 65,536 | 128.0.0.0 - 191.255.255.255 |
| C | 255.255.255.0 | 2,097,152 | 256 | 192.0.0.0 - 223.255.255.255 |

As we can see, Class A continues to use the first 8-bits of an address, and may be suitable for very large networks. Class B is for networks much smaller than Class A, but still large in their own right. Class C addresses are suitable for small networks.

Classful IP addressing wasn’t enough to keep up with growth of the internet. As internet popularity continued to surge past 1981, it became clear that allocating blocks of 16,777,216, 65,536, or 256 addresses simply wasn’t sustainable. Addresses were being wasted in too-large blocks, and it was clear there’d be a tipping point where we ran out of IP address space altogether.

One of the best ways to understand why this was a problem is to consider an organization that needed a network just slightly bigger than a Class C. For example, suppose our example organization needs 500 IP addresses. Going up to a Class B network means wasting 65,034 addresses (65,534 usable Class B host addresses minus 500). Similarly, if it needed just 2 public IP addresses, a Class C would waste 252 (254 usable addresses – 2). Any way you look at it, IP addresses under the IPv4 protocol were running out, either through waste or the upper limits of the system.

# Classless Inter-Domain Routing

Classless Inter-Domain Routing (CIDR) is a method for allocating IP addresses and for IP routing that tackles the problem of wastage of IP addresses. Its goal was to slow the growth of routing tables on routers across the Internet, and to help slow the rapid exhaustion of IPv4 addresses.

Whereas classful network design for IPv4 sized the network prefix as one or more 8-bit groups, resulting in the blocks of Class A, B, or C addresses, under CIDR address space is allocated to Internet service providers and end users on any address-bit boundary. In IPv6, however, the interface identifier has a fixed size of 64 bits by convention, and smaller subnets are never allocated to end users.

CIDR is based on variable-length subnet masking (VLSM) which allows the specification of arbitrary-length prefixes. CIDR introduced a new method of representation for IP addresses, now commonly known as CIDR notation, in which an address or routing prefix is written with a suffix indicating the number of bits of the prefix, such as 192.0.2.0/24 for IPv4, and 2001:db8::/32 for IPv6. 

The network address is written as a prefix, similar to how an IP address is written (e.g. 192.255.255.255). The suffix, which means how many bits are in the whole address (e.g. /12), is the second component. A CIDR IP address will look anything like this when put together − 192.255.255.255/12
This means the first 12 bits of the address are for the network, while the last 20 bits are for host addresses.

### Properties of CIDR Block
1. The IP addresses in a block are continuous.
2. The first address of a block should be exactly divisible by the number of addresses of a block.
3. The size of the Block should be power of 2.