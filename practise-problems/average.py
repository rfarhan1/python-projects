list = [1, 2, 3]

def add (list): 
  result = 0
  for i in range (0, len(list)-1):
    result += list[i]
  print(result)


add(list)