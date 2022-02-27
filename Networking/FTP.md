# File Transfer Protocol (FTP)
FTP means "File Transfer Protocol" and refers to a group of rules that govern how computers transfer files from one system to another over the internet. Businesses use FTP to send files between computers, while websites use FTP for the uploading and downloading of files from their website's servers.

FTP works by opening two connections that link the computers trying to communicate with each other. One connection is designated for the commands and replies that get sent between the two clients, and the other channel handles the transfer of data. During an FTP transmission, there are four commands used by the computers, servers, or proxy servers that are communicating. These are “send,” “get,” “change directory,” and “transfer.”

While transferring files, FTP uses three different modes: block, stream, and compressed. The stream mode enables FTP to manage information in a string of data without any boundaries between them. The block mode separates the data into blocks, and in the compress mode, FTP uses an algorithm called the Lempel-Ziv to compress the data.

## What is FTP Useful For?
One of the main reasons why modern businesses and individuals need FTP is its ability to perform large file size transfers. FTP can send hundreds of gigabytes of data at once and still provide a smooth transmission. The ability to send larger amounts of data, in turn, improves workflow. FTP also allows to send multiple files at once, one can select several files and then send them all at the same time. Without FTP services, multiple files have to be sent one by one. 

## Types of FTP

**FTP Plain** - FTP Plain refers to normal FTP without encryption. By default, it uses port 21, and it is supported by the majority of web browsers.

**FTPS** - FTPS refers to FTP Secure or FTP secure sockets layer (SSL) because this kind of FTP server uses SSL encryption, which is slightly different than traditional FTP. The primary difference is the security that comes with FTPS, which was the first type of encrypted FTP invented.

**FTPES** - The “E” in FTPES means “explicit,” making the acronym stand for File Transfer Protocol over explicit transport layer security (TLS)/SSL. This type of FTP begins like regular FTP, using port 21, but then special commands upgrade it to a TLS/SSL-encrypted transmission. Because it tends to work well with firewalls, some prefer to use FTPES over FTPS.

## How to Use FTP
The three most common ways of using FTP include:
1. Via a web browser: With a web browser, you do not need any special software or a client to download files from servers that provide for FTP sites.
2. A general user interface (GUI) FTP client: These third-party applications enable users to connect and then send files over FTP.
3. Command-line FTP: Major operating systems come equipped with FTP client capabilities as a command line.

## FTP vs. SFTP
FTP stands for File Transfer Protocol, while SFTP refers to Secure Shell (SSH) File Transfer Protocol. This gives you file transfers that are secured via SSH, which provides full access to shell accounts. A shell account is one that sits on a remote server.

FTP is different from SFTP in that it does not give users a secure channel for transferring files. Also, FTP makes use of two channels for transferring data, but SFTP only uses a single channel. The inbound connections that each protocol uses are different as well. FTP defaults to port 21, but SFTP allows inbound communication on port 22. Additionally, SFTP uses a tunneling method to transfer data while FTP uses direct transfer.

## FTP vs. HTTP
Even though Hyper Text Transfer Protocol (HTTP) and FTP are similar in that they are application-layer protocols that enable you to send files between systems, there are some key differences. HTTP can support multiple sessions at the same time because it is a stateless protocol. This means it does not save the data used in a session to employ it in the next one. 

FTP, on the other hand, is stateful, which means it collects data about the client and uses it in the next request the client makes. Because FTP performs this function, it is limited in the number of sessions it can support simultaneously. Regardless of the bandwidth of a network, HTTP has the potential to be a much more efficient method of data transmission.

Another key differen ce is that with FTP, there needs to be client authentication before information is transferred. With HTTP, no client authentication is needed. HTTP uses a well-known, common port, making it easy for firewalls to work with. In some cases, FTP can be more difficult for a firewall to manage.

## FTP vs. MFT
In some ways, managed file transfer (MFT) is the new kid on the block when compared to FTP. FTP, while effective in many settings, was not designed to accommodate the complex threat landscape people are forced to deal with today. In fact, there has even been an official warning issued by the FBI regarding the potential pitfalls of using FTP - even that which is secured with SSL and SSH.

As the name suggests, managed file transfer comes with management and various compliance and security features. It is important for these to be in place, not just to make data transfer safer but to appease the authorities that require secure data transfer, particularly in companies that handle sensitive data such as patient medical records. Normal FTP leaves data transfers open to an eavesdropping attack or a banker Trojan, which targets financial institutions.

Even though you could manually program the security and management features necessary for safer FTP transmissions, MFT saves you the time and energy. If, for example, two people were using the Mist Browser to configure dapps on Ethereum, a hacker could intercept their communications before they reached the FTP port. The hacker could then sell what was intercepted to a competitor, who could use it to make a similar dapp and release it sooner, thus gaining a strategic advantage.

## Security Challenges of FTP
FTP was not designed to provide a secure tunnel through which information could travel. Hence, there is no encryption. If a hacker is able to intercept an FTP transmission, they would not have to muddle through encryption to view or make changes to the data usable. Even if you use FTP cloud storage, if the service provider has their system compromised, the data could be intercepted and exploited.

Therefore, data transmitted through FTP is a relatively slow-moving target for spoofing, sniffing, brute force, and other kinds of attacks. Through simple port scanning, a hacker could check an FTP transmission and attempt to exploit its vulnerabilities.

One of the primary vulnerabilities of FTP is its use of clear-text passwords, which are passwords that do not undergo an encryption process. In other words, “Jerry1992” looks exactly like “Jerry1992.” In more secure protocols, an algorithm is used to mask the actual password. Therefore, “Jerry1992” may end up looking like “dj18387saksng8937d9d8d7s6a8d89.” FTP does not secure passwords like this, making them easier to figure out by bad actors.