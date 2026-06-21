l1 = [10,20,30,40,50]

l2 = l1
print(type(l2))
print(l2)
print(l1[0])
print(l1[len(l1)-1])

for i in l1:
  print(i)

print("count of 10" , l1.count(10))
## split always returns the list of elems which we split
l3 = [int(elem) for elem in input().split() ]
print(l3)

print("sum",sum(l3))

largestnum =0 

for i in l3:
  if  i > largestnum:
    largestnum = i
else:
  print("The largest elem",largestnum)

  