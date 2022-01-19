# Public-Key Infrastructure (PKI)

PKI (or Public Key Infrastructure) is a framework of encryption and decryption based on the concept of assymetric cryptography and digital certificates. Digital Certificates are used to verify the identity of the machines and/or users that ultimately proves the integrity of the transaction.

## Components Of Public Key Infrastructure
There are three key components: digital certificates, certificate authority, and registration authority. 

**Digital Certificates**\
PKI functions because of digital certificates. A digital certificate is like a drivers license — it’s a form of electronic identification for websites and organizations. Secure connections between two communicating machines are made available through PKI because the identities of the two parties can be verified by way of certificates. 

Public key pertaining to the user is stored in digital certificates by The Certification Authority (CA) along with other relevant information such as client information, expiration date, usage, issuer etc. CA digitally signs this entire information and includes digital signature in the certificate. Anyone who needs the assurance about the public key and associated information of client, carries out the signature validation process using CA’s public key. Successful validation assures that the public key given in the certificate belongs to the person whose details are given in the certificate.

Users can create their own certificates for internal communications or obtain a PKI digital certificate through a trusted third party issuer, called the Certificate Authority.

**Certificate Authority**\
A Certificate Authority (CA) is used to authenticate the digital identities of the users, which can range from individuals to computer systems to servers. The CA takes responsibility for identifying correctly the identity of the client asking for a certificate to be issued, and ensures that the information contained within the certificate is correct and digitally signs it. Certificate Authorities prevent falsified entities and manage the life cycle of any given number of digital certificates within the system.

The key functions of a CA are as follows −

- Generating key pairs − The CA may generate a key pair independently or jointly with the client.

- Issuing digital certificates − The CA could be thought of as the PKI equivalent of a passport agency − the CA issues a certificate after client provides the credentials to confirm his identity. The CA then signs the certificate to prevent modification of the details contained in the certificate.

- Publishing Certificates − The CA need to publish certificates so that users can find them. There are two ways of achieving this. One is to publish certificates in the equivalent of an electronic telephone directory. The other is to send your certificate out to those people you think might need it by one means or another.

- Verifying Certificates − The CA makes its public key available in environment to assist verification of his signature on clients’ digital certificate.

- Revocation of Certificates − At times, CA revokes the certificate issued due to some reason such as compromise of private key by user or loss of trust in the client. After revocation, CA maintains the list of all revoked certificate that is available to the environment.

**Registration Authority**\
Registration Authority (RA) is authorized by the Certificate Authority to provide digital certificates to users on a case-by-case basis. All of the certificates that are requested, received, and revoked by both the Certificate Authority and the Registration Authority are stored in an encrypted certificate database.

Certificate history and information is also kept on what is called a certificate store, which is usually grounded on a specific computer and acts as a storage space for all memory relevant to the certificate history, including issued certificates and private encryption keys. Google Wallet is a great example of this.

**Hierarchy of CA**\
With vast networks and requirements of global communications, it is practically not feasible to have only one trusted CA from whom all users obtain their certificates. Secondly, availability of only one CA may lead to difficulties if CA is compromised.

In such case, the hierarchical certification model is of interest since it allows public key certificates to be used in environments where two communicating parties do not have trust relationships with the same CA.

- The root CA is at the top of the CA hierarchy and the root CA's certificate is a self-signed certificate.
- The CAs, which are directly subordinate to the root CA (For example, CA1 and CA2) have CA certificates that are signed by the root CA.
- The CAs under the subordinate CAs in the hierarchy (For example, CA5 and CA6) have their CA certificates signed by the higher-level subordinate CAs.

A certificate chain traces a path of certificates from a branch in the hierarchy to the root of the hierarchy. Verifying a certificate chain is the process of ensuring that a specific certificate chain is valid, correctly signed, and trustworthy. The following procedure verifies a certificate chain, beginning with the certificate that is presented for authentication −

- A client whose authenticity is being verified supplies his certificate, generally along with the chain of certificates up to Root CA.
- Verifier takes the certificate and validates by using public key of issuer. The issuer’s public key is found in the issuer’s certificate which is in the chain next to client’s certificate.
- Now if the higher CA who has signed the issuer’s certificate, is trusted by the verifier, verification is successful and stops here.
- Else, the issuer's certificate is verified in a similar manner as done for client in above steps. This process continues till either trusted CA is found in between or else it continues till Root CA.

## What Is PKI Security?
PKI performs encryption directly through the keys that it generates. It works by using two different cryptographic keys: a public key and a private key. Whether these keys are public or private, they encrypt and decrypt secure data. 

By using a two-key encryption system, PKI secures sensitive electronic information as it is passed back and forth between two parties, and provides each party with a key to encrypt and decrypt the digital data.

PKI security is used in many different ways. The main ways that PKI security can be used are:

- Securing emails
- Securing web communications (such as retail transactions)
- Digitally signing software
- Digitally signing applications
- Encrypting files
- Decrypting files
- Smart card authentication
  
## Security Limitations Of PKI
- PKIs rely heavily on the integrity of the associated Certificate Authority and Registration Authority, which aren’t always functioning at the ideal level of diligence and scrutiny. 
- Another current security limitation of Public Key Infrastructures today (or rather, a security risk) is the obvious lack of multi-factor authentication on many of the top frameworks. 
- Furthermore, the overall usability of Public Key Infrastructure has never been ideal. More often than not, PKIs are so remarkably complicated that users would rather forgo the addition PKI authorization in exchange for a more convenient and realistic security process.
- Lastly, PKI technology is known for its inability to easily adapt to the ever-changing advancements of the digital world. Users report being unhappy with their current PKI’s lack of ability to support new applications that are geared toward improvements in security, convenience, and scalability.

## X.509 

The X.509 standard is what defines the format of digital certificates. It also defines a certificate
revocation list or CRL which is a means to distribute a list of certificates that are no longer valid. The
X.509 standard was first issued in 1988 and the current modern version of the standard is version 3.
The fields defined in X.509 certificate are - 
- Version, what version of the X.509 standard certificate
adheres to.
- Serial number, a unique identifier for their certificate assigned by the CA which allows the CA to
manage and identify individual certificates.
- Certificate Signature Algorithm, this field indicates what public key algorithm is used for the public
key and what hashing algorithm is used to sign the certificate.
- Issuer Name, this field contains information about the authority that signed the certificate.
- Validity, this contains two subfields, Not Before and Not After, which define the dates when the
certificate is valid for.
- Subject, this field contains identifying information about the entity the certificate was issued to.
- Subject Public Key Info, these two subfields define the algorithm of the public key along with the
public key itself.
- Certificate signature algorithm, same as the Subject Public Key Info field, these two fields must
match.
- Certificate Signature Value, the digital signature data itself.


