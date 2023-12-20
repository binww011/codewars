def narcissistic(value):
  sum = 0
  for i in str(value):
    sum += int(i)**len(str(value))
  return sum == value
