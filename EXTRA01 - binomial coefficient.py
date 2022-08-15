import math
# calculate factorial
def factorial (x):
    return math.factorial(x)

# calculate binomial coefficient
def binomial_coefficient (x,y): 
    return factorial(x)/(factorial(y)*factorial(x-y))   