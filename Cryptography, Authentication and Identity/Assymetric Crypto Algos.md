# Assymetric Cryptographic Algorithms

## RSA

The RSA algorithm is an asymmetric cryptography algorithm; this means that it uses a public key and a private key (i.e two different, mathematically linked keys). The RSA algorithm is named after those who invented it in 1978: Ron Rivest, Adi Shamir, and Leonard Adleman.

**Generating the keys**
1. Select two large prime numbers, $x$ and $y$. The prime numbers need to be large so that they will be difficult for someone to figure out.
2. Calculate $n = x * y$.
3. Calculate the totient function; $\phi(n) = (x-1)(y-1)$.
4. Select an integer $e$, such that $e$ is co-prime to $\phi(n)$ i.e., $gcd(e, \phi(n)) = 1$ and $1 < e < \phi(n)$. The pair of numbers $(n,e)$ makes up the public key.\
Note: Two integers are co-prime if the only positive integer that divides them is 1.
5. Calculate $d$ such that $e.d = 1$ mod $\phi(n)$. $d$ can be found using the extended euclidean algorithm. The pair $(n,d)$ makes up the private key.

**Encryption**\
Given a plaintext $P$, represented as a number, the ciphertext $C$ is calculated as:

$C = P^{e}$ mod $n$

**Decryption**\
Using the private key $(n,d)$, the plaintext can be found using:

$P = C^{d}$ mod $n$

What makes RSA difficult to break is that nobody knows how to compute the inverse RSA (the "decryption") without knowing the prime factors of the $n$; and for large numbers $x$ and $y$, $n$ would be very large making the prime factorization hard. 

## Diffie Hellman Key Exchange

Diffie–Hellman key exchange establishes a shared secret between two parties that can be used for secret communication for exchanging data over a public network.
The simplest and the original implementation of the protocol uses the multiplicative group of integers modulo p, where p is prime, and g is a primitive root modulo p. These two values are chosen in this way to ensure that the resulting shared secret can take on any value from 1 to p–1. 

1. Alice and Bob publicly agree to use a modulus $p = 23$ and base $g = 5$ (which is a primitive root modulo 23).
2. Alice chooses a secret integer $a = 4$, then sends Bob $A = g^a$ mod $p$\
  $A = 5^4$ mod $23 = 4$
3. Bob chooses a secret integer $b = 3$, then sends Alice $B = g^b$ mod $p$\
$B = 53$ mod $23 = 10$
4. Alice computes $s = B^a$ mod $p$\
$s = 10^4$ mod $23 = 18$
5. Bob computes $s = A^b$ mod $p$\
$s = 43$ mod $23 = 18$
6. Alice and Bob now share a secret (the number 18).
   
Both Alice and Bob have arrived at the same values because under mod p, \
$A^b$ mod $p$ = $g^{ab}$ mod $p$ = $g^{ba}$ mod $p$ = $B^a$ mod $p$

Only a and b are kept secret. All the other values – $p, g, g^a$ mod $p$, and $g^b$ mod $p$ – are sent in the clear. The strength of the scheme comes from the fact that $g^{ab}$ mod $p$ = $g^{ba}$ mod $p$ take extremely long times to compute by any known algorithm. Once Alice and Bob compute the shared secret they can use it as an encryption key, known only to them, for sending messages across the same open communications channel.

Of course, much larger values of $a, b,$ and $p$ would be needed to make this example secure. If $p$ is a prime of at least 600 digits, then even the fastest modern computers using the fastest known algorithm cannot find $a$ and $b$ given only $g$, $p$ and $g^a$ mod $p$. Such a problem is called the discrete logarithm problem and the computation of $g^a$ mod $p$ is known as modular exponentiation and can be done efficiently even for large numbers. 

## RSA vs. Diffie Hellman
RSA tends to be more popular for securing information on the internet. Because the Diffie-Hellman Key Exchange doesn’t authenticate either party, a hacker could more easily send spoof messages posing as one of the parties in the transaction. Thus, RSA is preferred over Diffie Hellman for verifying certificates because the Diffie Hellman approach requires an additional digital signature component.

Diffie Hellman is preferred over RSA for key exchange because Diffie Hellman requires one user to have different keys for every communication. Thus, the Diffie Hellman approach gaurantees perfect forward secrecy.