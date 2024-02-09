import doctest
import math

_author_ = "Cameron Clarke"
_credits_ = ["Cameron Clarke"]
_email_ = "clarkeck@mail.uc.edu" # Your email address

# CS2023 - Lab 3 Required Questions 
# All functions should be written using recursion.
# RQ1

def doubletime(i,n):
    
    
    # https://chat.openai.com/share/67b7a889-d098-4fea-a91a-920af6c6de31
    # ChatGPT URL used to help solve this problem
    # I couldn't think of how to approach this problem
    
    """Returns the result of repeatedly doubling the number i a total of n times
    >>> doubletime(3, 1)
    6
    >>> doubletime(2, 0)
    2
    >>> doubletime(2, 9)
    1024
    """
    "*** YOUR CODE HERE ***"
    
    if n == 0:
        return i
    else:
        # doubles i and decrements n
        return doubletime(i * 2, n - 1)

# RQ2
def skip2_add(n):
    """ Takes a number x and returns x + x-3 + x-6 + x-9 + ... + 0.

    >>> skip2_add(5)  # 5 + 2  + 0
    7
    >>> skip2_add(10) # 10 + 7 + 4 + 1 + 0
    22
    """
    "*** YOUR CODE HERE ***"
    
    total = 0
    
    if n <= 0:
        total = 0
    else:
        total = n + skip2_add(n - 3)
    return total
    
# RQ3
def a(n):
    """Return the number in the sequence defined by a(1) = 1;
    a(n) = (3/2)*a(n-1) if a(n-1) is even; a(n) = (3/2)*(a(n-1)+1) if a(n-1) is odd.
    (see, http://oeis.org/A070885)

    >>> a(1)
    1
    >>> a(2) 
    3
    >>> a(3)
    6
    >>> a(10)
    123
    """
    "*** YOUR CODE HERE ***"
    
    total = 0
    
    if n == 1:
        total = 1
    elif a(n - 1) % 2 == 0:
        total += math.floor((3/2) * a(n - 1))
    else:
        total += math.floor((3/2) * (a(n - 1) + 1))
        
    return total

#RQ4
def gridPaths(mx, ny):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.
    >>> gridPaths(2, 2)
    2
    >>> gridPaths(3, 3)
    6
    >>> gridPaths(5, 7)
    210
    >>> gridPaths(117, 1)
    1
    >>> gridPaths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    
    # https://github.com/galenscovell/CS61A/blob/master/Labs/Pre-MT1/Recursion.py
    # credit for code used
    
    # 1x1 matrix would just be one step
    if mx == 1 or ny == 1:
        return 1
    else:
        # needs to be able to go diagonal
        return gridPaths(mx - 1, ny) + gridPaths(mx, ny - 1)

if __name__ == "__main__":
  doctest.testmod(verbose=True)