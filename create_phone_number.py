def create_phone_number(number):
  return "(" + "".join([str(i) for i in number])[0:3] + ") " + "".join([str(i) for i in number])[3:6] + '-' + "".join([str(i) for i in number])[6:len(number)]
