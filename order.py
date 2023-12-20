def order(sentence):
  res = ''
  tmp = sentence.split(' ')
  for i in range(1, len(tmp)+1):
    for e in tmp:
      if e.count(str(i)) > 0:
        res += e
    if i < len(tmp):
      res += ' '
  return res
