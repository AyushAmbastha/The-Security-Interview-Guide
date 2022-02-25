# Botnets

A botnet is a number of Internet-connected devices, each of which runs one or more bots. Bots are software applications that run automated tasks or scripts over the internet. They perform tasks, that are simple and repetitive, much faster than a person could ever do. Usually, a botnet is infected by malware that are under the control of a single attacking party. From one central point, the attacking party can command every computer on its botnet to simultaneously carry out a coordinated criminal action. The scale of a botnet (many comprised of millions of bots) enable the attacker to perform large-scale actions that were previously impossible with malware. Since botnets remain under control of a remote attacker, infected machines can receive updates and change their behavior on the fly.

## How to build a Botnet
Basic stages of building a botnet can be simplified into a few steps:
1. Prep and Expose - hacker exploits a vulnerability to expose users to malware.
2. Infect - user devices are infected with malware that can take control of their device.
3. Activate - hackers mobilize infected devices to carry out attacks.

Stage 1 exposure starts with hackers finding a vulnerability in a website, application, or human behavior. The goal is to set the user up for being unknowingly exposed to a malware infection. You’ll commonly see hackers exploit security issues in software or websites or deliver the malware through emails and other online messages.

In stage 2, the user gets infected with the botnet malware upon taking an action that compromises their device. Many of these methods either involve users being persuaded via social engineering to download a special Trojan virus. Other attackers may be more aggressive by using a drive-by download upon visiting an infected site. Regardless of the delivery method, cybercriminals ultimately breach the security of several users’ computers.

Once the hacker is ready, stage 3 initiates by taking control of each computer. The attacker organizes all of the infected machines into a network of “bots” that they can remotely manage. Often, the cybercriminal will seek to infect and control thousands, tens of thousands, or even millions of computers. The cybercriminal can then act as the boss of a large “zombie network” - i.e. a fully assembled and active botnet.

## Botnet Attack

A botnet attack is a type of cyber attack carried out by a botnet that is controlled by a malicious actor.  Attackers inject malware into the network using a botnet and use them for launching attacks by controlling them as a collective. Botnet attacks can be used for sending spam, data theft, compromising confidential info, perpetuating ad fraud or for launching more dangerous Distributed Denial of Service or DDoS attacks. 

## Architecture

Botnet architecture has evolved over time in an effort to evade detection and disruption. Traditionally, bot programs are constructed as clients which communicate via existing servers. This allows the bot herder (the controller of the botnet) to perform all control from a remote location, which obfuscates the traffic. Many recent botnets now rely on existing peer-to-peer networks to communicate. These P2P bot programs perform the same actions as the client–server model, but they do not require a central server to communicate.

**Client-Server Model -** The first botnets on the Internet used a client–server model to accomplish their tasks. Typically, these botnets operate through Internet Relay Chat networks, domains, or websites. Infected clients access a predetermined location and await incoming commands from the server. The bot herder sends commands to the server, which relays them to the clients. Clients execute the commands and report their results back to the bot herder.

In the case of IRC botnets, infected clients connect to an infected IRC server and join a channel pre-designated for C&C by the bot herder. The bot herder sends commands to the channel via the IRC server. Each client retrieves the commands and executes them. Clients send messages back to the IRC channel with the results of their actions. The disadvantage to using a centralized model over a P2P model is that it is susceptible to a single point of failure.

The two most common C&C communication channels are IRC and HTTP:
- IRC (Internet Relay Chat) botnet - IRC botnets are among the earliest types of botnet and are controlled remotely with a pre-configured IRC server and channel. The bots connect to the IRC server and await the bot herder’s commands.
- HTTP botnet - An HTTP botnet is a web-based botnet through which the bot herder uses the HTTP protocol to send commands. Bots will periodically visit the server to get updates and new commands. Using HTTP protocol allows the herder to mask their activities as normal web traffic.

**Peer-to-peer -** In response to efforts to detect and decapitate IRC botnets, bot herders have begun deploying malware on peer-to-peer networks. These bots may use digital signatures so that only someone with access to the private key can control the botnet.
Newer botnets fully operate over P2P networks. Rather than communicate with a centralized server, P2P bots perform as both a command distribution server and a client which receives commands. This avoids having any single point of failure, which is an issue for centralized botnets.

In order to find other infected machines, the bot discreetly probes random IP addresses until it contacts another infected machine. The contacted bot replies with information such as its software version and list of known bots. If one of the bots' version is lower than the other, they will initiate a file transfer to update. This way, each bot grows its list of infected machines and updates itself by periodically communicating to all known bots.

### Bot Attacks vs a Botnet Attack
Botnet attacks can be thought of as a specific type of the more general “bot attack”. Bot attacks are cyber attacks that use automated web requests meant to tamper with a website, application or device. Bot attacks initially consisted of simple spamming operations but have evolved to be more complex in nature, intended to defraud or manipulate users. One of the reasons for this is the availability of open-source tools for building bots, known as botkits. These botkits, usually available for free online or on the Dark Web, can be used to carry out nefarious tasks like scraping a website, taking over an account, abusing form submissions and to create botnet attacks, including DDoS attacks. 

