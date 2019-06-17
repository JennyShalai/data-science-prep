# Tuple, Dictionary and Set checkpoint


# Challenge 1:
# Write a script that prompts the user to input a series of numbers separated by
# commas. Your script will then take these inputted numbers and store them
# as a list of tuples, two at a time. Finally, your script will print that list
# of tuples to the user. If the user inputs an odd number of numbers, then only
# make a list of the largest number of pairs of two that are possible.

nums = input('''Please enter a series of numbers separated by commas. \n Hit enter when you are done. ''')
result = []
number_list = nums.split(',')
if len(number_list) % 2 != 0:
    number_list.pop()
for i in range(0, len(number_list)-1, 2):
    result.append((int(number_list[i]), int(number_list[i+1])))

print(result)


# Challenge 2:
# Write a script that prompts the user to input numbers separated by dashes
# ( - ). Your script will take those numbers, and print a dictionary where
# the keys are the inputted numbers, and the values are the squares of those numbers.

nums = input('''Please enter a series of numbers separated by '-'. \n Hit enter when you are done. ''')
squares_dictionary = {int(number):int(number)*int(number) for number in nums.split('-')}
print(squares_dictionary)



