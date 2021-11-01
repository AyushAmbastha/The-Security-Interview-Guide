def rotationalCipher(input, rotation_factor):
  # Write your code here
  if not input or not rotation_factor:
    return input
  
  capAlphabets = [chr(c) for c in range(ord('A'), ord('Z') + 1)]
  alphabets = [chr(c) for c in range(ord('a'), ord('z') + 1)]   

  res = []
  for c in input:
    if not c.isalnum():
      res.append(c)

    elif c.isalpha():
      if c.isupper():
        ind = capAlphabets.index(c) + rotation_factor
        if ind > 25:
          ind = ind % 26
        res.append(capAlphabets[ind])

      else:
        ind = alphabets.index(c) + rotation_factor
        if ind > 25:
          ind = ind % 26
        res.append(alphabets[ind])

    elif c.isdigit():
      new = str(int(c) + rotation_factor)[-1]
      res.append(new)


  return "".join(c for c in res)

input1 = "Zebra-493?"
rotationFactor1 = 3
print(rotationalCipher(input1, rotationFactor1))

input2 = "abcdefghijklmNOPQRSTUVWXYZ0123456789"
rotationFactor2 = 39
print(rotationalCipher(input2, rotationFactor2))