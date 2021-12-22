# Important terms

## Confidentiality
Confidentiality is the act of keeping information private. It entails ensuring that the data is only accessible to those who are authorized to use it, as well as restricting access to others. Data encryption is a way of ensuring confidentiality.

## Integrity
This principle assures that the data is genuine, correct, and safe from unwanted threat actors or unintentional user alteration. If any changes are made, precautions should be taken to protect sensitive data from corruption or loss, as well as to quickly recover from such an incident. Furthermore, it denotes that the source of information must be genuine.

## Availability
This principle ensures that information is constantly available and helpful to those who have access to it. It ensures that system failures or cyber-attacks do not obstruct these accesses.

## Authentication vs. Authorization

Authentication is the security practice of confirming that someone is who they claim to be, while authorization is the process of determining which level of access each user is granted.

For example, when a user signs into their email or online banking account, they use a login and password combination that only they are supposed to know. The software uses this information to authenticate the user. Some applications may require two-factor authentication or a biometrical confirmation, such as a thumbprint or face ID scan.

Once authenticated, a user can only see the information they are authorized to access. In the case of an online banking account, the user can only see information related to their personal banking account. Meanwhile, a fund manager at the bank can log in to the same application and see data on the bank’s overall financial holdings. Since the bank handles very sensitive personal information, it’s entirely possible that no one has unrestricted access to the data.

## Encryption
Encryption is the process of securely encoding data in such a way that only authorized users with a key or password can decrypt the data to reveal the original. There are two basic types of encryption; symmetric key and public key/asymmetric. In symmetric key, the same key is used to encrypt and decrypt data, like a password. In asymmetric or public key encryption, one key is used to encrypt data and a different key is used to decrypt the data.

Encryption is used when data needs to be protected so those without the decryption keys cannot access the original data. When data is sent to a website over HTTPS it is encrypted using public key encryption.

While encryption does involve encoding data, the two are not interchangeable terms, encryption is always used when referring to data that has been securely encoded. Encoding data is used only when talking about data that is not securely encoded.

An example of encryption is: AES 256.

## Encoding
Encoding data is a process involving changing data into a new format using a scheme. Encoding is a reversible process; data can be encoded to a new format and decoded to its original format. Encoding typically involves a publicly available scheme that is easily reversed. Encoding data is typically used to ensure integrity and usability of data and is commonly used when data cannot be transferred in its current format between systems or applications.

Encoding is not used to protect or secure data because it is easy to reverse.Encoding data is a process involving changing data into a new format using a scheme. Encoding is a reversible process; data can be encoded to a new format and decoded to its original format. Encoding typically involves a publicly available scheme that is easily reversed. Encoding data is typically used to ensure integrity and usability of data and is commonly used when data cannot be transferred in its current format between systems or applications.

Encoding is not used to protect or secure data because it is easy to reverse.

An example of encoding is: Base64

## Hashing
Hashing involves computing a fixed-length mathematical summary of data, the input data can be any size. In contrast to encoding, hashing cannot be reversed. It is not possible to take a hash and convert it back to the original data. Hashing is commonly used to verify the integrity of data. If two pieces of identical data are hashed using the same hash function, the resulting hash will be identical. If the two pieces of data are different, the resulting hashes will be different and unique.

As an example, say Alice wants to send Bob a file and verify that Bob has the exact same file and that no changes occurred in the transferring process. Alice will email Bob the file along with a hash of the file. After Bob downloads the file, he can verify the file is identical by performing a hash function on the file and verify the resulting hash is the same as Alice provided.

An example of a hash function is: SHA512

In addition to verifying the integrity of data, hashing is the recommended data transformation technique in authentication processes for computer systems and applications. It is recommended to never store passwords and instead store only the hash of the “salted password”. A salt is a random string appended to a password that only the authentication process system knows; this guarantees that if two users have the same password the stored hashes are different.

When a user inputs a password to a web application, the password is sent to the web server. The web server then appends the salt to the password and performs a hash function on the password and a salt and compares this output hash with the hash stored in the database for the user. If the hashes match for that user, the user is granted access. Hashing ensures in the event of a breach, or malicious insider the original passwords can never be retrieved. Salting ensures that, if a breach does occur, an attacker cannot determine which users have the same passwords.

## Obfuscation
The purpose of obfuscation is to make something harder to understand, usually for the purposes of making it more difficult to attack or to copy.

One common use is the the obfuscation of source code so that it’s harder to replicate a given product if it is reverse engineered.

It’s important to note that obfuscation is not a strong control (like properly employed encryption) but rather an obstacle. It, like encoding, can often be reversed by using the same technique that obfuscated it. Other times it is simply a manual process that takes time to work through.

Another key thing to realize about obfuscation is that there is a limitation to how obscure the code can become, depending on the content being obscured. If you are obscuring computer code, for example, the limitation is that the result must still be consumable by the computer or else the application will cease to function.

## Signing

Signing of data works to authenticate the sender of the data and tends to implement a form of encryption in its process. The process of signing emails, sensitive data, and other information has become necessary, as it verifies the identity of the sender and ensures the data has not been altered in transit. If a Man in the Middle attack occurred and the data was altered or compromised by the attacker, the recipient of the information would know that this has occurred. The attacker could alter the data, but as they do not have the key used by the sender to sign the data, the recipient of the data will know not to trust the sent data when analyzing the key and data.

## Threat, Risk and Vulnerability

<ins>Threat</ins> - A threat is any form of hazard that has the potential to destroy or steal data, disrupt operations, or cause harm in general. Malware, phishing, data breaches, and even unethical employees are all examples of threats.
Threat actors, who might be individuals or groups with a variety of backgrounds and motives, express threats. Understanding threats is essential for developing effective mitigations and making informed cybersecurity decisions. Threat intelligence is information regarding threats and threat actors.

<ins>Vulnerability</ins> - A vulnerability is a flaw in hardware, software, personnel, or procedures that threat actors can use to achieve their objectives.
Physical vulnerabilities, such as publicly exposed networking equipment, software vulnerabilities, such as a buffer overflow vulnerability in a browser, and even human vulnerabilities, such as an employee vulnerable to phishing assaults, are all examples of vulnerabilities.
Vulnerability management is the process of identifying, reporting and repairing vulnerabilities. A zero-day vulnerability is a vulnerability for which a remedy is not yet available.

<ins>Risk</ins> - The probability of a threat and the consequence of a vulnerability are combined to form risk. To put it another way, the risk is the likelihood of a threat agent successfully exploiting a vulnerability, which may be calculated using the formula:

Risk = Likelihood of a threat * Vulnerability Impact

Risk management is the process of identifying all potential hazards, analyzing their impact, and determining the best course of action. It's a never-ending procedure that examines new threats and vulnerabilities on a regular basis. Risks can be avoided, minimized, accepted, or passed to a third party depending on the response chosen.

Threat = a new incident with potential to harm a system\
Vulnerability = known weakness that hackers coudl exploit\
Risk = potential for damage when a threat exploits a vulnerability   