### How Does a Botnet Attack Work?
Botnet attacks start with cyber criminals gaining access to devices by compromising their security. They could do this via hacks like the injection of Trojan viruses or basic social engineering tactics. Then these devices are brought under control using software that commands the devices to carry out attacks on a large scale. Sometimes, the criminals themselves may not use the botnet to launch attacks but instead, they sell access to the network to other malicious actors. These third parties can then use the botnet as a “zombie” network for their own needs, like directing spam campaigns. 

Botnet attacks can differ based on their methods and the tools they employ. Sometimes these botnets themselves don’t attack but instead become a pathway for hackers to launch secondary campaigns like scams and ransom attacks. Some of the common types of botnet attacks include:

1. Distributed Denial-of-Service (DDoS) attacks: During a DDoS attack, the botnet sends an overwhelming number of requests to a targeted server or application, causing it to crash. Network layer DDoS attacks use SYN floods, UDP floods, DNS amplification, and other techniques designed to eat up the target’s bandwidth and prevent legitimate requests from being served. Application-layer DDoS attacks use HTTP floods, Slowloris or RUDY attacks, zero-day attacks and other attacks that target vulnerabilities in an operating system, application or protocol in order to crash a particular application. This downtime in the server’s operation can also be used for launching additional botnet based attacks.
2. Phishing attacks: These are often launched with the purpose of extracting key information from an organization’s employees. For example, mass spam campaigns can be devised to imitate trusted sources within the organization to trick people into revealing confidential information like login details, financial info and credit card details.  
3. Brute force attacks: These involve programs which forcefully breach web accounts by force. Dictionary attacks and credential stuffing are used to exploit weak user passwords and access their data.
4. Cryptojacking: Cryptocurrency is “mined” by computers that earn bits of currency by solving encrypted math equations. However, computations use a lot of electricity – Bitcoin mining alone uses as much energy as the entire nation of Switzerland, and when all expenses associated with mining cryptocurrency are counted, an adversary would spend three times more mining cryptocurrency than mining actual gold. To a criminal mind, it makes a lot more sense to make someone else pay for the effort by commandeering their resources.
5. Snooping: Botnets can be used to monitor network traffic, either passively to gather intelligence and steal credentials or actively to inject malicious code into HTTP traffic. Domain Name System (DNS) snooping maps IP addresses to domain names that are contained in the dynamic database or a local list in order to discover what queries are being made, which domains might be the best targets for a cache poisoning attack, or what mis-typed domains might be worth registering.

### Detecting Botnet Attacks
Botnet attacks are hard to detect because the user is often not aware when a device is compromised. Some botnets are designed with a central server controlling each bot in a command-and-control model. For these botnets, a key step to detecting attacks involves finding that central server.

Static analysis techniques can be helpful to spot infections in devices. These are run when the device is not executing any programs and involve looking for malware signatures and other suspicious connections to command-and-control servers that look for instructions and suspicious executable files. Botnet creators are developing more sophisticated techniques to avoid detection and are becoming better at avoiding static analysis methods. Behavioural or dynamic analyses can also be used if there are more resources available. These involve scanning ports on local networks, looking for unusual traffic and activity involving Internet Relay Chat (IRC).

Antivirus software can detect botnet attacks to a certain extent but fails to spot infected devices. Another interesting method is using honeypots. These are fake systems that bait a botnet attack via a fake infiltration opportunity.

### Can Botnet Attacks be Prevented?
One of the main challenges in preventing these attacks is the proliferation of devices. As different types of devices become easily available, often with their own security settings, it becomes difficult to monitor, track and stop these attacks before they happen. Yet you can still take certain measures to prevent botnet attacks.

- Keep all systems updated - One of the main pathways that botnets take to penetrate and compromise a business’ security system is using the unpatched vulnerabilities present in the network’s machines. This makes it critical to keep the systems updated, and to ensure new updates are installed as soon as they are available. This also includes hardware devices, especially legacy devices which can often be ignored in enterprises when they are no longer used actively.

- Adopt basic cybersecurity best practices - It is important to follow basic security hygiene on all devices as well, to keep botnet attacks at bay. This involves using complex passwords, educating employees about the dangers of phishing emails and clicking on suspicious attachments and links. Enterprises should also take appropriate measures to ensure that any new device that enters their network has sound security settings.

- Control access to machines - Taking measures to lock access to machines is another way you can prevent botnet attacks. In addition to strong passwords, you should also deploy multi-factor authentication and controls to provide access to only those who need it most.

- Monitor network traffic using analytics solutions - Prevention of botnet attacks requires good techniques to detect them ahead of time. Using advanced analytics to monitor and manage traffic flows, user access and data leaks is another measure you can take.

### How to Mitigate Against Bot Attacks
Sometimes even your best prevention measures can be overcome by botnet attacks, and it becomes too late by the time you detect them in your network. In such scenarios, your best bet is to mitigate the impact of such attacks. This means reducing the damage that will be caused.

- Disable the central server - Botnets designed in the command-and-control model can be disabled if the central resource or server is identified. Think of it like cutting off the brain of the operation to take down the whole botnet.

- Run antivirus or reset the device - For individual computers which have been compromised, the goal should be to regain control. And this can be done by running antivirus software, reinstalling the system’s software or reformatting the system from scratch. In the case of IoT devices, you will have to flash the firmware, completing a factory reset to mitigate a botnet attack.