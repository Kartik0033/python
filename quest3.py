#print all the characters of the strings but stop printing if r appeared in the sequence if 
# all characters are successfully printed then print a message all characters are proccessed

sen = input()

for char in sen:
  if(char == 'r' ):
    break
  print(char)
else:
  print("All strings are processed.")



