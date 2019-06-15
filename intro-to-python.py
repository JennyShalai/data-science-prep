# Intro to Python checkpoint

# Challenge 1:
# Write a script that takes two user inputted numbers and prints 
# "The first number is larger" or "The second number is larger" 
# depending on which is larger. If the numbers are equal, print 
# "The two numbers are equal". (Hint: you'll need to use input() twice.)

number1 = int(input('Please enter a number: '))
number2 = int(input('Please enter a number: '))

if number1 > number2:
    print('The first number is larger.')
elif number1 < number2:
    print('The second number is larger.')
else:
    print('The two numbers are equal.')


# Challenge 2
# Write a script that computes the factorial of a user-inputted
# positive number and prints the result. 

number = int(input('Please enter a number: '))
if number == 0 or number == 1:
  result = 1
else:
  result = number
  while number > 2:
    result = result * (number - 1)
    number -= 1
print(result)


# Challenge 3
# Write a script that computes and prints all of the positive divisors 
# of a user-inputted positive number from lowest to highest.

number = int(input('Please enter a number: '))
division = 1
while division <= number:
    if number % division == 0:
        print(division)
    division += 1


# Challenge 4
# Write a script that computes the greatest common divisor 
# between two user inputted positive numbers and prints the result.

number1 = int(input('Please enter a number: '))
number2 = int(input('Please enter a number: '))
if number1 < number2:
    divisor = number1
else:
    divisor = number2
while divisor > 0:
  if number1 % divisor == 0 and number2 % divisor == 0:
    break
  divisor -= 1
print(divisor)


# Challenge 5
# Write a script that computes the least common multiple 
# between two user inputted positive numbers and prints the result. 

number1 = int(input('Please enter a number: '))
number2 = int(input('Please enter a number: '))
if number1 < number2:
    delta = number1
else:
    delta = number2
multipler = delta
while multipler <= number1 * number2:
  if multipler % number1 == 0 and multipler % number2 == 0:
    break
  multipler += delta
print(multipler)



