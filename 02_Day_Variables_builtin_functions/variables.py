
# Day 2: 30 Days of python programing

import math

#Declaring variables
first_name = 'Ruben'
last_name = 'Arenhardt'
country = 'Brasil'
city = 'Venancio Aires'
age = 20
is_married = False
is_true = True
is_light_on = True
#Declaring variables in one line
first_name, last_name, country, city, age, is_married, is_true,is_light_on = 'Ruben', 'Arenhardt', 'Brasil', 'Venancio Aires', 20, False, True, True

#Printing the values, types and lengths
print('First name:', first_name)
print('First name type:', type(first_name))
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name type:', type(last_name))
print('Last name length: ', len(last_name))

#A little play
print('Comparisson: First name:',len(first_name),'; Last name:',len(last_name))
if len(first_name)>len(last_name):
    print('First name is',len(first_name)-len(last_name),'letters longer')
elif len(first_name)<len(last_name):
    print('Last name is',len(last_name)-len(first_name),'letters longer')
elif len(first_name)==len(last_name):
    print("Your First and last names have the same size")

print('Country: ', country)
print('Country type:', type(country))
print('City: ', city)
print('City type:',type(city))
print('Age: ', age)
print('Age type:', type(age))
print('Is married: ', is_married)
print('Is maried type', type(is_married))
print('Is True?', is_true)
print('Is true type:', type(is_true))
print('Is the light on?', is_light_on)
print('Light on type', type(is_light_on))

#Level 2: 4
num_one,num_two = 5,4
total = num_one + num_two
diff = num_two - num_one
product = num_two*num_one
division = num_one/num_two
remainder = num_two%num_one
exp = num_one**num_two
floor_division = num_one // num_two

#Level 2: 5
radius = 30
area_of_circle = math.pi * radius**2
circum_of_circle = 2*math.pi*radius
area_inp = int(input('Radius of a circle:'))
print( math.pi*area_inp**2)

print()

first_name = input('Whats your first name?')
last_name = input('Whats your last name?')
country = input('Whats your country?')
age = input('How old are you?')
print(first_name, last_name, country, age)