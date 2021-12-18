# Injection

## Description

When user supplied data is not sanitized or validated and is used directly, it leaves the application 
vulnerable to injection attacks. 
This is a technique used for database manipulation and to access information one should not have access to. 
This information may include any number of items, including sensitive company data, user lists or private customer details.

## Example Attack Scenarios

<ins>SQL injection to Bypass Authentication</ins>

Consider the following SQL query - 

`SELECT * FROM ACCOUNT_DETAILS WHERE ACCOUNT_ID='<USER ENTERED ID>' AND PASSWORD='<USER ENTERED PASSWORD>';`

If an attacker enters `' or 1=1 --` in the Username field, the query now becomes 

`SELECT * FROM ACCOUNT_DETAILS WHERE ACCOUNT_ID='' or 1=1 --`

There are two things to notice here - 
1. Because of the comment sequence (--), the rest of the query is ignored.
2. WHERE ACCOUNT_ID='' or 1=1 will always result in TRUE.

When the attacker attempts to login using the SQLi mentioned above, the entire ACCOUNT_DETAILS database is displayed.

<ins>Denial of Service using Batched statements</ins>

Consider the following SQL query - 

`SELECT * FROM USER_DETAILS WHERE USER_ID= <USER ENTERED ID>;`

If an attacker enters `100; DROP TABLE ACCOUNT_DETAILS;` in the ID field, the query now becomes

`SELECT * FROM USER_DETAILS WHERE USER_ID=100; DROP TABLE ACCOUNT_DETAILS;`

This query will not just return the details of User ID 100 but also delete the entire ACCOUNT_DETAILS table. 
And if any future query tries to access information in that table it wont work, and hence will cause a denial of service.