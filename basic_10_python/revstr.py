#reverse a string 

# 1st using the slicing operator

str1 = "Hello"

print(str1[0:5])  #default step how many poition to move each time 1 stop to 4
print(str1[4:1:-1]) # moves from 4 to 2 because stop before 1
print(str1[:4:])

print(str1[::-1]) # defautl will be [4::-1] middle will be until ending

# 2nd method for palindrome
reverse = ""
for ch in str1:
  reverse = ch + reverse

print("Rev ",reverse)
