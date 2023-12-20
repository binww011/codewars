from preloaded import MORSE_CODE

def decode_morse(morse_code):
  init = 0
  
  for char in morse_code:
    if char == " ":
      init += 1
    else:
      break
  
  end = len(morse_code)
  
  for i in range(0, end):
    if morse_code[end - 1] == " ":
      end -= 1
    else:
      break
  
  words = morse_code[init:end].split("   ")
  res = ""
  i = 0
  for word in words:
    for char in word.split(" "):
      res += MORSE_CODE[char]
      i += 1
      if i != len(words):
        res += " "
  return res
