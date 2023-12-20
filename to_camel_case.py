import re

def to_camel_case(text):
  temp = re.split(r'-|_', text)
  for i in range(1, len(temp)):
    temp[i] = str(list(temp[i])[0].capitalize()+temp[i][1:len(temp[i])])
  return "".join(temp)
