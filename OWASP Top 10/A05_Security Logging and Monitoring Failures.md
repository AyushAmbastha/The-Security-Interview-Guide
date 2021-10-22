# Security Logging and Monitoring Failures 

## Description

This category is to help detect, escalate, and respond to active breaches. Without logging and monitoring, breaches cannot be detected.

1. The application cannot detect, escalate, or alert for active attacks in real-time or near real-time.
2. Auditable events, such as logins, failed logins, and high-value transactions, are not logged.
3. Logs of applications and APIs are not monitored for suspicious activity.
4. Warnings and errors generate no, inadequate, or unclear log messages.
5. If you make the logging and alerts visible to users(attackers), you are vulnerable to information leakage.

## Prevention

1. Ensure all login, access control, and server-side input validation failures can be logged with sufficient user context to identify suspicious or malicious accounts and held for enough time to allow delayed forensic analysis.
2. Ensure that logs are generated in a format that log management solutions can easily consume.
3. Ensure log data is encoded correctly to prevent injections or attacks on the logging or monitoring systems.
4. Ensure high-value transactions have an audit trail with integrity controls to prevent tampering or deletion, such as append-only database tables or similar.
5. Establish or adopt an incident response and recovery plan.

## Example Attack Scenarios

<ins>Insufficient Real-Time Monitoring</ins>

A major Indian airline had a data breach involving more than ten years' worth of personal data of millions of passengers, including passport and credit card data. The data breach occurred at a third-party cloud hosting provider, who notified the airline of the breach after some time.

<ins>Insufficient Logging</ins>
 
A health app that had millions of patient records was hacked using a known exploit. But the system logs weren't good enough to detect how the attackers gained access to the system. By the time the developers fixed the vulnerability, more than 10,000 patient records were erased. One thing to keep in mind is that this could've been happening for many years before it was finally patched. 
