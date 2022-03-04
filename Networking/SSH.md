## Secure Shell (SSH)

The SSH protocol (also referred to as Secure Shell) is a method for secure remote login from one computer to another. It provides several alternative options for strong authentication, and it protects the communications security and integrity with strong encryption. It is a secure alternative to the non-protected login protocols (such as telnet, rlogin) and insecure file transfer methods (such as FTP).

The protocol is used in corporate networks for:
- providing secure access for users and automated processes
- interactive and automated file transfers
- issuing remote commands
- managing network infrastructure and other mission-critical system components.

SSH works within a network through a client/server architecture. An SSH client is the program that runs SSH protocol from a specific device in order to access remote machines, automate data transfers, issue commands, and even manage network infrastructure. 

SSH has three components: transport layer protocol (TLP), user authentication protocol, and connection protocol. The three layers do the following:
1. Transport layer protocol: The TLP serves to authenticate the server and establish confidentiality and integrity. According to the Request for Comments (RFC) memo 4251, TLP should be held to a standard of perfect forward secrecy. 
2. User authentication protocol: It authenticates the user to the server, confirming the identity of the agent operating as the client.
3. Connection protocol: The connection protocol mutiplexes the SSH tunnel. It creates distinct data streams, or logical channels, from a single client/server connection.

The sequential actions of these three protocol layers allow the SSH protocol to successfully secure connections, encrypt data, and transfer data along different channels.

<p align="center">
  <img src="../images/ssh.png" width="400" height="150">
</p>