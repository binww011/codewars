def binary_array_to_number(arr):
  res = 0
  for i in range(0, len(arr)):
    res += 2**(len(arr)-i) if arr[i] == 1 else 0 
  return res/2
