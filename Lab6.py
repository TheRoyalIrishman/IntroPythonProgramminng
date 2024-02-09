import doctest

_author_ = "Cameron Clarke"
_credits_ = ["Cameron Clarke"]
_email_ = "clarkeck@mail.uc.edu" # Your email address

## Required Questions: Linked Lists ##
## Use the Linked List ADT defined below

# https://github.com/Nsgj/cs61a/blob/master/lab06_extra.py
# how homework was solved

#RQ1
def hasPrefix(s, prefix):
    """Returns whether prefix appears at the beginning of linked list s.

    >>> x = link(3, link(4, link(6, link(6))))
    >>> print_link(x)
    3 4 6 6
    >>> hasPrefix(x, empty)
    True
    >>> hasPrefix(x, link(3))
    True
    >>> hasPrefix(x, link(4))
    False
    >>> hasPrefix(x, link(3, link(4)))
    True
    >>> hasPrefix(x, link(3, link(3)))
    False
    >>> hasPrefix(x, x)
    True
    >>> hasPrefix(link(2), link(2, link(3)))
    False
    """
    "*** YOUR CODE HERE ***"

    if link_length(s) < link_length(prefix):
        return False
    if prefix == empty:
        return True
    if first(s) == first(prefix):
        # recursively checks if number exists before it
        return hasPrefix(rest(s), rest(prefix))
    else:
        return False

#RQ2
def hasSublist(s, sublist):
    """Returns whether sublist appears somewhere within linked list s.

    >>> hasSublist(empty, empty)
    True
    >>> aca = link('A', link('C', link('A')))
    >>> x = link('G', link('A', link('T', link('T', aca))))
    >>> print_link(x)
    G A T T A C A
    >>> hasSublist(x, empty)
    True
    >>> hasSublist(x, link(2, link(3)))
    False
    >>> hasSublist(x, link('G', link('T')))
    False
    >>> hasSublist(x, link('A', link('T', link('T'))))
    True
    >>> hasSublist(link(1, link(2, link(3))), link(2))
    True
    >>> hasSublist(x, link('A', x))
    False
    """
    "*** YOUR CODE HERE ***"

    if sublist == 'empty':
        return True
    if link_length(s) < link_length(sublist):
        return False
    if hasPrefix(s, sublist):
        return True
    else:
        # recursively goes through each item in linked list
        return hasSublist(rest(s), sublist) 

#RQ3
def hasCatGene(dna):
    """Returns whether the linked list dna contains the CATCAT gene as a sublist.

    >>> dna = link('C', link('A', link('T')))
    >>> dna = link('C', link('A', link('T', link('G', dna))))
    >>> print_link(dna)
    C A T G C A T
    >>> hasCatGene(dna)
    False
    >>> end = link('T', link('C', link('A', link('T', link('G')))))
    >>> dna = link('G', link('T', link('A', link('C', link('A', end)))))
    >>> print_link(dna)
    G T A C A T C A T G
    >>> hasCatGene(dna)
    True
    >>> hasCatGene(end)
    False
    """
    "*** YOUR CODE HERE ***"

    # definition for CAT linked list
    gen = link('C', link('A', link('T', link('C', link('A')))))
    # checks if CAT exists in string
    return hasSublist(dna, gen)

#RQ4
# A set of coins makes change for n if the sum of the values of the coins is n. 
# For example, if you have 1-cent, 2-cent and 4-cent coins, the following sets make change for 7:
#
# 7 1-cent coins
# 5 1-cent, 1 2-cent coins
# 3 1-cent, 2 2-cent coins
# 3 1-cent, 1 4-cent coins
# 1 1-cent, 3 2-cent coins
# 1 1-cent, 1 2-cent, 1 4-cent coins
# Thus there are 6 ways to make change for 7. Write a function countCoinChange that takes a positive integer n 
# and a linked list of the coin denominations and returns the number of 
# ways to make change for n using these coins:

def countCoinChange(amount, denominations):
    """Returns the number of ways to make change for amount where denominations is a linked list of coins
       in descending sorted order.
    >>> denominations = link(50, link(25, link(10, link(5, link(1)))))
    >>> print_link(denominations)
    50 25 10 5 1
    >>> countCoinChange(7, denominations)
    2
    >>> countCoinChange(100, denominations)
    292
    >>> denominations = link(16, link(8, link(4, link(2, link(1)))))
    >>> print_link(denominations)
    16 8 4 2 1
    >>> countCoinChange(7, denominations)
    6
    >>> countCoinChange(10, denominations)
    14
    >>> countCoinChange(20, denominations)
    60
    """
    "*** YOUR CODE HERE ***"


    if amount == 0:
        return 1
    if amount < 0 or denominations == empty:
        return 0

    with_change = countCoinChange(amount - first(denominations), denominations)
    without_change = countCoinChange(amount, rest(denominations))

    return with_change + without_change

# Linked list ADT
# Interface Definitions and Implementations
empty = 'empty'

def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (type(s) == list and len(s) == 2 and is_link(s[1]))

# traverses 
def link_length(lst):
    if lst == empty:
        return 0
    if not is_link(rest(lst)):
        return 1
    else:
        return 1 + link_length(rest(lst))

def link(first, rest=empty):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), 'rest must be a linked list.'
    return [first, rest]

def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), 'first only applies to linked lists.'
    assert s != empty, 'empty linked list has no first element.'
    return s[0]

def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), 'rest only applies to linked lists.'
    assert s != empty, 'empty linked list has no rest.'
    return s[1]

def print_link(s):
    """Print elements of a linked list s.

    >>> s = link(1, link(2, link(3, empty)))
    >>> print_link(s)
    1 2 3
    """
    line = ''
    while s != empty:
        if line:
            line += ' '
        line += str(first(s))
        s = rest(s)
    print(line)

if __name__ == "__main__":
  doctest.testmod(verbose=True)