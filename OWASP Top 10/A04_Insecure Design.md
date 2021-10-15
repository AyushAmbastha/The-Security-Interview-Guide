# Insecure Design 

## Description

Insecure design is a broad category representing different weaknesses, expressed as “missing or ineffective control design.” Insecure design is not the source for all other Top 10 risk categories. 

There is a difference between insecure design and insecure implementation,they have different root causes and remediation. A secure design can still have implementation defects leading to vulnerabilities that may be exploited. An insecure design cannot be fixed by a perfect implementation. One of the reasons why insecure designs exist is because of incorrect risk profiling of the software being developed, and thus the failure to determine what level of security design is required.

## Prevention

1. Establish and use a secure development lifecycle to help evaluate and design security and privacy-related controls

2. Establish and use a library of secure design patterns or paved road ready to use components

3. Use threat modeling for critical authentication, access control, business logic, and key flows

4. Integrate security language and controls into user stories

5. Integrate plausibility checks at each tier of your application (from frontend to backend)

6. Write unit and integration tests to validate that all critical flows are resistant to the threat model. Compile use-cases and misuse-cases for each tier of your application.

7. Segregate tier layers on the system and network layers depending on the exposure and protection needs

8. Segregate tenants robustly by design throughout all tiers

9. Limit resource consumption by user or service

## Example Attack Scenarios

<ins>Movie tickets</ins>

If a movie theatre allows booking group tickets and does not require a deposit if the group has less than 10 people. An attacker can block the entire theatre by booking the seats in pairs of 9, and the website will show the entire theatre booked out to real customers. This is because the authorities didn't consider this attack vector/didn't give it enough importance, causing a massive loss of income. 

