# #take input in list
# print("Enter the number of elements to enter in list")
# n = int(input())
# l1 = []

# i = 0

# while i<n :
#   l1.append(int(input()))
#   i+=1

# l1.sort()

# for elem in l1:
#   print(elem)


# s1 = input()
# l1 = input().split(',')

l2 = [int(i) for i in input("Enter elements in seperated by comma,").split(',')]

print(type(l2[0]))
print(type(l2))
for i in l2:
  print(i)