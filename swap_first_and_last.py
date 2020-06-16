def front_back(str):
  if len(str)>1:
    new_str=str[-1]+str[1:-1]+str[0]
    return new_str
  else:
    return str


def fb(str):
  new_str=str[len(str)-1]+str[1:len(str)-1]+str[0]
  return new_str



def fandb(str):
    new_strs=str[len(str)-1]+str[1:len(str)-1]+str[len(str)-len(str)]
    return new_strs


print(front_back('hey'))
print(front_back('a'))
print(front_back(''))

print(fb('hey'))

print(fandb('hey'))
