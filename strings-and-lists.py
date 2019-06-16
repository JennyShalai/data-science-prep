# Strings and Lists checkpoint


# Challenge 1:
# Write a script that computes the factorial of a user-inputted
# positive number and prints the result.
# Remember, the goal is to solve the challenge using a for loop.

number = int(input('Please enter a number: '))
result = 1
for i in range(1, number+1):
    result *= i
print(result)


# Challenge 2:
# Write a script that determines whether or not a user-inputted
# number is a prime number and prints "The number that you inputted
# is a prime number" or "The number that you inputted is not
# a prime number" depending on what your script finds.
# Remember, the goal is to solve the challenge using a for loop

number = int(input('Please enter a number: '))
answer = True
for i in range(2, number - 1):
    if number % i == 0:
        answer = False
        break
if answer:
    print('The number you inputted is a prime number.')
else:
    print('The number you inputted is not a prime number.')


# Challenge 3:
# Write a script that prints the number of times a user-inputted letter
# occurs in a user-inputted string. Make sure to build this in such a way
# that it ignores the case of the inputted string and letter.
# For example, if the user inputs the string "Hello, Lovely World!" and
# the letter "l", your program should print '5'.

s = input('Please enter a string: ')
l = input('Please enter a letter to count: ')
s = s.lower()
counter = 0
for char in s:
    if char == l:
    counter += 1
print(counter)


# Challenge 4:
# Write a script that checks if a user-inputted string ends in
# an exclamation point. If it does, then print the string in all
# capital letters. If it doesn't, print the string in all lowercase letters.

s = input('Please enter a string: ')
if s.endswith('!'):
    s = s.upper()
else:
    s = s.lower()
print(s)


# Challenge 5:
# Write a script that removes all of the vowels in a user-inputted string
# and prints the result. (remove the letters a, e, i, o and u.)
# For example, "Hello, World!", your program should print "Hll, Wrld!"

s = input('Please enter a string: ')
vowels_list = ['a', 'e', 'i', 'o', 'u']
output = ''
for char in s:
    if char not in vowels_list:
        output += char
# Print your result here
print(output)


# Challenge 6:
# Write a script that makes every other character of a user-inputted string
# capitalized. For example, "Hello World!", should be "hElLo wOrLd!"

s = input('Please enter a string: ')
s = s.lower()
result = ''
for index in range(len(s)):
    if index % 2 != 0:
        result += s[index].upper()
    else:
        result += s[index]
print(result)


# Challenge 7
# Write a script that creates a list of the even numbers from 0 up to
# but not including a user-inputted positive number and then prints the result.
# For example, inputs '7', your program should print '[0, 2, 4, 6]'.
n = int(input('Please enter a number: '))
for i in range(0,n,2):
    l.append(i)
print(l)


# Challenge 8
# Write a script that prints a list of the numbers between 0 and a user-inputted
# number (exclusive) that are evenly divisible by a second user-inputted number.
# For example, inputs '9' and '3', your program should print '[0, 3, 6]'

n1 = int(input('Please enter a number: '))
n2 = int(input('Please enter a number to divide by: '))
for i in range(0,n1,n2):
    l.append(i)
print(l)

# Challenge 9
# Given the two lists [0, 3, 6, 9, 10, 2, 5] and [2, 6, 4, 7, 8, 1, 15],
# write a script that finds the common elements between them.
# Store the results in a list, then print that list, sorted, as the final output.

l1 = [0, 3, 6, 9, 10, 2, 5]
l2 = [2, 6, 4, 7, 8, 1, 15]
common = []
for element in l1:
    if element in l2:
        common.append(element)
common.sort()
print(common)


# Challenge 10
# Revise your script from Challenge 9 to accept user input.
# Build it so that the user has to enter seven numbers (each separated
# by an enter at the command line) for each list.
l1 = []
l2 = []

#print('Please enter a number each separated by an enter:')
for i in range(7):
    user_input = input()
    l1.append(int(user_input))
#print('Please enter a number each separated by an enter:')
for i in range(7):
    user_input = input()
    l2.append(int(user_input))
for element in l1:
    if element in l2:
        common.append(element)
common.sort()
print(common)
