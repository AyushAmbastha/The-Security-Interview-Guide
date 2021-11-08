### What is a CVE?

CVE, short for Common Vulnerabilities and Exposures, is a list of publicly disclosed computer security flaws. When someone refers to a CVE, they mean a security flaw that's been assigned a CVE ID number. CVEs help IT professionals coordinate their efforts to prioritize and address these vulnerabilities to make computer systems more secure. CVE identifiers are assigned by a CVE Numbering Authority (CNA).

CVE entries are brief. They don’t include technical data, or information about risks, impacts, and fixes. Those details appear in other databases, including the U.S. National Vulnerability Database (NVD), the CERT/CC Vulnerability Notes Database, and various lists maintained by vendors and other organizations. Across these different systems, CVE IDs give users a reliable way to tell one unique security flaw from another.

CVE IDs are assigned to flaws that meet a specific set of criteria. They must be:

1. Independently fixable.  
    The flaw can be fixed independently of any other bugs.

2. Acknowledged by the affected vendor OR documented.  
    The software or hardware vendor acknowledges the bug and that it has a negative impact on security. Or, the reporter must have shared a vulnerability report that demonstrates the negative impact of the bug AND that it violates the security policy of the affected system.

3. Affecting one codebase.  
    Flaws that impact more than one product get separate CVEs. In cases of shared libraries, protocols or standards, the flaw gets a single CVE only if there’s no way to use the shared code without being vulnerable. Otherwise each affected codebase or product gets a unique CVE.