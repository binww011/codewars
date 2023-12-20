def longest(a, b):
  res = ""
  for i in a:
    if i not in res:
      res += i
  for i in b:
    if i not in res:
      res += i
  return "".join(sorted(res))
