# i = 3

# while i>=1:
#   num = int(input("Enter the even number"))
#   if (num % 2 == 0):
#     print("Your are the winner")
#     break
#   elif i==1 :
#     print("Your are a looser")
#   else:
#     print("More",(i-1),"chance left")
    
#   i-=1
n = int(input())

for i in range(n,0,-1):
  print(i*2)

n = int(input())
for i in range((n*2),0,-2):
  print(i)

#PRint the n number of the even natural numbers