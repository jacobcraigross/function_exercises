'''
Given several lists of random integers, write a function that checks to
see of the sequence of "1, 2, 3" ever occurs. A simple boolean statement
will suffice.
'''

# define the func. and nums will be the list of integers to pass in
def array_checker (nums):
    # iterate the list and take 2 from the end, since were counting in 3s
    for i in range(len(nums)-2):
        # the counter mechanism
        if nums[i] == 1 and nums[i + 1] == 2 and nums [i + 2] == 3:
            return True
    # if that sequence does not appear, return False.
    return False

'''
Given a string of characters, return a new string made up of every other
character in that string. Ex: Hello = Hlo, Jacob = Jcb, etc.
'''

my_string = 'Jacob Ross and python. A match made in hellfire.'

def string_bits (my_string):

    result = ''

    for letter in range (len(my_string)):
        if letter % 2 == 0:
            result = result + my_string[letter]

    print result

string_bits(my_string)

'''
Given a string, return a new string with every character printed twice.
ex: Jake = JJaakkee, etc.
'''
my_string = 'Hello world. Oh shit I noticed its burning to the ground.'

def double_char(my_string):
    result = ''
    for char in my_string:
        result += char * 2
    print result

double_char(my_string)

'''
Given an array of integers, count the number of even integers and print the tally.
'''

nums = [1, 22, 33, 57, 3, 2, 9, 88, 27, 99, 73, 77266278, 9928827, 100276]

def count_even (nums):

    count = 0

    for elem in nums:
        if elem % 2 == 0:
            count += 1

    print count

count_even(nums)
