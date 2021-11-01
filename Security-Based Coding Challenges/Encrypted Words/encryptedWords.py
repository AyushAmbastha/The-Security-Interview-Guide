def findEncryptedWord(s):
    # Write your code here
    if len(s) < 3:
        return s
    else:
        if len(s) % 2 :
            mid = len(s)//2
            left = mid
            right = mid + 1
        else:
            mid = len(s)//2 - 1
            left = mid
            right = mid + 1
        return "" + s[mid] + findEncryptedWord(s[0:left]) + findEncryptedWord(s[right:len(s)])

print(findEncryptedWord("abc"))
print(findEncryptedWord("abcd"))
print(findEncryptedWord("abcxcba"))
print(findEncryptedWord("facebook"))