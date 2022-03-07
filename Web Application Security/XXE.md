# XML External Entity

An XML External Entity attack is a type of attack against an application that parses XML input. This attack occurs when XML input containing a reference to an external entity is processed by a weakly configured XML parser. This attack may lead to the disclosure of confidential data, denial of service, server side request forgery, port scanning from the perspective of the machine where the parser is located, and other system impacts.

The XML 1.0 standard defines the structure of an XML document. The standard defines a concept called an entity, which is a storage unit of some type. An external entity is one of the types of entities that can access local or remote content via a declared system identifier. The system identifier is assumed to be a URI that can be dereferenced (accessed) by the XML processor when processing the entity. The XML processor then replaces occurrences of the named external entity with the contents dereferenced by the system identifier. For example:

```
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [
    <!ELEMENT foo ANY>
    <!ENTITY xxe SYSTEM "file:///home/myuser/world.txt">
]>
<foo>Hello &xxe;</foo>
```

Assuming the file `/home/myuser/world.txt` exists and contains the string `World`, this example will give the output `Hello World`.

If the system identifier contains tainted data and the XML processor dereferences this tainted data, the XML processor may disclose confidential information normally not accessible by the application. Attacks can include disclosing local files, which may contain sensitive data such as passwords or private user data, using file: schemes or relative paths in the system identifier. Since the attack occurs relative to the application processing the XML document, an attacker may use this trusted application to pivot to other internal systems, possibly disclosing other internal content via http(s) requests or launching a CSRF attack to any unprotected internal services. In some situations, an XML processor library that is vulnerable to client-side memory corruption issues may be exploited by dereferencing a malicious URI, possibly allowing arbitrary code execution under the application account. Other attacks can access local resources that may not stop returning data, possibly impacting application availability if too many threads or processes are not released.

Note that the application does not need to explicitly return the response to the attacker for it to be vulnerable to information disclosures. An attacker can leverage DNS information to exfiltrate data through subdomain names to a DNS server that they controls.

### Resource Exhaustion Attacks
The XML-based denial of service attack, also known as the Billion Laughs Attack or XML bomb relies on combining multiple XML entities that reference each other. For example:

```
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE bomb [
    <!ELEMENT bomb ANY>
    <!ENTITY fun "haha">
    <!ENTITY fun1 "&fun;&fun;&fun;&fun;&fun;&fun;&fun;&fun;">
    <!ENTITY fun2 "&fun1;&fun1;&fun1;&fun1;&fun1;&fun1;&fun1;&fun1;">
    <!ENTITY fun3 "&fun2;&fun2;&fun2;&fun2;&fun2;&fun2;&fun2;&fun2;">
    <!-- repeat many more times -->
]>
<bomb>&fun3;</bomb>
```
As the XML parser expands each entity, it creates new instances of the first entity at an exponential rate. Even in this short example, the string haha would be generated 83 = 512 times. If parser resources are not capped, this type of attack can quickly exhaust server memory by creating billions of entity instances. This example doesn't use an external entity. 

Another way to achieve resource exhaustion is to inject an external entity that references an endless stream of data, such as /dev/urandom on Linux systems. Note the use of the SYSTEM identifier to specify an external entity:
```
<?xml  version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [
    <!ELEMENT foo ANY>
    <!ENTITY xxe SYSTEM "file:///dev/urandom">
]>
<foo>&xxe;</foo>
```
Again, if uncapped, the XML parser could lock up the server by exhausting its memory to store the never-ending data. Apart from resource capping, parsers can be protected from such attacks by enabling lazy expansion to only expand entities when they are actually used.

### Data Extraction Attacks
External entities can reference URIs to retrieve content from local files or network resources. By referencing a known (or likely) filename on the local system, an attacker can gain access to local resources, such as configuration files or other sensitive data:
```
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE foo [
    <!ELEMENT foo ANY>
    <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<foo>&xxe;</foo>
```

On a Linux system, this would return the content of the password file. For Windows, you could reference file:///c:/boot.ini or another common system file. Relative paths can also be used.

The same approach can be used to retrieve remote content from the local network, even from hosts that are not directly accessible to the attacker. This example attempts to retrieve the file mypasswords.txt from the host at IP 192.168.0.1:
```
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE foo [
    <!ELEMENT foo ANY>
    <!ENTITY xxe SYSTEM "http://192.168.0.1/mypasswords.txt">
]>
<foo>&xxe;</foo>
```

### SSRF Attacks
By exploiting an XXE vulnerability, attackers can gain indirect access to an internal network and launch attacks that appear to originate from a trusted internal server. Here’s an example of server-side request forgery using an XXE payload:
```
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE foo [
    <!ELEMENT foo ANY>
    <!ENTITY xxe SYSTEM "http://internal-system.example.com/">
]>
<foo>&xxe;</foo>
```
If executed on a web server, this could allow the attacker to send HTTP requests to an internal system, providing a foothold for further attacks.

## Preventing XML External Entity Attacks

XML external entity attacks rely on legacy support for Document Type Definitions. Thus, disabling DTD support is the best way of eliminating XXE vulnerabilities. If that’s not possible, you can disable just the external entity support – in PHP, for example, this is done by setting libxml_disable_entity_loader(true). 

To check your web applications for XXE vulnerabilities, use a reliable and accurate web application scanner.