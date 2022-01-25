# Systems Hardening

Systems hardening is a collection of tools, techniques, and best practices to reduce vulnerability in technology applications, systems, infrastructure, firmware, and other areas. The goal of systems hardening is to reduce security risk by eliminating potential attack vectors and condensing the system’s attack surface. By removing superfluous programs, accounts functions, applications, ports, permissions, access, etc. attackers and malware have fewer opportunities to gain a foothold within your IT ecosystem.

Systems hardening demands a methodical approach to audit, identify, close, and control potential security vulnerabilities throughout your organization. There are several types of system hardening activities, including:
- Application hardening
- Operating system hardening
- Server hardening
- Database hardening
- Network hardening

Although the principles of system hardening are universal, specific tools and techniques do vary depending on the type of hardening you are carrying out. System hardening is needed throughout the lifecycle of technology, from initial installation, through configuration, maintenance, and support, to end-of-life decommissioning. Systems hardening is also a requirement of mandates such as PCI, DSS and HIPAA.

## Systems Hardening to Reduce the “Attack Surface”
The “attack surface” is the combination of all the potential flaws and backdoors in technology that can be exploited by hackers. These vulnerabilities can occur in multiple ways, including:
- Default and hardcoded passwords
- Passwords and other credentials stored in plain text files
- Unpatched software and firmware vulnerabilities
- Poorly configured BIOS, firewalls, ports, servers, switches, routers, or other parts of the infrastructure
- Unencrypted network traffic or data at rest
- Lack, or deficiency, of privileged access controls

## 9 Best Practices for Systems Hardening
The type of hardening you carry out depends on the risks in your existing technology, the resources you have available, and the priority for making fixes.

### **Audit your existing systems**
Carry out a comprehensive audit of your existing technology. Use penetration testing, vulnerability scanning, configuration management, and other security auditing tools to find flaws in the system and prioritize fixes. Conduct system hardening assessments against resources using industry standards from NIST, Microsoft, CIS, DISA, etc.

### **Create a strategy for systems hardening**
You do not need to harden all of your systems at once. Instead, create a strategy and plan based on risks identified within your technology ecosystem, and use a phased approach to remediate the biggest flaws.

### **Patch vulnerabilities immediately**
Ensure that you have an automated and comprehensive vulnerability identification and patching system in place.

### **Network hardening**
Ensure your firewall is properly configured and that all rules are regularly audited; secure remote access points and users; block any unused or unneeded open network ports; disable and remove unnecessary protocols and services; implement access lists; encrypt network traffic.

### **Server hardening**
Put all servers in a secure datacenter; never test hardening on production servers; always harden servers before connecting them to the internet or external networks; avoid installing unnecessary software on a server; segregate servers appropriately; ensure superuser and administrative shares are properly set up, and that rights and access are limited in line with the principle of least privilege.

### **Application hardening**
Remove any components or functions you do not need; restrict access to applications based on user roles and context (such as with application control); remove all sample files and default passwords. Application passwords should then be managed via an application password management/privileged password management solution, that enforces password best practices (password rotation, length, etc.). Hardening of applications should also entail inspecting integrations with other applications and systems, and removing, or reducing, unnecessary integration components and privileges.

### **Database hardening**
Create admin restrictions, such as by controlling privileged access, on what users can do in a database; turn on node checking to verify applications and users; encrypt database information—both in transit and at rest; enforce secure passwords; introduce role-based access control (RBAC) privileges; remove unused accounts;

### **Operating system hardening**
Apply OS updates, service packs, and patches automatically; remove unnecessary drivers, file sharing, libraries, software, services, and functionality; encrypt local storage; tighten registry and other systems permissions; log all activity, errors, and warnings; implement privileged user controls.

### **Eliminate unnecessary accounts and privileges**
Enforce least privilege by removing unnecessary accounts (such as orphaned accounts and unused accounts) and privileges throughout your IT infrastructure.

## Benefits of Systems Hardening
Systems hardening requires continuous effort, but the diligence will pay off in substantive ways across your organization via:
- Enhanced system functionality: Since fewer programs and less functionality means there is less risk of operational issues, misconfigurations, incompatibilities, and compromise.
- Significantly improved security: A reduced attack surface translates into a lower risk of data breaches, unauthorized access, systems hacking, or malware.
- Simplified compliance and auditability: Fewer programs and accounts coupled with a less complex environment means auditing the environment will usually be more transparent and straightforward.