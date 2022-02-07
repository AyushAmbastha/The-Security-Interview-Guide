# Advanced Encryption Standard
AES is a symmetric type of encryption, as it uses the same key to both encrypt and decrypt data. It uses the SPN (substitution permutation network) algorithm, applying multiple rounds to encrypt data. These encryption rounds are the reason behind the impenetrability of AES, as there are far too many rounds to break through.

There are three lengths of AES encryption keys. Each key length has a different number of possible key combinations:
- 128-bit key length: 3.4 x 1038
- 192-bit key length: 6.2 x 1057
- 256-bit key length: 1.1 x 1077
  
Even though the key length of this encryption method varies, its block size - 128-bits (or 16 bytes) - stays fixed. 

Why are there multiple key lengths? And, if the 256-bit key is the strongest of the bunch (even referred to as “military-grade” encryption), why don’t we just always use it? Well, it all comes down to resources. For example, an app that uses AES-256 instead of AES-128 might drain your phone battery a bit faster.

## Advantages of AES
- Allows for easy implementation, as well as really fast encryption and decryption times.
- Requires less memory than many other types of encryption (like DES)
- Finally, when an action requires an extra layer of safety, you can combine AES with various security protocols like WPA2 or even other types of encryption like SSL. 

### Why AES over DES?

The DES key length was a mere 56 bits. And it turned out that this isn’t nearly enough to keep encrypted information safe. For example, a test by distributed.net and the Electronic Frontier Foundation showed that DES can be easily cracked in a little bit more than 22 hours. Keep in mind that this was done in 1999, when computing power was far from what it is now. Today, a powerful machine can crack a 56-bit DES key in 362 seconds. 

On the other hand, cracking a 128-bit AES encryption key can take up to 36 quadrillion years. Just imagine what time it would take to crack a 256-bit AES key, which boasts a staggering number of 984,665,640,564,039,457,584,007,913,129,639,936 combinations. Keeping this number in mind, we can safely assume that a brute-force attack on AES encryption will not happen without a significant increase in computing power.

## How does AES encryption work?

**1. Dividing data into blocks**\
AES is a block cipher. Unlike stream ciphers, it encrypts data in blocks of bits instead of bit-by-bit. 

Each of its blocks contains a column of 16 bytes in a layout of four-by-four. As one byte contains 8 bits, we get 128-bit block size (16x8=128). 

**2. Key expansion**\
This is an important step of AES encryption. It produces new 128-bit round keys with the help of Rijndael’s key schedule.

The AES algorithm will need this set of new expanded keys a bit later.

**3. Adding round key**\
This is the very first round of AES encryption. Here, the algorithm adds the initial key to our phrase, which was previously turned into a 4x4 block. Since, AES actually uses binary code, adding here is the XOR operation. So, after adding the two blocks, we end up with a completely new block of cipher.

**4. Byte substitution**\
Now, the AES algorithm substitutes every byte with a code according to a pre-established table called the Rijndael S-box. This look-up table is designed to be very complex and the relationship between the input and output is highly non-linear.

**5. Shifting rows**\
In this step, the AES algorithm shifts the rows of the block it got during the byte substitution process. The first row stays put. However, the second row gets shifted to the left by one byte, the third row moves to the left by two bytes, while the last one gets shifted by three bytes.

**6. Mixing columns**\
This step multiplies each column by a predefined matrix, giving us a brand new block of code. 

**7. Adding round key**\
It’s time to apply the round key we got in the key expansion section. Let’s add it to the block we got in the previous section after the process of column mixing.

**8. Rinse and repeat**\
Now, the AES encryption algorithm will go through many more rounds of byte substitution, shifting rows, mixing columns, and adding a round key.

The number of identical rounds the data goes through depends on the AES key length:

128-bit key: 9 rounds\
192-bit key: 11 rounds\
256-bit key: 13 rounds\
So, in the case of 256-bit key encryption, for example, the data goes through the previously mentioned steps 13 times in a row.

However, that’s still not the end of it. There is one extra round after the mentioned 9, 11, or 13 rounds of encryption. During this additional round, the algorithm only goes through the stages of byte substitution, row shifts, and adding a round key. It leaves out the step of mixing columns. Why? Because, at this point, that would be redundant. In other words, this action would use too much processing power without significantly altering the data.

So, at the very end of the encryption process, the data will have gone through the following number of rounds:

128-bit key: 10 rounds\
192-bit key: 12 rounds\
256-bit key: 14 rounds\
After all the rounds are completed, the original phrase will look like a set of random characters. 

AES decryption begins with the inverse round key. Afterwards, the algorithm reverses every single action (shift rows, byte substitution, and, later on, column mixing), until it deciphers the original message.

## Does AES encryption have any security issues?
Even though AES is an exceptionally secure type of encryption, it might not be 100% impenetrable a few years from now. No known successful real-life attacks have been recorded so far. A “brute-force” type of attack is virtually useless against the AES algorithm, as it would potentially take billions of years to crack it. However, if the encryption is implemented incorrectly, there might be some potential risks. Luckily, no hacker will be able to crack a correctly configured AES system. So, as long as there’s no error, your sensitive information is completely safe.

Related-key attacks - Unlike brute-force attacks, related-key attacks target the encryption key itself. They require less time and effort, and have a higher chance of being successful. This type of attack can work if the hacker knows (or suspects) the relationship between two different keys. A few times, AES encryption has been a target of related-key attacks, the most notable one discovered in 2009. To prevent similar things from happening, cryptographers improved the complexity of the AES key schedule.

Side-channel attacks - In case of improper implementation of a computer system, AES encryption is not completely immune to side-channel attacks. This type of attack relies on data leakage, for example, electromagnetic leaks. However, if AES is properly implemented, it can help detect the data leaks before anything bad happens.

Known-key distinguishing attacks - In 2009, there was an attempt to crack AES-128 with the help of a known-key distinguishing attack. It proved to be successful against the 8-round version of the 128-bit key length AES encryption. However, the actual AES-128 goes through 10 rounds of encryption, which means that the attack was not a threat in real life. Also, to perform a known-key distinguishing attack, the hacker has to know the key, which is very unlikely.

Key-recovery attacks - In 2011, a key-recovery attack was done as a test to crack AES. This type of attack requires the hacker to have at least one pair of encrypted and decrypted messages. However, the test didn’t provide significant results, as it only proved to be four times faster than a brute-force attack (which would still take billions of years).