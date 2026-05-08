#max of num
def find_max(*args):
  temp =0
  for i in args:
    if i>temp:
      temp=i
  
  return temp

print(find_max(60,30,50))

# reverse str  or another  [::-1] using slicing
s1 = input()

def reverse(s1):
  i = 1
  while i<=len(s1):
    print(s1[-i])
    i += 1

reverse(s1)

#factorial functin
n = int(input("Enter the value of number which you want factorial"))

def fact(n):
  result = 1
  if n < 0:
    return "Enter positive val" 
  elif n == 0:
    return 1
  else :
    for i  in range(1,n+1,1):
      result *= i
  return result   

print(fact(n))


# Write fun to calculate no of uppercase and lowercase in a string
      

def cal():
  s2 = input("Enter string finding uppercase and lowercase")
  i = 0
  up = 0
  low = 0
  for i in s2:
    if i.isupper():
      up +=1
    elif i.islower():
      low +=1
  
  print("Upper ",up,"Lower",low)

cal()