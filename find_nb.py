def find_nb(m):
  n = 1
  while n**2 * (n+1)**2 // 4 != m and n**2 * (n+1)**2 // 4 < m:
    n += 1
  return n if n**2 * (n+1)**2 // 4 == m else -1
