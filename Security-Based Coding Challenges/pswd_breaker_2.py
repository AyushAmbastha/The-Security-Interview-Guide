import hashlib
from urllib.request import urlopen
 
def readwordlist(url):
    try:
        wordlistfile = urlopen(url).read()
    except Exception as e:
        print("Hey there was some error while reading the wordlist, error:", e)
        exit()
    return wordlistfile
 
def hash(wordlistpassword):
    result = hashlib.sha1(wordlistpassword.encode())
    return result.hexdigest()
 
 
def bruteforce(guesspasswordlist, actual_password_hash):
    for guess_password in guesspasswordlist:
        if hash(guess_password) == actual_password_hash:
            print("Hey! your password is:", guess_password,
                  "\n please change this, it was really easy to guess it (:")
            # If the password is found then it will terminate the script here
            exit()
 
############# append the below code ################ 

url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'
actual_password = 'Amby'
actual_password_hash = hash(actual_password)
 
wordlist = readwordlist(url).decode('UTF-8')
guesspasswordlist = wordlist.split('\n')
 
# Running the Brute Force attack
bruteforce(guesspasswordlist, actual_password_hash)
 
# It would be executed if your password was not there in the wordlist
print("Hey! I couldn't guess this password, it was not in my wordlist, this is good news! you win (: ")

#---------------------------------------------------------------

#To generate your own wordlist 
from itertools import chain, product

def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i) for i in range(1, maxlength + 1)))
        # .from_iterable will flatten the lists out -> [a,b,c],[e,f],[g] => [a,b,c,d,e,f,g]
        # product('abcd',2) => aa,ab,ac,ad,ba ...
        # each will be in a different list so we need from_iterable to make it one big list
    
print(list(bruteforce('abcde',2)))