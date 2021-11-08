# Regular Expressions (RegEx)

### Metacharacters
List of metacharacters - 
```
. ^ $ * + ? { } [ ] \ | ( )
```

1. `[ ]` - They’re used for specifying a character class, which is a set of characters that you wish to match. Characters can be listed individually, or a range of characters can be indicated by giving two characters and separating them by a '-'. For example, [abc] will match any of the characters a, b, or c; this is the same as [a-c]  
    NOTE: Metacharacters are not active inside classes. For example, [akm$] will match any of the characters 'a', 'k', 'm', or '$'; '$' is usually a metacharacter, but inside a character class it’s stripped of its special nature.
2. `^` - [^5] will match any character except '5'
3. `\` - If you need to match a [ or \, you can precede them with a backslash to remove their special meaning: \[ or \\  
    Predefined sets of characters - 
    1. `\w` Matches any alphanumeric character. If the regex pattern is expressed in bytes, this is equivalent to the class [a-zA-Z0-9_].
    2. `\W` Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].
    3. `\d` Matches any decimal digit; this is equivalent to the class [0-9].
    4. `\D` Matches any non-digit character; this is equivalent to the class [^0-9].
    5. `\s` Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].
    6. `\S` Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].
4. `.` - Matches anything except a newline character. It is often used where you want to match “any character”.

### Repeating Things

1. `*` - It specifies that the previous character can be matched <ins>zero</ins> or more times, instead of exactly once.  
    Ex 1: `ca*t` will match 'ct' (0 'a' characters), 'cat' (1 'a'), 'caaat' (3 'a' characters), and so forth.  
    Ex 2: `a[bcd]*b` will match the letter 'a', zero or more letters from the class [bcd], and finally ends with a 'b'.
    NOTE: Repetitions such as * are greedy; when repeating a RE, the matching engine will try to repeat it as many times as possible. If later portions of the pattern don’t match, the matching engine will then back up and try again with fewer repetitions.
2. `+` - It specifies that the previous character can be matched <ins>one</ins> or more times.  
    Ex: `ca+t` will match 'cat' (1 'a'), 'caaat' (3 'a' characters), and so forth. It will not match 'ct'.
3. `?` - It specifies that the previous character can be matched <ins>zero or one</ins> times. Similar to making something optional.  
    Ex: `home-?brew` matches either 'homebrew' or 'home-brew'.
4. `{m,n}`, where m and n are decimal integers - This qualifier means there must be at least m repetitions, and at most n.  
    Ex: `a/{1,3}b` will match 'a/b', 'a//b', and 'a///b'. It won’t match 'ab', which has no slashes, or 'a////b', which has four.  
    NOTE: Omitting m is intepreted as lower limit of 0 and omitting n is intepreted as upper limit of infinity. You can express all of the above mentioned repetition qualifiers using {m,n} but it's simpler to use them instead.

### Backslash problems 

Let’s say you want to write a RE that matches the string \section.  
Since Regular Expressions (REs) are passed as strings and strings use \ for the same reason, the RE for \section will look like `\\\\section`. Which makes the RE difficult to understand and unnecessarily complex. 

The solution is to use the raw string notation in Python.  
`r"\n"` is a two character string containing \ and n, while `"\n"` is a one character string containing a newline character.
So `"\\\\section"` can be written as `r"\\section"`

