# SQL Injection 

SQL Injection (SQLi) is a type of injection attack that makes it possible to execute malicious SQL statements. These statements control a database server behind a web application. Attackers can use SQL Injection vulnerabilities to bypass application security measures. They can go around authentication and authorization of a web page or web application and retrieve the content of the entire SQL database. They can also use SQL Injection to add, modify, and delete records in the database.
An SQL Injection vulnerability may affect any website or web application that uses an SQL database such as MySQL, Oracle, SQL Server, or others. Criminals may use it to gain unauthorized access to your sensitive data: customer information, personal data, trade secrets, intellectual property, and more.
SQL Injection flaws are introduced when software developers create dynamic database queries that include user-supplied input. To avoid SQL injection flaws is simple. Developers need to either: a) stop writing dynamic queries; and/or b) prevent user-supplied input that contains malicious SQL from affecting the logic of the executed query.
Primary Defenses:
Option 1: Use of Prepared Statements (with Parameterized Queries)
Option 2: Use of Stored Procedures
Option 3: Allow-list Input Validation
Option 4: Escaping All User Supplied Input
