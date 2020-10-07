python3 -m virtualenv -p python3 <virtual_environment_name> # create new virtualenv
python3 -m virtualenv <virtual_environment_name> # works also
source <virtual_environment_name>/bin/activate # to activate this venv
variables are dynamic # string variable value can be replaced with any other type
type(<variable>) # returns a variable type
del <variable>  # a way do delete a variable

## numbers ##

# numbers without decimal spaces, only whole numbers
# mathematical operations can be done on them
sum([list_of_numbers]) # returns a summary
number = 5
number =+ 4 # adds the for to that number and saves that as numbers
    # number now has value 9
num**2 # "na kvadrat"

## floats ##

# numbers with decimal spaces e.g. 123.45
# mathematical operations can be done on them

## strings ##


print("<string>") # print out the string value
len('<string>') # checks the length of a sting (spaces included)
all strings are indexed, whitespaces count as strings [] # each letter 0 1 2 3 ...
    mystring = "neki text"
    mystring[0] # result is n (as the first character)
    mystring[-1] # grabs the last letter
string slicing [start:stop:step]
    # start # where to start
    # stop # where to stop (without that character)
    # step # size of the jump you take
    mystring[1:] # from e to the end (eki text)
    mystring[:7] # everything to the 7th character (neki t)
    mystring[0:5] # (neki)
    mystring[::] # whole string
    mystring[::2] # every second character
    mystring[::-1] # string in reverse order
ecape characters can be used within strings
  \n for new line
  \t for tab
string concatination
    "string1" + "string2" # result string1string2
    # replacing letter within a string has to be done as "letter" + "string"
    Sam ==> Pam
    'P' + Sam[1:]
string methods
    x = "Hello World"
    x.upper() # 'HELLO WORLD' - this doesnt replace the original variable
    x = x.upper() # this does
        # without () it will just return what x.upper does
    x.lower()
    x.split() # splits where whitespaces variable, result is a list
    x.split('i') # splits where each 'i' character is, it delete's the 'i's
    '+'.join([list_of_strings]) # will join them with + in between
        '+'.join(['a','b','c','d','e']) # returns a+b+c+d+e
        # if '' is at the beggining then there would be no space in betwen -> abcde
    +=  # to append to the end of a string and save it in that variable
        text = 'hello'
        text += 'world'
        # result print(text) 'hello world'
    print('this is a string {}'.format('word')) # inserts a word wher {} are
        # result this is a string word
    print(f'this is a string {word}') # if variable "word" is defind up front
        # result this is a string word
    print('this is a string %s' %'word')
        #  result this is a string word
    print('{2} {1} {0}'.format('tri', 'dva', 'jedan')) # inserts variables with that order
        # result jedan dva tri
    print('{one} {two} {three}'.format(three='tri', two='dva', one='jedan'))
        # result jedan  dva tri

float formatting
# {value:width.precision f}
    result = 10/3
    print("The result is {r}".format(r=result))
    print("The result is {r:1.3f}".format(r=result))
        # 1 is a width 3.333 vs       3.33 if it was set to 10
        # 3f is how many decimal places it will take


## lists ##

# list of any type of data, sparated by comma,
# any entry can be replaced - muttable

my_list = [1,2,3,4]
my_list = ['rec',2,33.3] # data types ca be different
# unlike with strings, elements within a list can be easily changed
my_list[0] = 'jedan' # will change the first element from there to that value
my_list.append(5) # adds item to the end of the list
my_list.pop() # removes the last element
my_list.pop(0) # removes the first element
my_list.sort() # sorts A-Z
sorted(my_list) # does the same thing and outputs the value
my_list.reverse() # sorts Z-A


## dictionaries ##

# dictionaries can contain any other data daype, dictionaries included
my_dict = { 'key1':'value1', 'key2':'value2' }
     my_dict['key1'] # returns 'value1'
d = {'k1':123, 'k2':[0,1,2], 'k3':{'insideKey':'someValue'}}
     d['k3']['insideKey'] # returns 'someValue'
# methods can be applied to dictinaries
d = {'k1':['a', 'b', 'c']}
    d['k1'][1].upper() # returns 'B'
# adding elements
d['k2'] = ['d', 'e']
    d = {'k1':['a', 'b', 'c'], 'k2':['d', 'e']}
# same principal us used to override
d.keys() # returns all keys
d.values() # returns all values
d.items() # returns key:value pairs


## tuples ##

# same like lists but they can't be changed - immutable
t = (1,2,3) # tuple
l = [1,2,3] # list
# only two methods available - count and index
    # count - how many times has certain element appeared
    # index - at what position has it appeared for the first time

## sets ##

