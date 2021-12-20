# Ceasar Cipher

One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order. This is called the Ceasar Cipher.

For example, if the string "Zebra-493?" is shifted 3 places, the resulting string is "Cheud-726?". Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A), and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0). Note that the non-alphanumeric characters remain unchanged.

Given a string and a rotation factor/shift, return an encrypted string.

<ins>Signature</ins>

string ceasarCipher(string text, int shift)

<ins>Input</ins>

1 <= |text| <= 1,000,000

0 <= shift <= 1,000,000

<ins>Output</ins>

Return the result of rotating text a number of times equal to shift.

<ins>Example 1</ins>

text = Zebra-493?

shift = 3

cipherText = Cheud-726?

<ins>Example 2</ins>

text = abcdefghijklmNOPQRSTUVWXYZ0123456789

shift = 39

cipherText = nopqrstuvwxyzABCDEFGHIJKLM9012345678