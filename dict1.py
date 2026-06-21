students = {
  "name" : "kartik",
  "age" : 21,
}

print(students["name"])
students["cgpa"] = 9.4

for key,values  in students.items():
  print(f"key {key} values {values}")

l1 = [10,20,10,20,30]
dc ={}
count = 0
temp  = 0

for i in l1:
  temp = i
  for j in l1:
    if temp == j:
     count +=1

  dc[temp]=count
  count = 0

print(dc)

chars = ['d','c','d','c','a']
freq = {}

for  cha in chars:

  if cha in freq:
    freq[cha] += 1
  else:
    freq[cha] = 1

print(freq)
