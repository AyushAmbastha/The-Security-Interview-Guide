# Broken Access Control

## Description

Access control enforces policy such that users cannot act outside of their intended permissions. 
Failures typically lead to unauthorized information disclosure, modification, or destruction of all 
data or performing a business function outside the user's limits. 

## Example Attack Scenarios 

<ins>Scenario 1: Forced Browsing</ins>

An Attacker forces the browser to URLs that require admin privileges to view. These resources are not 
directly referenced in the application (you can't see any links to these resources) but are still available.

Users can access http://test.com/user_details

Attacker finds the admin page http://test.com/admin_details and attempts to view that.

If the attacker is able to view the admin page, access control is broken.

<ins>Scenario 2: Directory Traversal</ins> 

Sometimes websites store data in several files and hence has 'file' as a request parameter. 

Eg. For a website that display an image, the URL might look like http://test.com/images?file=dog.png

This is because there is a folder on the server side with this image in it and it simply fetches 
it from there.
An Attacker can abuse this by using multiple ../ (terminal command to go one directory back) to 
eventually reach the root folder.

So by entering http://test.com/images?file=../../../../etc/passwd , an attacker has access to sensitive 
information and can access any file from there. 

<ins>Scenario 3: Insecure IDs</ins>

The above scenario dealt with websites that use files to display images/text. What if the website is using a database?
Often, they use a unique user ID to access that user's particular files. 

The URL might look like http://test.com?profile?id=5 

What if I changed the URL to http://test.com?profile?id=6 instead? You'll be able to see another user's senstitive data, 
records you shouldn't have access to.  

Using a random user ID makes it slightly harder to exploit this flaw and isn't the best way to fix it.
