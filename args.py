def fun(*args):
  print(*args) # to unpack the tuple args is store the positional argument as tuple
  for i in args:
    print(i)

a =8 
b= 8 
c =9

fun(a,b,c)

def newfun(**kwargs): # use when dictionary return
  print(kwargs)
  for i in kwargs:
    print(i,kwargs[i])

newfun(firstname ="kartik",middlename="sharad",lastname="gaikwad")

