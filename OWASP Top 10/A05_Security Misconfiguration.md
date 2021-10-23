# Security Misconfiguration

## Description

Misconfiguration normally happens when a system or database administrator or developer does not properly configure the security framework of an application, website, desktop, or server leading to dangerous open pathways for hackers.

These vulnerabilities are configuration weaknesses that may exist in software components or subsystems. For example, web server software may ship with default user accounts that an attacker can use to access the system.

## Prevention

1. Do not use vendor-supplied defaults for system passwords and other security parameters.
2. Disable debugging and administration interfaces.
2. Protect all systems against malware and regularly update software.
3. Configure server to prevent unauthorized access, directory listing
4. Configure a security policy to deny requests for certain file types. Doing so allows you to create a set of files on your site that you don't want users to access.

## Example Attack Scenarios

1. Directory listing is not disabled on the server. An attacker discovers they can simply list directories and view files, that leads to information disclosure.
2. The application server's configuration allows detailed error messages, e.g., stack traces, to be returned to users. This potentially exposes sensitive information or underlying flaws such as component versions that are known to be vulnerable.
3. A cloud service provider has default sharing permissions open to the Internet by other Content Security Policy header (CSP) users. This allows sensitive data stored within cloud storage to be accessed.

