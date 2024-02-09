_author_ = "Cameron Clarke"
_credits_ = ["Cameron Clarke", "Nick Barth"]
_email_ = "clarkeck@mail.uc.edu" # Your email address

import doctest

def egypt(nr, dr):
    """
    >>> egypt(3, 4)
    '1/2 + 1/4'
    >>> egypt(11, 12)
    '1/2 + 1/3 + 1/12'
    >>> egypt(123,124)
    '1/2 + 1/3 + 1/7 + 1/64 + 1/8333 + 1/347186112'
    >>> egypt(103,104)
    '1/2 + 1/3 + 1/7 + 1/71 + 1/9122 + 1/141449381 + 1/100039636784966424'
    """

    outputString = ""
    
    unitFractionList = []
    
    # I received help from Nick Barth with this assignment
    # We were bouncing ideas off of each other, and he eventually came up
    # with the solution
    
    while nr > 1:
        # dr % nr > 0 is equivalent to either plus zero or plus one
        # so it's functionally equivalent to the ceiling function in math
        unitFraction = dr // nr + (dr % nr > 0)
        unitFractionList.append(unitFraction)
        nr = ((nr * unitFraction) - dr)
        dr = dr * unitFraction
        
        # https://stackoverflow.com/questions/39829827/how-to-get-rid-of-extra-sign-in-print-statement-python
        # Couldn't remember how to format a Python string
        # so I used this StackOverflow link to remind myself
        outputString = " + ".join("1/{}".format(n) for n in unitFractionList)
    
    return outputString
    
if __name__ == "__main__":
  doctest.testmod(verbose=True)