# unordered collections of unique elements
myset = set()
myset.add(1) # adds 1 to the set myset
mylist = [1,1,1,1,1,1,2,2,2,2,2,3,3,3]
    set(mylist) # result {1, 2, 3}

## booleans ##

True / False # must be capitalized


## Files ##

myfile = open('<file_name>') # path an name to the file must be correct
myfile.read() # reads the file in a single line as a string
# if the same file is read again it will return an empty string ''
# reason for it is that the coursor has moved to the end of the file after reading
myfile.seek(0) # resets the coursor to the beggining
print(myfile.read()) # returns each line individually
myfile.readlines() # reads file but separates lines with \n
myfile.close() # this releases the file so it could be deleted etc...
with open('myfile.txt') as myfile:
    contents = myfile.txt.read() # this uses the file but doesn't lock it
with open('myfile.txt', mode='r') as myfile:
    contents = myfile.txt.read() # this uses the file but doesn't lock it
    # mode='r' # read only, same as without a mode
    # mode='w' # write only, this will overrite the file_name if it exists
    # mode='a' # append, add to the end of a file
    # mode='r+' # read and write
    # mode='w+' # write and read (overrites file if it exists)
with open('myfile.txt', mode='a') as myfile:
    myfile.write('\nthis is the fourth line') # adds this to the end of a file
# file can't be edited and read at the same time


## comparison operators ##
== # equal
!= # not equal
>
<
<=
>=

## logical oparators ##

and
or
not
# () can be used
(1 == 2) or (2 == 2) # same as without ()
not(1 == 1) # to get an oposite response

## statements ##

if
elif
else
if 3>2:
    print('Its true!')
elif <something>:
    print('<whatever>')
else:
    print('not true')

## for loops ##

# used to iterate through every elment of a list/string/dict...
my_iterable = [1,2,3]
for i in my_iterable:
    print(i) # prints out each item
    print('hello') # prints out hello as many times as there are items
# example with if :
mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number: {num}') # this or the one below
        print('Odd Number: {}'.format(num)) # either of these print will work
# sometimes name for the variable isn't used, only _ i set
for _ in "hello world":
    print('Cool!')
# tuple unpacking
mylist = [(1,2),(3,4),(5,6),(7,8)]
for (a,b) in mylist: # (a,b) is a variable name which has two elements
    print(a)
    print(b)
# working with dictionaries
d = {'k1':1, 'k2':2, 'k3':3}
for i in d:
    print(i) # this prints out only keys (k1, k2, k3)
for i in d.items():
    print(i) # this prints out key:value pairs like tuples (key, value)
for (key,value) in d.items():
    print(value) # this returns only values

## while loops ##

# while this is true do this
x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x = x + 1
    x += 1 # either this or the line above, they do the same thing
    # result
    The current value of x is 0
    The current value of x is 1
    The current value of x is 2
    The current value of x is 3
    The current value of x is 4
break # breaks out of the current closest enclosing loop
    mystring = "Sammy"
    for l in mystring:
        if l == 'a':
            break
        print(l) # prints out only 'S' as it stopps when it gets to 'a'
        # this breaks out only out of that for loop, if there is some other loop after that it will continue

continue # goes to the top of the closest enclosing loop
    mystring = "Sammy"
    for l in mystring:
        if l == 'a':
            continue
        print(l) # prints out S m m y - wihout 'a' as it is skipped
pass # does nothing at all
    x = [1,2,3]
    for item in x:
        pass # there is no condition, but if this wasn't here loop woud error out

## operators ##

  # range #
for n in range(10):
    print(n)
    # prints out numbers 0-9 (10 numbers)
for n in range(3,10):
    print(n)
    # prints out numbers 3-9 (up to number 10)
for n in range(0,10,2):
    print(n)
    # prints out numbers 0-2-4-6-8 (every second unmber, up to number 10)
list(range(<parameters>)) # to get requested range as a list

  # enumerate #
word = 'abcde'
for i in enumerate(word):
    print(i)
    # result prints out tuples (0, 'a'), (1, 'b')...

  # zip #

mylist1 = [1,2,3]
mylist2 = ['a', 'b', 'c']
for i in zip(mylist1, mylist2):
    print(i)
    # result is a tuple (1, 'a'),(2, 'b'), (3, 'c')
    # it zips only pairs, if there was a an eg 4, ti wouldn't be zipped
list(zip(mylist1,mylist2))

  # in #

'x' in [1,2,3]
    # returns True or False
    # works the same way with string or tuples
d = {"mykey":123}
'mykey' in d # to work with keys
345 in d.values() # to work with values

  # min / max #

min(<list_name>) # returns minimum value
max(<list_name) # returns maximum value

  # random #

