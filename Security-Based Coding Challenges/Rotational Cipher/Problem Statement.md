# Rotational Cipher

One simple way to encrypt a string is to "rotate" every alphanumeric character by a certain amount. Rotating a character means replacing it with another character that is a certain number of steps away in normal alphabetic or numerical order.

For example, if the string "Zebra-493?" is rotated 3 places, the resulting string is "Cheud-726?". Every alphabetic character is replaced with the character 3 letters higher (wrapping around from Z to A), and every numeric character replaced with the character 3 digits higher (wrapping around from 9 to 0). Note that the non-alphanumeric characters remain unchanged.

Given a string and a rotation factor, return an encrypted string.

<ins>Signature</ins>

string rotationalCipher(string input, int rotationFactor)

<ins>Input</ins>

1 <= |input| <= 1,000,000

0 <= rotationFactor <= 1,000,000

<ins>Output</ins>

Return the result of rotating input a number of times equal to rotationFactor.

<ins>Example 1</ins>

input = Zebra-493?

rotationFactor = 3

output = Cheud-726?

<ins>Example 2</ins>

input = abcdefghijklmNOPQRSTUVWXYZ0123456789

rotationFactor = 39

output = nopqrstuvwxyzABCDEFGHIJKLM9012345678