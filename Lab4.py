import doctest

##Lab04 Required Questions ##

#########
# Lists #
#########

_author_ = "Cameron Clarke"
_credits_ = ["Cameron Clarke"]
_email_ = "clarkeck@mail.uc.edu" # Your email address

# RQ1
def cascade(lst):
    """Returns the cascade of the given list running forward and back.

    >>> cascade([1, 2, 3, 4])
    [1, 2, 3, 4, 4, 3, 2, 1]
    """
    "*** YOUR CODE HERE ***"

    reversedList = list(reversed(lst))
    
    lst = lst + reversedList
    
    return lst

# RQ2
def maptwice(function, seq):
    """Applies fn twice onto each element in seq and returns the resulting list.

    >>> maptwice(lambda x: x*x, [1, 2, 3])
    [1, 16, 81]
    """
    "*** YOUR CODE HERE ***"
    
    outputList = []
    
    for item in seq:
        outputList.append(function(function(item)))
    
    return outputList

#RQ3
def filterout(pred, seq):
    """Keeps elements in seq only if they do not satisfy pred.

    >>> filterout(lambda x: x % 2 == 0, [1, 2, 3, 4])
    [1, 3]
    """
    "*** YOUR CODE HERE ***"
    
    filteredList = []
    
    for item in seq:
        if not pred(item):
            filteredList.append(item)
            
    return filteredList
    
#RQ4
def comp(n, pred):
    """ Uses a one line list comprehension to return list of the first n integers (0...n-1) which satisfy the predicate pred.
    >>> comp(7, lambda x: x%2 ==0)
    [0, 2, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    
    filteredList = []

    for counter in range(0, n):
        if pred(counter):
            filteredList.append(counter)
        
    return filteredList

#RQ5
def flatten(lst):
    """ Takes a nested list and "flattens" it.
    
    >>> flatten([1, 2, 3]) 
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] 
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> lst = [1, [[2], 3], 4, [5, 6]]
    >>> flatten(lst)
    [1, 2, 3, 4, 5, 6]
    """
    "*** YOUR CODE HERE ***"

    # https://www.sanfoundry.com/python-program-flatten-nested-list-using-recursion/
    # URL I used to solve this problem

    if lst == []:
        # check if list is by default empty
        return lst
    if isinstance(lst[0], list):
        # combines all sub-lists into main list
        return flatten(lst[0]) + flatten(lst[1:])
    
    return lst[:1] + flatten(lst[1:])

if __name__ == "__main__":
  doctest.testmod(verbose=True)