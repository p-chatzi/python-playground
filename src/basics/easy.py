###### Welcome to python ######
#_______________
### Sources ###
# https://www.youtube.com/watch?v=fWjsdhR3z3c (youtube - idently)
# https://www.youtube.com/watch?v=Gx5qb1uHss4&t=951s (youtube - idently)

#______________
### Strings ###
print("\n ** Strings ** \n")
snake_is_default = 'sick'
print("yooooo")
print(snake_is_default)
print("yooooo " + snake_is_default, "\n")

#_________________
### Math stuff ###
print("\n ** Math stuff (no print) ** \n")
a = 2
b = 7
math_this = a + b - a * b / a
# ^ Does not do a power, a^b = 5 here!
power = a**b
another_power = pow(a, b)

#_____________________
### Input / Output ###
print("\n ** IO ** \n")
print("You can + or ,", "it won't matter " + "for strings")
value = 7
string_val = "9"
print("Casting a string, whaaat", value + int(string_val))
user_input = input("Enter a number: ")
print("You entered ", user_input, "!\n")

#____________ 
### Loops ###
print("\n ** Loops ** \n")
## if / else 
age = 10
is_happy = True
if (is_happy):
    print("Yay!")
else:   
    print("Boo!\n")

## for loop 
#(start at 0, goes until value - 1)
for i in range(value):
    print(i)

## while loop
while True:
    print("This would run forever, without the break")
    break

## do while
while True:
    if not False:
        print("This will run once")
        break

## Switch 
# Only python 3.10+ has switch (match)
# input receives a string, so it needs to be casted
switch_input = int(input("Enter a number: "))
match switch_input:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Something else\n")        

try:
    # Tries to execute code in here
    print("Try this")
    print("haha" + 1) # This will throw an error
except:
    # If an error is thrown, this will catch it
    print("Catch this") 

#______________________
### Data structures ###
# (those not covered in the previous snippets)
print("\n ** Data structures ** \n")
## float
float = 2.5

## Lists
list = [1, 2, 3, 4, 5]
print("List: ", list)

## Linked Lists

## Tuples
# (immutable lists)
tuple = (1, 2, 3, 4, 5)
print("Tuple: ", tuple)

## Sets
# (unique elements)
set = {1, 2, 3, 4, 5}
print("Set: ", set)

## Dictionaries
# (key-value pairs)
dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
print("Dict: ", dict)

#______________________
### Type annotation ###
# Warns if the wrong type is passed ;)
# Wihtout type annotation, python is dynamically typed
print("\n ** Type annotation (no print) ** \n")
john: str = "John"
who: str = 'Who'
twenty: int = 20
FINAL: int = 10 # This is not a const, just a convention
FINAL = 12      # can still change it :/

#________________
### Functions ###
# Optionally, type annotation can be used in parameters
print("\n ** Fonctions (no print) ** \n")

def add(a, b):
    return a + b

def skip():
    pass

# This function does not return anything
# -> is optional, makes the code safer
# bcs if the return type is different, it will show an error
def show_date() -> None: 
    print("Today is 2021-10-10")
    

#_____________
### Class ###
print("\n ** Classes ** \n")
class Car: # First letter is caps
    # initialisation never returns anything
    # Creates an instance from the parameters
    def __init__(self, brand: str, horse_power: int) -> None:
        # Assigns the parameters to the instance
        self.brand = brand
        self.horse_power = horse_power

    def drive(self) -> None:
        print(f'{self.brand} is driving')
        
    def get_info(self, var: int) -> None:
        print(var)
        print(f'{self.brand} has {self.horse_power} hp')
        
    # Dunders (double underscores) are special methods
    def __str__(self) -> str:
        return f'{self.brand}, {self.horse_power} hp'
    
    def __add__(self, other) -> str:
        return f'{self.brand} & {other.brand}'
        
volvo = Car("Volvo", 200)
volvo.drive()
volvo.get_info(10)

bmw = Car("BMW", 300)
print(volvo + bmw)
