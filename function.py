# arguments and function

def main() :
  x = 5
  value(x)

def value(y):
  x=y
  print(x)

def add(a,b): #formal arguments
  a = a 
  b = b
  print(a+b)

add(1,2) #actual arguments

# variable lenght arguments
# but every time we change no of arguments formula also change so we use variable lenght arguments
def average(*t):
  result = sum(t)/len(t)
  return result

print("The average is:",average(10,20,20))#passed as tuple

