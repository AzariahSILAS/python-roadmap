import keyword

#comments 
#variables
#operators
#expressions vs statements
#a brief overview of functions



#variables------------------------
# a variable is a named reference to a value stored in memory -------

# reference = value
age = 24
dollar_per_hour = 22.50
name = "azariah"


# rules for naming variables

#must start with a letter (A-Z, a-z) or underscore(_)

# reserved keywords (can't be used for variables names)

# and, as, assert, break, class, continue, def, del,
# elif, else, except, False, finally, for, from, global,
# if, import, in, is, lambda, None, nonlocal, not, or,
# pass, raise, return, True, try, while, with, yield

#print(keyword.kwlist)




#arithmatic operators------------

# + addition
# - subtraction
# * multiplication
# / division(returns a float)
# // floor division(returns an integer)
# % modulus (remainder)
# ** exponent (power)
#---------------------------------------


add = 5 + 5

sub = 5 - 1

mult = 6 * 7

div = 5 / 2

fdiv = 5 // 2

mod = 10 % 3

exp = 2 ** 2



print(fdiv)



#comparison AKA (relational) operators------------


# == (equal to)
# != ( not equal to)
# > (greater then)
# < (less then)
# >= (greater or equal to)
# <= (less then or equal to)

x = 1
y = 2

z = x >= y

print(z)


#logical operators -------------------------------



# and (True if both are true)
# or (True if at least one is true)
# not (True is False, False is True)

x = True
y = False

z = x or not y

print(z)

#assignment operators ------------------------------------

# = (simple assignment)
# += (add and assign)
# -= (subtact and assign)
# *= (multiply and assign)
# /= (devide and assign)
# //= (floor devide and assign)
# %= (modulus and assign)
# **= (exponent and assign)

x *= 


print(x)

#bitwise operators ------------------------------------------

# & (and)
# | (or)
# ^ (xor (exclusive or))
# ~ (not (inverts bits))\
# << (left shfit)
# >> (right shift)


# identity operators ---------------------------------------
#-check if two objects are the same in memory--------------

# is (True if both variables point to the same object in memory)
# is not (true if they point to difrent objects)


#membership operators ----------------------
#-check if a value is in a sequence (list, string, tuple, etc.)

# in (True if value exists in sequence)
# not (True if value does not exist)

# expressions vs statements-------------------------

#expression (produces a value) (what is x)

x = 5 + 7 #(x is 12)

#statements (performs an action) (do this)

print (x) # (prints the value to the console)



#basic function ---------------------------------

def sum(a, b):
    value = a + b
    print(value)


sum(15, 15)