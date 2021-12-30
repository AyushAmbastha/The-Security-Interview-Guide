# Access Control Models
After a user is authenticated to an application, the tasks that a user is authorized to perform can be determined in one of several ways:

**Mandatory access control (MAC)**\
 Mandatory access control establishes strict security policies for individual users and the resources, systems, or data they are allowed to access. These policies are controlled by an administrator; individual users are not given the authority to set, alter, or revoke permissions in a way that contradicts existing policies.

Under this system, both the subject (user) and the object (data, system, or other resource) must be assigned similar security attributes in order to interact with each other. Consider the example where a bank’s president is authorized to access customer data files. Here the system administrator would also need to specify that those files can be viewed and altered by the president. While that process may seem redundant, it ensures that users cannot perform unauthorized actions simply by gaining access to certain data or resources.

**Role-based access control (RBAC)**\
Role-based access control establishes permissions based on groups (defined sets of users, such as bank employees) and roles (defined sets of actions, like those that a bank teller or a branch manager might perform). Individuals can perform any action that is assigned to their role, and may be assigned multiple roles as necessary. Like MAC, users are not permitted to change the level of access control that has been assigned to their role.

For instance, any bank employee assigned to the role of bank teller might be given the authorization to process account transactions and open new customer accounts. A branch manager, on the other hand, might hold several roles, authorizing them to process account transactions, open customer accounts, assign the role of bank teller to a new employee, and so on.

**Rule-Based Access Control**\
Rule Based Access Control allows system owners to personalise the type of access a user has based on their role within an organisation.

Users can be grouped into roles based on their responsibilities within an organisation as this generally determines their system access needs. Access is then granted to each user based on the access requirements established for each role. For example, if someone is only allowed access to files during certain hours of the day, Rule-Based Access Control would be the tool of choice.

**Discretionary access control (DAC)**\
Once a user is given permission to access an object (usually by a system administrator or through an existing access control list), they can grant access to other users on an as-needed basis. This may introduce security vulnerabilities, however, as users are able to determine security settings and share permissions without strict oversight from the system administrator.

When evaluating which method of user authorization is most appropriate for an organization, security needs must be taken into account. Typically, organizations that require a high level of data confidentiality (e.g. government organizations, banks, etc.) will opt for more stringent forms of access control, like MAC, while those that favor more flexibility and user or role-based permissions will tend toward RBAC and DAC systems.

## Methods for implementing access control

**VPNs**\
A popular tool for information access control is a virtual private network (VPN). A VPN is a service that allows remote users to access the Internet as though they were connected to a private network. Corporate networks will often use VPNs to manage access control to their internal network across a geographic distance.

For example, if a company has an office in San Francisco and another office in New York, as well as remote employees scattered across the globe, they can use a VPN so that all of their employees can securely log into their internal network, regardless of their physical location. Connecting to the VPN will also help protect the employees against on-path attacks if they are connected to a public WiFi network.

VPNs also come with some drawbacks. For example, VPNs negatively impact performance and increase latency. When connected to a VPN, every data packet a user sends or receives has to travel an extra distance before arriving at its destination, as each request and response has to hit the VPN server before reaching its destination. VPNs generally provide an all-or-nothing approach to network security. VPNs are great at providing authentication, but not great at providing granular authorization controls. If an organization wants to grant different levels of access to different employees, they have to use multiple VPNs. This creates a lot of complexity, and still doesn’t satisfy the requirements of zero trust security.

**Access Control Lists**\
Access Control Lists (ACLs) are permissions attached to an object such as a spreadsheet file, that a system will check to allow or deny control to that object. These permissions range from full control to read-only to “access denied.” When it comes to the various operating systems (i.e., Windows, Linux, Mac OS X), the entries in the ACLs are named “access control entry,” or ACE, and are configured via four pieces of information: a security identifier (SID), an access mask, a flag for operations that can be performed on the object and another set of flags to determine inherited permissions of the object. So, as one can see, ACLs provide detailed access control for objects. However, they can become cumbersome when changes occur frequently and one needs to manage many objects.

**Group Policies**\
Group policies are part of the Windows environment and allow for centralized management of access control to a network of computers utilizing the directory services of Microsoft called Active Directory. This eliminates the need to go to each computer and configure access control. These settings are stored in Group Policy Objects (GPOs) which make it convenient for the system administrator to be able to configure settings. Although convenient, a determined hacker can get around these group policies and make life miserable for the system administrator or custodian.

**Password**\
Passwords are the most common access control method. However, they need to be tough to hack to provide an essential level of access control. If one makes the password easy to guess or uses a word in the dictionary, they can be subject to brute force attacks, dictionary attacks or other attacks using rainbow tables. Keeping this in mind, experts agree that the longer the password is, the harder it is to crack, provided the user remembers it and uses many different characters and non-keyboard type characters in creating it. Utilizing this concept also makes it more difficult for a hacker to crack the password with the use of rainbow tables. Having a two-factor authentication (such as a smart card with a password) can make things more secure, especially with technology advancing to the point where cracking passwords can take only seconds. 

**Account Restrictions**\
The two most common account restrictions are time of day restrictions and account expiration. Time of day restrictions can ensure that a user has access to certain records only during certain hours. This would make it so that administrators could update records at night without interference from other users. Account expirations are needed to ensure unused accounts are no longer available so hackers cannot possibly utilize them for any “dirty work.”

## Zero Trust Security
Zero trust security is an IT security model that requires strict identity verification for every person and device trying to access resources on a private network, regardless of whether they are sitting within or outside of the network perimeter. Zero trust networks also utilize microsegmentation. Microsegmentation is the practice of breaking up security perimeters into small zones to maintain separate access for separate parts of the network.