from random import shuffle # random is a library from which you import functions
shuffle(<list_name>) # shuffles the list
randint(1,100) # selects random number from the given range
input('enter a number: ') # shows a user prompt for number entering
    variable = input('enter a number: ') # saves entered value in a variable
    # all entres are saved as  string!!!
    int(variable) # to convert to intiger (or float)

  # list comperhensions #

append # used to add elemnts to a list
    mystirng = 'hello'
    mylist = []
    for l in mystring:
        mylist.append(l)
    # result is a list ['h', 'e', 'l', 'l', 'o']
    mylist = [l for l in mystring] # does the same thing
    mylist = [l.upper() for l in mystring] # operations can be done here, like here to turn it to CAPS


### METHODS AND FUNCTIONS ###

help(something.method()) # get help about a method

  ## functions ##

def name_of_the_function(paramater):
    '''
    DOCSTRING: ...
    INPUT: ...
    OUTPUT: ...
    '''
    what_function_does

def add_function(num1,num2):
    return num1 + num2
result = add_function(1,2)
print(result)
    # returns 3
def say_hello(name='NAME'): # if no parameter is supplied put in NAME
    print('hello'+name)
def dog_check(mystring):
    return 'dog' in mystring.lower() # use this when checking strings to avaiod problems with Caps

  -' arguments and key word arguments'-

def myfunc(*args): # enables function to accept an unlimited number of parameters
    return sum(args) # does sum an all provided parameters
    # all supplied parameters are going to be treated as a tuple
    # word doesn't have to be 'args' it just has to start with * but args is a conventional choice

def myfunc(**kwargs): # key-word arguments
    if 'fruit' in kwargs:
        print('My fruit of chice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')
myfunc(fruit='kiwi')
    # returns My fruit of choice is kiwi
myfunc(fruit='kiwi',fruit='apple')
    # if two fruit arguments are supplied it wil error as it expects done
    # all supplied arguments are treated as dictionary
    # {'fruit': 'kiwi', 'fruit': 'apple'}
myfunc(fruit='kiwi',veggie='carrot')
    # if second argument is supplied which is anything other than fruit than it will work

def myfunc(*args,**kwargs):
    print('I would like {} {}'.format(args[0],kwargs['food']))
    # accept first argument and put in a key-word which maches 'food'

 # function examples #

def spy_game(nums):
    code = [0, 0, 7, 'x'] # x could have been anything
    for n in nums:
        if n == code[0]:
            code.pop(0) # remove first item from code
    return len(code) == 1 # do a return when length of a code is 1
spy_game([1,2,4,0,0,7,9])
---
def paper_doll(text):
    result = '' # create an empty string
    for t in text:
        result += t*3 # append t*3 (or t+t+t) to the end of the string "result"
    return result
paper_doll('hello')
---
def has_33(nums):
    for n in range(0,len(nums)-1): # len-1 is done as last element shouldn't have next one
        if nums[n] == 3 and nums[n+1] == 3: # if this and next number are equal to 3
            return True
    return False
has_33([1, 3, 3])
---
def master_yoda(text):
    mylist = text.split() # split text into a list of words
    myreverse = mylist.reverse() # reverse the list
    return ' '.join(myreverse) # joint the list back into a string
master_yoda('I am home')
---
def old_macdonald(name):
    first_half = name[:3] # split and take 0,1 and 2nd character
    second_half = name[3:] # split and take all character from 3rd till the end
    return first_half.capitalize() + second_half.capitalize()
old_macdonald('macdonalnd')
---
def animal_crackers(text):
    return text.split()[0][0].lower() == text.split()[1][0].lower() # compare first letters of each word
animal_crackers('jedna dva')
---
def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        return min(a,b) # return the smallest one (in this case just smaller one)
    else:
        return max(a,b) # return the biggest
lesser_of_two_evens(1,2)
---
def myfunc(text):
    out = [] # create an empty string
    for i in range(len(text)): # calculate length of an entered text and from that value create a range
        if i %2==0: # if it is an odd number
            out.append(text[i].lower()) # append that to the list "out" as lower
        else:
            out.append(text[i].upper()) # append to list "out" as upperCase
    return ''.join(out) # join that list of strings into a word
---
def summer_69(arr):
    total = 0
    add = True

    for num in arr:
        while add: # while add is True
            if num != 6: # if num is not 6
                total += num # add num to total
                break # exit this while loop
            else
                add = False # set add to False
        while not add: # while add is False
            if num != 9:
                break
            else:
                add = True
                break
        return total
summer_69([1,3,5])
---

  ## lambda expressions, map and filter ##

# lambda, temp function which doesn't need to be named as it is going to be used only once

 # maps #

