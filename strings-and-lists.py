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


