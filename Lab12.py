_author_ = "Cameron Clarke"
_credits_ = ["Cameron Clarke", "Nick Barth"]
_email_ = "clarkeck@mail.uc.edu"

import doctest

#RQ1
class Cheer:
    """
    >>> UC = Cheer("Bearcats")
    >>> for c in UC:
    ...     print(c)
    ...
    Give me an B
    Give me an e
    Give me an a
    Give me an r
    Give me an c
    Give me an a
    Give me an t
    Give me an s
    """
    def __init__(self, term):
        self.startVal = 0
        self.term = term
    
    def __next__(self):
        if self.startVal == len(self.term):
            raise StopIteration
        self.startVal += 1 
        return "Give me an " + str(self.term[self.startVal-1])
    
    def __iter__(self):
        return self


#RQ2
class Countdown:
    """
    An iterator that counts down from N to 0.
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in Countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    def __init__(self, value):
        self.start = value
    
    def __next__(self):
        if self.start == -1:
            # checks if illegal out of bounds value
            raise StopIteration
        self.start -= 1 
        return str(self.start + 1)
    
    def __iter__(self):
        return self   
    


##############
# Generators #
##############

# RQ3
def evens():
    """A generator function that yields the infinite sequence of all even natural
    numbers, starting at 1.

    >>> m = evens()
    >>> type(m)
    <class 'generator'>
    
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    i = 0
    while i > -1:
        i += 1 
        yield i * 2
    
def naturals():
    """A generator function that yields the infinite sequence of all even natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    counter = 0

    while counter > -1:
        counter += 1        
        yield counter
    

#RQ4
def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    if type(s) == list:
        for item in range(len(s)):
            yield s[item] * k
    else:
        while True:
            yield s.__next__() * k
    

# RQ5
def countdown(n):
    """
    A generator that counts down from N to 0.
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    for i in range(n + 1):
        yield(n - i)


# RQ6
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    # stop is flag to tell program when n = 1
    stop = False
    yield n
    while not stop :
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        yield n
        if n == 1:
            stop = True

if __name__ == "__main__":
  doctest.testmod(verbose=True)