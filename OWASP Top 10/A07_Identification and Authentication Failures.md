The terms Identification and Authentication are often used synonymously, although they are two distinct activities. 

**Identification** is the ability to identify uniquely a user of a system or an application that is running in the system. 
**Authentication** is the ability to prove that the user or application is genuinely who they claim to be.

Both processes are usually a part of a 2-step process, with identification taking place before authorization. However, they can be stand alone depending on the nuances of the system.
For example, consider a user who logs on to a system by entering their user ID and password. The system uses the user ID to **identify** the user. It then **authenticates** the user by checking that the password is correct and belongs to that user.

Example Attack Scenarios - 

Scenario #1: Credential stuffing, the use of stolen username-password pairs in website login forms, is a common attack where the application is used as a password oracle to determine if the credentials are valid.

Scenario #2: Authentication attacks that occur due to the continued use and reuse of weak passwords due to complex password requirements by websites and applications.

Scenario #3: Incorrect application session timeouts that could lead to a user staying logged on to a website if they simply chose to close the browser tab instead of logging out on a public system. An attacker could use the same browser an hour later, and the user would still be authenticated.

Confirmation of a user's identity, authentication, and session management is critical to protect against authentication-related attacks. Failures occur when the application - 

- Permits automated attacks such as credential stuffing and brute forcing.
- Permits default, weak, or well-known passwords, such as "Password1" or "admin/admin".
- Uses a weak or ineffective credential recovery process, such as security questions which can be answered by some knowledge of the user.
- Uses plain text, encrypted, or weakly hashed passwords data stores.
- Has missing or ineffective multi-factor authentication.
- Exposes session identifier in the URL.
- Reuses session identifier after successful login.
- Does not correctly invalidate Session IDs after logout or a period of inactivity.

How do we prevent these failures ?

- Implement multi-factor authentication to prevent automated credential stuffing, brute force, and stolen credential reuse attacks.
- Do not ship or deploy with any default credentials or ensure these are one-time credentials that are changed after the user's first login.
- Implement a password policy to ensure weak password checks, such as testing new or changed passwords against the top 10,000 worst passwords list.
- Ensure registration, credential recovery, and API pathways are hardened against account enumeration attacks by using the same messages for all outcomes.
- Limit or increase the delay between failed login attempts, but ensure to not create a denial of service scenario. Log all failures and alert administrators when credential stuffing, brute force, or other attacks are detected.
- Use a server-side, secure, built-in session manager that generates a new random session ID with high entropy after login. Session identifier should not be in the URL, be securely stored, and invalidated after logout, idle, and absolute timeouts.
