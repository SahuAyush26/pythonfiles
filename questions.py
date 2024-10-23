# To check if a given number is armstrong number or not

''' 
a = int(input("Enter a number : "))
list = []
sum = 0
a = str(a)

for i in range(0, len(a)):
    list.append(a[i])

for i in list:
    sum = sum + int(i)**3

a = int(a)

if a == sum:
    print("the number is an armstrong number")
else:
    print("the number is not an armstrong number")
'''

# To check if given strings are anagrams or not

'''
a = set()
b = set()
str1 = input("Enter first string : ")
str1 = str1.upper()
str2 = input("Enter second string : ")
str2 = str2.upper()

for i in range(0,len(str1)):
    a.add(str1[i])

for i in range(0,len(str2)):
    b.add(str2[i])

if(len(str1) == len(str2)):
    if(a == b):
        print("the given strings are anagrams of each other")
    else:
        print("the given strings are not anagrams of each other")
else:
    print("the given strings are not anagrams of each other")
'''

# find factorial of a number

'''
def factorial(n):
    y = 1
    while n != 1 and n > 0:
      if n != 1 and n > 0:
          x = n-1
          y = y*n*x
          n = n-2
    return y
    

num = int(input("enter a number : "))

print(factorial(num))
'''
 












