# Cert transparency

Certificate Transparency is an open framework for monitoring SSL Certificates. Domain owners may find it useful to monitor certificate issuance for their domain and use that to detect misissued certificates. Prior to CT, there was not an efficient way to get a comprehensive list of certificates issued to your domain. 

With CT, all certificates are publicly disclosed, providing greater insight and transparency into the Web PKI ecosystem as a whole. The Certificate Transparency Project aims to achieve three goals: 
1. To make it impossible (or at least very difficult) for a CA to issue a SSL Certificate for a domain without the certificate being visible to the owner of that domain.
2. To provide an open auditing and monitoring system that lets any domain owner or CA determine whether certificates have been mistakenly or maliciously issued.
3. To protect users from being duped by certificates that were mistakenly or maliciously issued. 

The Certificate Transparency framework means misissued certificates can be detected quickly and efficiently as  compared to the old system where rogue certificates could be left in the wild to wreak havoc for weeks or months before being discovered. Early detection of suspect certificates allows CAs and domain owners alike to act quickly and revoke the certificates.  

The main two CT components are the CT logs and Monitors.   
 - **CT logs** maintain records of issued SSL Certificates. These logs are append-only, meaning entries can’t be deleted or altered in any way once a certificate has been added to a log.  SSL Certificates and precertificates (more on this below) may be posted to CT logs.  Upon receipt of a valid SSL Certificate or precertificate, the log returns a Signed Certificate Timestamp (SCT), which is proof that the log received the request.  
- **Monitors** query CT logs and can download and store certificates for subsequent reporting.  Monitors will parse the certificates into subfields and allow their users to create and run queries for certificates.  Domain owners may be interested in receiving notices for certificates issued to their domains, or for certificates that match their Organizational name, while compliance teams may be looking for compliance with the CA/Browser Forum Baseline Requirements or Root Program requirements.  Regardless, there are many purposes for Monitors.  
  
Precertificates - CT logs accept SSL precertificates and certificates.  A precertificate contains all the same data as the “real” certificate, but also contains one additional extension that makes the certificate unusable.  This extension is referred to as a poison extension and is used to distinguish it from the “real” certificate.  Since all certificates issued by a CA must contain unique serial numbers, and since both the precertificate and certificate will have the same serial number, it’s important to make one of them as invalid or not usable, thus the poison extension. 