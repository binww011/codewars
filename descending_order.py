def descending_order(num):
  l = [int(e) for e in list(str(num))]
  l.sort(reverse=True)
  return int(''.join([str(e) for e in l]))
