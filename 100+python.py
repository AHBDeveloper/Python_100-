# Q-1
#  Program to add two numbers in python
# So1ution with user dfine vaiables

"""num1 = 12
num2 = 12
 
print("sum is:", num1 + num2)"""

# So1ution with user-input

"""num1 = float(input("enter num1: "))
num2 = float(input("enter num2: "))

sum = num1 + num2

print("Sum is:", sum)"""

# Q-2
# Program to find square root
# Sol-1 Using Exponentiation

# num1 = 23

"""num2 = int(input("ENTER A NUMBER HERE: "))
sqrt = num2**(1/2)
print("THE SQUARE ROOT OF THE GIVEN NUMBER IS: ", sqrt )
"""
# Sol-1 Using Math Module
"""
import math
num = int(input('ENTER A NUMBER: '))
sqrt = math.sqrt(num)
print("SQUARE ROOT OF THE NUMBER IS: ", sqrt)
"""

# Q-3
# Area of triangle
"""
height = float(input('ENTER THE HEIGHT OF TRIANGLE: '))
base = float(input('ENTER THE BASE OF TRIANGLE: '))

area = (0.5) * (base * height)
print("AREA OF TRIANGLE IS: ", area)
"""

# Q-4
# Program to solve quadratic equation
# Quadratic Equation Formula is ax**2 + bx + c = 0 
#a, b and c are  real numbers
# a!=0
"""
import cmath

a = int(input("ENTER NUMBER  (a!=0): " ))
b = int(input("ENTER NUMBER For B: " ))
c = int(input("ENTER NUMBER For C : " ))

# Formula for discriminant
disc = (b**2) - (4*a*c)

root1 = (-b-cmath.sqrt(disc)/2*a)
root2 = (-b+cmath.sqrt(disc)/2*a)

print("ROOTS ARE ",root1, "and", root2)"""

# Q-5
# Program to swap two variables
# Sol-1 using 3rd variable temp
"""
x = 13
y = 12
#  Swapping
temp = x
print("THE VALUE OF TEMPORARY VARIABLE IS: ", temp)
x = y 
print("THE VALUE OF X VARIABLE IS: ", x)
y = temp
print("THE VALUE OF Y VARIABLE IS: ", y)
"""

# Sol-2 without using third variable
"""x = 12
y = 13

x, y = y, x
print("THE VALUE OF X IS ", x)
print("THE VALUE OF X IS ", y)"""

# Q-6
# python program to generate a remdon number
'''import random
num = random.randint(0,100)
print(num)'''

# Q-7
# program to convert kilometers into miles
'''km = float(input("ENTER A KIOMETERS :"))

miles = km * 0.621371

print('KIOMETER TO MILES CONVERTED SUCCESSFULLY :', miles)
print( km, 'KIOMETER IN MILES WILL BE :', miles , "miles")
'''
# Q-8
# Program to check 
# if number is positive, negative or 0
# sol-1 using conditional statement
'''
num = int(input("ENTER A NUMBER: "))

if (num > 0):
    print("Number is positive")
elif(num < 0):
    print("Number is Negative")
else:
    print("IT IS ZERO: ")'''

# Q-9
# Program to check 
# If Number is ODD OR EVEN
"""
num = int(input("ENTER A NUMBER :"))
if (num % 2 == 0):
    print("This is even number: ")
else:
    print("This is ODD Number:")
"""

# Q-10
# Program to check Leap year 
# leap year = 366 days 
# once in 4 year
"""
year = int(input("ENTER A YEAR: "))

if(year % 400 == 0) and (year % 100 == 0):
    print(year, "is a leap year")

elif (year % 4 == 0) and (year % 100 != 0):
    print(year, "is a leap year")
else:
    print(year, "is  not a leap year")
"""   
# Q-11 
# Program to Find 
# The Largest Among Three Numbers
"""
num1 = int(input("Enter number 1: ")) 
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if (num1 > num2) and (num1 > num3):
    print("NUM ONE IS BIG")
elif(num2 > num1) and (num2 > num3):
    print("NUM TWO IS BIG")
else:
    print("NUM Three IS BIG")"""
    
# Q-12    
# program to check prime numbers
"""
num = int(input("ENTER A NUMEBR: "))

if num == 1:
    print("it is not a prime number")
if num > 1: 
   for i in range(2, num):
       if num % i == 0:
          print("NOT A PRIME NUMBER: ")
          break
   else:
          print("it is prime number")"""
# Q-13
# program to print all 
# prime numbers in intervals
"""
lower = int(input("ENTER LOWER LIMIT: "))
upper = int(input("ENTER UPPER LIMIT: "))

for num in range (lower, upper + 1):
    if num > 1:
        for i in range (2, num):
            if num%i == 0:
                break
        else:
               print(num)"""

# Q-14
# Program to find the fictorial
# Using for loop

# num = int(input("ENTER A NUMBER: ")) 
# num < 0
# factorial = 1


# for i in range(1, num):

