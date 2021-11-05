### What is Secure Code Review?

Code review aims to identify security faws in the application related to its features and design, along with the
exact root causes. With the increasing complexity of applications and the advent of new technologies, the
traditional way of testing may fail to detect all the security flaws present in the applications. One must understand the code of the application, external components, and confgurations to have a better chance of finding
the flaws. Such a deep dive into the application code also helps in determining exact mitigation techniques
that can be used to avert the security faws.
It is the process of auditing the source code of an application to verify that the proper security and logical
controls are present, that they work as intended, and that they have been invoked in the right places.

Automation Tools - 
1. SourceClear
2. Snyk
3. Bandit
4. GoSec
5. Scorecard

Example Checklist/ Some questions you should consider while conducting a secure code review - 
1. Have you implemented proper authorization controls?
2. Have you implemented proper authentication controls? Do you have two-factor or multi-factor authentication in place?
3. Is sensitive data encrypted? How do you handle encryption keys?
4. Does the error message display sensitive information to the user?
5. Do you have other security controls in place that prevent SQL Injection, XSS attacks, malware, etc?