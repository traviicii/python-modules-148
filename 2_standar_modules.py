# from helper import d # Best practice : all imports should always go at the top of any file
# The above example imports a specific function(s) by name.

# as opposed to importing the module as a whole

# import helper # this is importing the module as a whole. Meaning whatever we want to use inside of that module, we need to reference the module, then the function, variable, class we're trying to use 

# helper.d() # referencing the module, and then the funciton I'm trying to use from that module

from helper import d, help # Importing specific functions I want to use


import math
#https://docs.python.org/3/library/math.html

# square root
root = math.sqrt(30)
print(root)

# round root up
up = math.ceil(root)
print(up)

# round root down
down = math.floor(root)
print(down)

d()

# Import a module using an alias
import datetime as dt

now = dt.datetime.now()
print(now)

start_time = dt.datetime.now() # Testing how fast looping through a list is vs a tuple
for _ in list(range(1000000)):
    pass
finish = dt.datetime.now()
print(f"time to complete list for loop: {finish - start_time}")

start_time = dt.datetime.now()
for _ in tuple(range(1000000)):
    pass
finish = dt.datetime.now()
print(f"time to complete tuple for loop: {finish - start_time}")

# create a datetime object for a specific date
my_birthday = dt.date(1991, 10, 9)
print(f"My birthday is: {my_birthday}")

d()

# from module import function
from collections import Counter

colors = ['red', 'blue','black','blue','white','green','blue','orange','blue','yellow','red']


color_count = Counter(colors)
print(color_count)
print(color_count['blue'])