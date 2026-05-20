#checking the string is an padlindrome  madam,nitin ,"121" are palindrome

#using the slicing operator 1 method reverse the string and check 

str2 = "madam"
if( str2 == str2[::-1]):
  print("Palindrome")
else:
  print("NOt a Palindrome")

# 2nd checking using the left and right index comparing 

str3 = "nitin"

left = 0
right = len(str3) -1

while left != right :
  if (str3[left] != str3[right]):
    print("Not a palindrom")
    break

  left +=1
  right -=1
else: #when the condition is not satisfied it runs
  print("Is a palindrome")



  

