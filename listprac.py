l1 = [10,20,30]
print(l1)
l1.append(30)
print(l1)
l1.insert(0,20) # index , value entered
print(l1)

#l2 = list(3) # error can give  list a number and only one argument can pass
l3 = list("string") #converts to char diff index
print(l3)

for val in l3:
  print("The index is ",val)

print(max(l1))
print("",l1[::-1]) #re
