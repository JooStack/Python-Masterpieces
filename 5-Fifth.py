# Flattening a list within a list (Another)

liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
def neon(x):
  h = []
  def neo(x):
    for i in x:
      if type(i) != type(x):
        h.append(i)
      else:
        neo(i)
    return h
  neo(x)
  return h
 
print(neon(liste))