#  applys functions which accept a single element to a lists
def square(num):
    return num**2
my_nums = [1,2,3,4]
#square(my_nums) # this won't work
for item in map(square, my_nums): # apply function square to each element from my_nums
    print(item)
list(map(square,my_nums)) # returns a results as a list
# when passing function within a map, only name of the function is passed without ()

 # filter #

# filters out a list based on the function
def check_even(num):
    return num%2 == 0
mynums = [1,2,3,4,5,6]
list(filter(check_even,mynums))
    # returns 2, 4 and 6
list(map(check_even,mynums)) # would return True or False for each member of a list


 # lambda #

# regular function
def square(num):
    result = num ** 2
    return result
# simplifed
def square(num): return num ** 2
# as labda
lambda num: num ** 2
# can be assigned to a variable
square = lambda num: num ** 2
square(2)
list(map(lambda num:num**2,my_nums)) # same as above done with lambda
list(filter(lambda num:num%2 ==0, mynums))

    ## nested statements and scope ##

L # local       - names assigned within a function
E # enclosing   - names within enclosing functions (function within a function)
G # global      - names assgned at the top level of a module file
B # built-in    - preassgned names like len, map...

name = 'THIS IS A GLOBAL STRING' # global variable

def greet():
    name = 'Sammy' # enclosing variable
    def hello():
        name = 'Jo' # local variable
        print('Hello '+name)
    hello()
greet()

    ## Object oriented programming ##

clss ClassNamesInCammelCase():

# Attributes are attributes for any object of that class
    # If class is a Dog, his attributes are breed, color, species...
# Methods are functions defined within a body of a class and they are used to perform operations
# that some times utilize the attribtes of the object

# creating a class
class Dog():

    # Class object attribute
    # these are the same for any instance of the class
    # these don't use the self keyword
    species = 'mammal'

    # User defined attributes
    def __init__(self, breed, name, spots, legs=4):

        # breed is the attribute of the class and it has to be defined this way
        self.breed = breed
        self.name = name

        # expect a boolean, not a string
        self.spots = spots

        # default value can be set for attributes
        self.legs = legs

        # some attributes don't have to be defined up front and then they don't need to be supplied when defining a class
        self.tail = False

    # Method / operations / actions
    def bark(self, number):
        # print the name from the name attribute
        # external attributes can be set such as number here, they are defined when a method is called
        print('Woof! my name is {} and the number is {}'.format(self.name, number))

# setting a class to a variable and giving it a value to the attribute
my_dog = Dog(breed='lab', name="Vik", spots=False)
my_second_dog = Dog('Franky','Husky', True)

    ## inhariting from a different class ##

class Animal():
    def __init__(self, *args, **kwargs):
        print('Animal created')

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print('I am eating')


class Dog(Animal):
    def __init__(self, *args, **kwargs):
        Animal.__init__(self)
        print('dog created')

    def who_am_i(self): # method can be overwritten if same name is given to it
        print('I am a dog')

    def bark(self): # new methods can also be added
        print('woof')

mydog = Dog()
    # returns
        #Animal created # inherits this from the previous class
        #dog created

mydog.eat() # all methods from Animal class will be available in the Dog class

    ## polymorphism ##

# using the same method in multiple classes without inheritance

class Dog():
    def __init__(self, name, *args, **kwargs):
        self.name = name

    def speak(self):
        return self.name + " says woof!"

class Cat():
    def __init__(self, name, *args, **kwargs):
        self.name = name

    def speak(self):
        return self.name + " says meow!"

# both classes are using the same speak method
niko = Dog('niko')
felix = Cat('felix')
print(niko.speak())
print(felix.speak())

# one way to apply this is to use the for loop
for pet in [niko,felix]:
    print(type(pet))
    print(type(pet.speak))

# or to define a new method which will use this common method
def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)

# creating a class which should only be used as inherited class
class Animal():

    def __init__(self, name, *args, **kwargs):
        self.name = name

    def speak(self):
        # returning an error if this method is called directly for this class
        raise NotImplementedError("Subclass must implement this abstract method")

#myanimal = Animal('fred')
#myanimal.speak()

class Dog1(Animal):

    def speak(self):
        return self.name+ " says woof"

djuro = Dog1('djuro')
djuro.speak()

    ## Special Methods ##

class Book():

    def __init__(self, title, author, pages, *args, **kwargs):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print('a book object has been deleted')


b = Book('naslov', 'steva', 99)
print(b) # doesn't return anything
# print looks for string representation of the function that is why method __str__ is added
str(b) # returns the same thing
len(b) # to get this also __len__ had to be introduced
del b  # a way do delete a set variable
