def count_sheeps(sheep):
  number_of_sheeps = 0
  for i in sheep:
    number_of_sheeps += 1 if i == True else 0
  return number_of_sheeps
