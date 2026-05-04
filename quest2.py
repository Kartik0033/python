# program to count no of times a appear in a input string from user using the for loop

sen = input()
count = 0

for char in sen:
  if(char == 'a'):
    count+=1

print("The number of time a appear is",count)

