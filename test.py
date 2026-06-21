# # # check if num divisible by 3
# # n = int(input())
# # for i in range(1,(n+1)):
# #   print(f"square of {i} is {i*i}")

# n = int(input("Enter the number for table")) 

# i=1
# while i <=10:
#   print(f" {n}   * {i} : {n*i}")
#   i += 1

# n = int(input("Enter the until table u wanted to be print"))
# for i in range(1,n+1):
#   print("Printing table of",i)
#   for j in range(1,11):
#     print(f"{i} * {j} :{i*j}")

#---"Write a program to generate a string of n numbers and print it n times."--#

number = int(input("Enter the number"))
s= input("enter the string")
store = ""
## --- I dont care about the value ( _ ) says just repeat for no of times
for _ in range(1,number+1):
  store =store + s

print(store)

while number: #means until number = 0
  print(store)
  number -=1

text = "aadddcaadd"

for i in text:
  if i == "c":
    continue
  print(i)




