def array_diff(a, b):
  for e in b:
    if a.count(e) > 0:
      a = [x for x in a if x != e]
  return a
