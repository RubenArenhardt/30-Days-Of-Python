# Arithmetic Operations in Python
# Integers
"""
print('Addition: ', 1 + 2)
print('Subtraction: ', 2 - 1)
print('Multiplication: ', 2 * 3)
print ('Division: ', 4 / 2)                         # Division in python gives floating number
print('Division: ', 6 / 2)
print('Division: ', 7 / 2)
print('Division without the remainder: ', 7 // 2)   # gives without the floating number or without the remaining
print('Modulus: ', 3 % 2)                           # Gives the remainder
print ('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2)                     # it means 3 * 3

# Floating numbers
print('Floating Number,PI', 3.14)
print('Floating Number, gravity', 9.81)

# Complex numbers
print('Complex number: ', 1 + 1j)
print('Multiplying complex number: ',(1 + 1j) * (1-1j))

# Declaring the variable at the top first

a = 3 # a is a variable name and 3 is an integer data type
b = 2 # b is a variable name and 3 is an integer data type

# Arithmetic operations and assigning the result to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

# I should have used sum instead of total but sum is a built-in function try to avoid overriding builtin functions
print(total) # if you don't label your print with some string, you never know from where is  the result is coming
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

# Declaring values and organizing them together
num_one = 3
num_two = 4

# Arithmetic operations
total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_two
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)


# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

print(3 > 2)     # True, because 3 is greater than 2
print(3 >= 2)    # True, because 3 is greater than 2
print(3 < 2)     # False,  because 3 is greater than 2
print(2 < 3)     # True, because 2 is less than 3
print(2 <= 3)    # True, because 2 is less than 3
print(3 == 2)    # False, because 3 is not equal to 2
print(3 != 2)    # True, because 3 is not equal to 2
print(len('mango') == len('avocado'))  # False
print(len('mango') != len('avocado'))  # True
print(len('mango') < len('avocado'))   # True
print(len('milk') != len('meat'))      # False
print(len('milk') == len('meat'))      # True
print(len('tomato') == len('potato'))  # True
print(len('python') > len('dragon'))   # False

# Boolean comparison
print('True == True: ', True == True)
print('True == False: ', True == False)
print('False == False:', False == False)
print('True and True: ', True and True)
print('True or False:', True or False)

# Another way comparison 
print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False -there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statement is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False
"""
#Declare your age as integer variable

age = int(20)

#Declare your height as a float variable

height = float(1.86)

#Declare a variable that store a complex number

comp = complex(1 + 2j)

#Write a script that prompts the user to enter base and 
# height of the triangle and calculate an area of this 
# triangle (area = 0.5 x b x h).

print('Calculatin the area of a triangle')
b = float(input('Whats the size of the base?'))
h = float(input('Whats the size of the height?'))
print('The triangle has an area of:',0.5 * b * h)

#Write a script that prompts the user to enter side a, 
# side b, and side c of the triangle. Calculate the 
# perimeter of the triangle (perimeter = a + b + c).

print('Calculating the perimeter of a triangle')
side_a = floar(input('Whats the size of the first side?'))
side_b = floar(input('Whats the size of the second side?'))
side_c = floar(input('Whats the size of the third side?'))
print('The perimeter is:',side_a+side_b+side_c)

#Get length and width of a rectangle using prompt. 
# Calculate its area (area = length x width) and 
# perimeter (perimeter = 2 x (length + width))

print('Calculatin the area and the perimeter of a rectangle')
l = float(input('Whats the size of the length?'))
w = float(input('Whats the size of the width?'))
print('The rectagle has an area of:',l * w)
print('The rectangle has a perimeter of:',2*(l+w))

#Get radius of a circle using prompt. Calculate the 
# area (area = pi x r x r) and circumference 
# (c = 2 x pi x r) where pi = 3.14.

pi = 13.14
print('Calculating the area and the circunference of a circle')
r = float(input('Whats the radius of the circle?'))
print('The area of the circle is:',pi*r**2)
print('The perieter of the circle is:',2*pi*r)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2



#Slope is (m = y2-y1/x2-x1). Find the slope and 
# Euclidean distance between point (2, 2) and point (6,10)



#Compare the slopes in tasks 8 and 9.



#Calculate the value of y (y = x^2 + 6x + 9). 
# Try to use different x values and figure out at 
# what x value y is going to be 0.



#Find the length of 'python' and 'dragon' and make a 
# falsy comparison statement.



#Use and operator to check if 'on' is found in both 
# 'python' and 'dragon'



#I hope this course is not full of jargon. Use in 
# operator to check if jargon is in the sentence.



#There is no 'on' in both dragon and python



#Find the length of the text python and convert the 
# value to float and convert it to string



#Even numbers are divisible by 2 and the remainder is 
# zero. How do you check if a number is even or not using python?

print('Even or odd')
num_check = int(input('What is the number?'))
if num_check % 2 == 0:
     print('even')
else:
     print('odd')

#Check if the floor division of 7 by 3 is equal to 
# the int converted value of 2.7.

7//3 == int(2.7)

#Check if type of '10' is equal to type of 10

type('10')
type(10)

#Check if int('9.8') is equal to 10

int(9.8) == 10

#Write a script that prompts the user to enter hours 
# and rate per hour. Calculate pay of the person?



#Write a script that prompts the user to enter number 
# of years. Calculate the number of seconds a person can 
# live. Assume a person can live hundred years



#Write a Python script that displays the following table

list_exp = [1, 0, 1, 2, 3]
list_num = [1,2,3,4,5]

for x in list_num:
    list_ans=[]
    for y in list_exp:
         list_ans.append(x**y)
    print(list_ans)
    
