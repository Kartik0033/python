#find the maximum of three numbers

def find_max(*args):
  temp = -1
  for i in args:
    if temp < i:
      temp =i
  return temp


    
  


print(find_max(8,3,2,6,23))