# Flattening a list within a list


x = [312,["Hey"],[3,"WwW",3,[],[[3],44,["2",[]]],2,[]]]

b = []
def flatt(a) :
  
  for i in a :
    if type(i) != list :
      b.append(i)
    else :
      flatt(i)
  return b
print(flatt(x))