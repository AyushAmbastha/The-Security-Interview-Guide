import re

p = re.compile('[abcd]+')

print(p.match("abcdefg").group()) #Only matches from the start of a string
print(p.search("123445abcdefg").group()) #Matches anywhere in the string

#In programs, you store the match obj in a variable and check if it is empty

m = p.match( 'string goes here' )
if m:
    print('Match found: ', m.group())
else:
    print('No match')

y = p.findall('12 abcd drummers drumming, 11 aaaa pipers piping, 10 afsefs lords a-leaping')
print(y) # List of matching strings

# ^ This above method needs to create a list before it returns anything. 

z = p.finditer('12 abcd drummers drumming, 11 aaaa pipers piping, 10 afsefs lords a-leaping')
print(z)
for match in z:
    print(match.group()) #See every match one by one

# Can do the regex thing in one step also, dont have to compile all the time
print(re.match(r'From\s+', 'Fromage amk')) #None