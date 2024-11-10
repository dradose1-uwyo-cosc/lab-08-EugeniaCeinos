# Eugenia Ceinos
# UWYO COSC 1010
# Submission Date: 11/10/2024
# Lab 08
# Lab Section: 16
# Sources, people worked with, help given to: none


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
# "5.67" => 5.67
# "-4.4" => 4.4
# "-5.67." => False
# "teje" => False

def adv_convert(num):
    negative = False
    if num[0] == "-":
        negative = True
        num = num.replace("-", "")

    if "." in num:
        numsplit = num.split(".") # [somenumber, somenumber]
        if len(numsplit) == 2 and numsplit[0].isdigit() and numsplit[1].isdigit():
            if negative:
                return -1*float(num)
            else:
                return float(num)
        else:
            return False
    
    elif num.isdigit():
        if negative:
            return -1*int(num)
        else:
            return int(num)
    
    return False # In functions you return only once, so it executes if the first two aren't executed, no need for else:

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

def slope_intercept(m, b, lower_bound_x, upper_bound_x):
    y = []
    if type(lower_bound_x) is int and type(upper_bound_x) is int and type(m) is int and type(b) is int:
        if lower_bound_x <= upper_bound_x:
            for x in range(lower_bound_x, upper_bound_x + 1):
                y.append((m*x)+b)
        else:
            return 2 # Lower bound must be minor than upper bound
    else:
        return 1 # Only integer values
    return y

print("You can always end the program by typing 'exit'")
while True:
    m = input("Determine the slope: ")
    if m.lower() == "exit":
        break
    b = input("Determine the intercept: ")
    if b.lower() == "exit":
        break
    lower_bound = input("Determine the lower bound: ")
    if lower_bound.lower() == "exit":
        break
    upper_bound = input("Determine the upper bound: ")
    if upper_bound.lower() == "exit":
        break

    m = adv_convert(m)
    b = adv_convert(b)
    lower_bound = adv_convert(lower_bound)
    upper_bound = adv_convert(upper_bound)
    y = slope_intercept(m, b, lower_bound, upper_bound)
    if y == 1:
        print("Only integer values")
    elif y == 2:
        print("Lower bound must be minor than upper bound")
    else:
        print("The resulting list or value is:", y)
    
print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

def square_root(a,b,c):
    """Does the square root of a number"""
    if type(a) is int and type(b) is int and type(c) is int:
        num = b**(2) -4 * a * c
    else:
        return 1 #Only integer values
    if num < 0:
        return 2 #Can't do square root of a negative number
    if a == 0:
        return 3 #a can't equal 0 because it's a quadratic function
    num = num ** (1/2)
    return num

def quadratic_formula(a, b, c):
    """Does quadratic formula"""
    squared = square_root(a,b,c)
    if squared == 1 or squared == 2 or squared == 3:
        return squared
    positive_way = (-b + squared) / (2*a)
    negative_way = (-b - squared) / (2*a)
    return positive_way, negative_way


print("You can always put 'exit' to finish")
while True:
    a = input("Determine a: ")
    if a.lower() == "exit":
        break
    b = input("Determine b: ")
    if b.lower() == "exit":
        break
    c = input("Determine c: ")
    if c.lower() == "exit":
        break

    a = adv_convert(a)
    b = adv_convert(b)
    c = adv_convert(c)

    result = quadratic_formula(a, b, c) 
    if result == 1:
        print("Only integer values")
    elif result == 2:
        print("Can't do square root of negative numbers")
    elif result == 3:
        print("'a' can't equal 0 because it's a quadratic function")
    else:
        positive, negative = result
        print("The result is:", positive, "and", negative)