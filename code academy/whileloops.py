"""
While loops
"""


choice = raw_input('Enjoying the course? (y/n)')
## use conditions that are not in a list
while choice not in  ['n','y']:  # Fill in the condition (before the colon)
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")


## can use while true and if statement to break
    from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
print random_number
guesses_left = 3
# Start your game!
while guesses_left > 0:
    guess = int(raw_input("Guess a number between 1 and 10"))
    if guess == random_number:
        print 'You win!'
        break
    guesses_left -= 1
else: 
    print 'You lose.'

"""for loop
"""
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    # Your code here!
    print key + " " + d[key]
"""
enumerate allows us to pass a loop for number index and item
"""
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print index + 1, item



"""
zip function - allows us to use the shorter list by merging two
lists to the length of the smaller one
"""

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    # Add your code here!
    if a > b:
        print a
    else:
        print b
    
