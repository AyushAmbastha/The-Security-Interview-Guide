# RC4

RC4 is a symmetric stream cipher that gaines widespread adoption because of its simplicity and speed. RC4 supports key sizes of 40 bits to 2048 bits. 

First, the user enters a plaintext file and an encryption key. Then, the RC4 encryption engine generates keystream bytes with the help of the Key Scheduling Algorithm and the Pseudo-Random Generation Algorithm. The X-OR operation is executed byte-by-byte, and the byte output is the encrypted text, which the receiver gets. Once they decrypt it through a byte-by-byte X-OR operation, they can access the plaintext stream. 

Since RC4 supports even large keys, the weakness of the RC4 aren't due to the brute-force attacks, but the cipher itself has inherent weaknesses and vulnerabilities that aren't only theoretically possible, there are lots of examples showing RC4 being broken.

Here are the most prominent RC4 issues and attacks identified over the years:
- Roos’ biases: there are a keystream-key correlation and permutations-key correlations, as well as other types of biases
- Biased outputs: RC4 produces keystreams that can be biased to different extents, which makes them vulnerable to distinguishing attacks
- Fluhrer Mantin Shamir attack: the first bytes of RC4 keystreams are not random and thus expose information about the key, which opens the doors for WEP attacks 
- Andreas Klein attack: like in previous attacks, even more correlations between the key and the RC4 keystream were discovered
- Combinatorial problems: problems with the number of inputs and outputs were discovered
- Royal Holloway attack: security researchers at the Information Security Group at Royal Holloway, University of London identified breaches and attack scenarios that can affect TLS and SSL protocols and WPA/TKIP implementations
- Bar-mitzvah attack: RC4 ciphers can be used to attack SSL protocols 
- Numerous Occurrence MOnitoring & Recovery Exploit (NOMORE) attack: vulnerabilities for both TLS protocols and WPA/TKIP were discovered, including the Fluhrer−McGrew biases. This attack was able to recover an authentication cookie from a TLS-encrypted session in only 52 hours. As this is an attack on the RC4 cipher itself, any protocol that uses this cipher is potentially vulnerable to the attack.

RC4 was used in WEP and WPA. It was dropped in 2015 in all versions of TLS.