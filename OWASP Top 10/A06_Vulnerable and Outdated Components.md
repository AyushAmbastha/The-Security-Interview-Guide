# Vulnerable and Outdated Components

## Description

If you do not scan for vulnerabilities or do not fix/upgrade components in a timely fashion, you are likely vulnerable to this. Other examples of a situation in which you are likely impacted by this is if you do not know the versions of all components you use, if software is vulnerable, unsupported, or out of date, if you do not test the compatibility of updated, upgraded, or patched libraries.

## Prevention

A patch management system to -
1. Remove unused dependencies, unnecessary features, components, files, and documentation.
2. Continuously inventory the versions of the software used in both client and server side. 
3. Monitor for libraries and components that are unmaintained or do not create security patches for older versions.

## Example Attack Scenarios

OWASP WebGoat uses a vulnerable version of the Xstream library to transform an XML document into a Java object. In the pom.xml file, we notice that the library’s version 1.4.5. Looking for public exploits on the internet reveals that this version suffers from a severe deserialization vulnerability, which leads to remote code execution.