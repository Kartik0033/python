#finding the largest elemin the list 
# checking through each elem in  list for using

arr = [ 9,6,40,9]
temp =0
for var in arr:
  if (var > temp):
    temp = var

print("Largest ",temp)
print(max(arr))
# same time complexity