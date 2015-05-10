"""
Code Academy Notes
"""


"""
Functions
"""

def square(n):
    """Returns the square of a number."""
    squared = n**2
    print "%d squared is %d." % (n, squared)
    return squared
    
# Call the square function on line 9! Make sure to
# include the number 10 between the parentheses.
square(10)

"""
"""
def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

power(37,4)  # Add your arguments here!
"""
"""

def cube(number):
    return number**3
    
5
def by_three(number):
    if number % 3 ==0:
        return cube(number)
    else:
        return False

"""
import just teh function from a module
"""
from math import sqrt

from math import * #imports all functions

"""
see all that is important from module
"""

import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!

"""
built in
"""
def biggest_number(*args):
    print max(args)
    return max(args)
    
def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)



def distance_from_zero(n):
    if type(n) == int or type(n) == float:
        return abs(n)
    else:
        return "Nope"



"""
Functiosn part II
"""
def hotel_cost(nights):
    return 140*nights
    
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
        
def rental_car_cost(days):
    cost = days * 40
    if days >=7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost


"""Lists & Dictionaries
"""

"""List append"""

suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.append("swimmers")
suitcase.append("glasses")
suitcase.append("trainers")

#remove
backpack.remove()

list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase

"""INDEX RETURN"""

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")   # Use index() to find "duck"

# Your code here!

animals.insert(duck_index,"cobra")

print animals # Observe what prints after the insert operation

"""For loop across a list"""

start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for n in start_list:
    square_list.append(n**2)
square_list.sort()
print square_list


"""
Dictionaries
"""

#new entries
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['Burger'] = 10.25 # Adding new key-value pair
menu['soup'] = 8.00
menu['salad'] = 6.99


print "There are " + str(len(menu)) + " items on the menu."
print menu

##calling
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

##deletion
del zoo_animals['Sloth']


"""
Lists within dictionary
"""

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = ['seashell','strange berry','lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] +=50


"""
For loop
"""
# can look a string!
for letter in "Codecademy":
    print letter
    
# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
    # Only print out the letter i
    if letter == "i":
        print letter

# for loop dictionary!
webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!
for word in webster:
    print webster[word]

#if two dictionaries have same keys can use same loop!
prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
for item in prices:
    print item
    print "price: %s" % prices[item]
    print "stock: %s" % stock[item]


##simple shopping list
    shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:
            total += prices[item]
            stock[item] -= 1
    return total

###grades!
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total/len(numbers)
    
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    weights = [0.1, 0.3, 0.6]
    avg = homework * weights[0] + quizzes * weights[1] + tests * weights[2]
    return avg
    
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
        
print get_letter_grade(get_average(lloyd))


### using range in loop allows us to modify the list itself!
n = [3, 5, 7]

def total(numbers):
    result = 0
    for i in range(len(numbers)):
        result += numbers[i]
    return result

##loop within loop of lists within list

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
    results = []
    for numbers in lists:
        for i in numbers:
            results.append[i]
    
    return results
