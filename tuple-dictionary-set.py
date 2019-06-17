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


# Challenge 3:
# Write a script that prompts the user for a state name. It will then check
# that state name against the dictionary below to give back the capital
# of that state. However, you'll notice that the dictionary doesn't know the
# capitals for all the states. If the user inputs the name of a state that
# isn't in the dictionary, your script should print 'Capital unknown'.
# Your script should work regardless of capitalization used when the state
# is input. Example: If you inputted CALIfORnia it should print Sacramento.

state_dictionary = {'Colorado': 'Denver', 'Alaska': 'Juneau',
    'California': 'Sacramento', 'Georgia': 'Atlanta',
        'Kansas': 'Topeka', 'Nebraska': 'Lincoln',
            'Oregon': 'Salem', 'Texas': 'Austin', 'New York': 'Albany'}
user_input_state = input('Please enter your state:')
key = user_input_state.lower().title()
if key in state_dictionary:
    print(state_dictionary[key])
else:
    print('Capital unknown')


# Challenge 4:
# Write a script that prompts the user to input numbers separated by commas,
# and then does so again. It should then print those numbers that were common
# in both entries (from lowest to highest).

input1 = input('Please enter your numbers separated by commas:')
input2 = input('Please enter your numbers separated by commas:')

set1 = set(n for n in input1.split(', '))
set2 = set(n for n in input2.split(', '))
result_set = set1.intersection(set2)
result_list = list(result_set)
result_list.sort(key=int)
result = ', '.join(result_list)

print(result)



# Challenge 5:
# Write a script that prompts a user to input a list of words separated
# by commas, and then prints out the unique words in the list.
