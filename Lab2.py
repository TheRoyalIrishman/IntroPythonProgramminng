
# CS2021 Lab 02 - Required Questions
## Modify this file by adding your salutation and code. 
## Once you pass all the doctests, then 
## you can then submit you program for credit. 

_author_ = "Cameron Clarke"
_credits_ = ["Cameron Clarke"]
_email_ = "clarkeck@mail.uc.edu" # Your email address

#  RQ1
"""
Write a function day_name that converts an integer number 0 to 6 into the name of a day. Assume day 0 is 'Sunday'. 
Your function should return error message if the arguments to the function are not valid. 
"""
def day_name(n):
    """
    >>> day_name(3) 
    'Wednesday'
    >>> day_name(6) 
    'Saturday'
    >>> day_name(42)
    'Invalid argument'
    """
    "*** YOUR CODE HERE ***"
    
    dayOutput = ""
    
    if n == 0:
        dayOutput = "Sunday"
    elif n == 1:
        dayOutput = "Monday"
    elif n == 2:
        dayOutput = "Tuesday"
    elif n == 3:
        dayOutput = "Wednesday"
    elif n == 4:
        dayOutput = "Thursday"
    elif n == 5:
        dayOutput = "Friday"
    elif n == 6:
        dayOutput = "Saturday"
    else:
        dayOutput = "Invalid argument"
        
    return dayOutput    

#  RQ2
def two_of_three(a, b, c):
    """Return value using only a one-line return statement.  The value should be the sum of two squares x*x + y*y, 
         where x and y are the two largest members of the set of. positive numbers a, b, and c.
    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    
    # https://www.geeksforgeeks.org/python-program-to-find-second-largest-number-in-a-list/
    # source for how I got the first and second largest numbers in a list
    
    inputList = [a, b, c]
    
    largestNumber = sorted(inputList)[-1]
    secondLargestNumber = sorted(inputList)[-2]
    
    return largestNumber**2 + secondLargestNumber**2


#  RQ3
def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    """
    "*** YOUR CODE HERE ***"
    
    # https://www.programiz.com/python-programming/examples/factor-number
    # used above article to remind myself on how to get factors of number
    
    factorsList = list()
    
    # range function runs from 1 to n - 1
    
    for counter in range(1, n):
        if n % counter == 0:
            factorsList.append(counter)
            
    return max(factorsList)

# RQ 4
def keeper(pred, n):
    """Print the numbers between 1 and n which satisfy the predicate pred.

    >>> keeper(lambda x: x%2 == 0, 15)
    2 4 6 8 10 12 14 
    >>> keeper(lambda x: x%7 == 0, 40)
    7 14 21 28 35 
    """
    "*** YOUR CODE HERE ***"
    
    # https://chat.openai.com/share/db1f9827-200f-4d12-9f0b-fe0e38784f0e
    # Chat-GPT URL I used to solve this problem
    
    for counter in range(1, n + 1):
        if pred(counter):
            print(counter, end= " ")
    
import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)

