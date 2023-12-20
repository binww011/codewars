def find_next_square(n):
  if not (n**(1/2))%1:
    nxt = n+1
    while (nxt**(1/2))%1:
      nxt += 1
    return nxt
  else:
    return -1
