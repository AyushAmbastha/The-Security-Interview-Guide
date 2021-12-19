def caesarCipher(text, shift):
  # Write your code here
  if not text or not shift:
    return input
  
  capAlphabets = [chr(c) for c in range(ord('A'), ord('Z') + 1)]
  alphabets = [chr(c) for c in range(ord('a'), ord('z') + 1)]   

  cipherText = []
  for c in text:
    if not c.isalnum():
      cipherText.append(c)

    elif c.isalpha():
      if c.isupper():
        ind = capAlphabets.index(c) + shift
        if ind > 25:
          ind = ind % 26
        cipherText.append(capAlphabets[ind])

      else:
        ind = alphabets.index(c) + shift
        if ind > 25:
          ind = ind % 26
        cipherText.append(alphabets[ind])

    elif c.isdigit():
      new = str(int(c) + shift)[-1]
      cipherText.append(new)


  return "".join(c for c in cipherText)

text1 = "Zebra-493?"
shift1 = 3
print(caesarCipher(text1, shift1))

text2 = "abcdefghijklmNOPQRSTUVWXYZ0123456789"
shift2 = 39
print(caesarCipher(text2, shift2))