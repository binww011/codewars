def duplicate_count(text):
  strg = text.lower()
  sumi = 0
  cache = []
  for char in strg:
    if cache.count(char) == 0:
      if strg.count(char) > 1:
        sumi += 1
        cache.append(char)
  return sumi
