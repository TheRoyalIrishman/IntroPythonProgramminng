import doctest
import random
from collections import defaultdict

_author_ = "Cameron Clarke"
_credits_ = ["Cameron Clarke"]
_email_ = "clarkeck@mail.uc.edu" # Your email address

## Lab 5: Required Questions - Dictionaries  ##

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def build_successors_table():
    """Return a dictionary: keys are words; values are lists of successor words. By default, we set the first word in tokens to be a successor to "."
    """
    f = open("shakespeare.txt", "r", encoding="ascii")
    tokens = f.read().split()
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table[prev] = []
        table[prev] += [word]
        prev = word
    return table

def construct_tweet(word, table):
    """Returns a string that is a random sentence starting with word, and choosing successors from table.
    """
    result = ' '
    while word not in ['.', '!', '?']:
        result += word + ' '
        word = random.choice(table[word])
    return result + word

def random_tweet():
    tweet_table = build_successors_table()
    return construct_tweet(random.choice(tweet_table['.']), tweet_table)

# =============================================================================
# MAIN FUNCTIONS
# =============================================================================

# RQ1
def merge(dict1, dict2):
    """Merges two Dictionaries. Returns a new dictionary that combines both. You may assume all keys are unique.

    >>> new =  merge({1: 'one', 3:'three', 5:'five'}, {2: 'two', 4: 'four'})
    >>> new == {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    True
    """
    "*** YOUR CODE HERE ***"
    
    # https://www.geeksforgeeks.org/python-merging-two-dictionaries/
    # source used to help solve this question

    # hint suggests that we sort by the keys
    for item in dict2.keys():
        # this is just another way of indexing values in dictionaries
        # and smushes the items together into one dictionary
        dict1[item] = dict2[item]
    
    return dict1

# RQ2
def counter(message):
    """ Returns a dictionary where the keys are the words in the message, and each
    key is mapped (has associated value) equal 
    to the number of times the word appears in the message.
    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    "*** YOUR CODE HERE ***"
    
    # empty dictionary
    wordsDict = dict()
    
    # this will help split words if there's a space in the message string
    wordsInMessage = message.split()
    
    for word in wordsInMessage:
        if word in wordsDict:
            wordsDict[word] += 1
        else:
            wordsDict[word] = 1

    return wordsDict

# RQ3
def replace_all(d, x, y):
    """ Returns a dictionary where the key/value pairs are the same as d, 
    except when a value is equal to x, then it should be replaced by y.
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> d2= replace_all(d, 3, 'poof')
    >>> d2 == {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    "*** YOUR CODE HERE ***"
    
    # https://chat.openai.com/share/2c252337-ce08-4a09-b362-5f5a43a5a0ac
    # ChatGPT link used to solve this problem
    
    newDict = {}
    for key, value in d.items():
        if value == x:
            newDict[key] = y
        else:
            newDict[key] = value
    return newDict
    
    
# RQ4
def sumdicts(lst):
   """ 
   Takes a list of dictionaries and returns a single dictionary which contains all the keys/value pairs found in list. And 
   if the same key appears in more than one dictionary, then the sum of values in list of dictionaries is returned 
   as the value mapped for that key
   >>> d = sumdicts ([{'a': 5, 'b': 10, 'c': 90, 'd': 19}, {'a': 45, 'b': 78}, {'a': 90, 'c': 10}] )
   >>> d == {'b': 88, 'c': 100, 'a': 140, 'd': 19}
   True
   """
   "*** YOUR CODE HERE ***"
   
   # similar to STL dict
   resultantDict = defaultdict(int)
   
   # iterates through each dictionary in list
   for dictionary in lst:
       # iterates through each key value pair in the dictionary list
       for key, value in dictionary.items():
           resultantDict[key] += value
    
   return resultantDict
            
#RQ5
def middle_tweet():
    """ Calls the function random_tweet() 5 times (see Interactive Worksheet) and 
    returns the one string which has length in middle value of the 5.
    Returns a string that is a random sentence of median length starting with word, 
    and choosing successors from table. It is difficult to write a doctest for this function, 
    since it is randomized. But my experiments showed that with 5 random samples you should usually
    get a tweet that is roughly ordinary size sentence (6-10 words).
    
    >>> len(middle_tweet()) > 60
    True
    >>> len(middle_tweet()) < 100
    True
    
    """
    "*** YOUR CODE HERE ***"
    
    quoteList = []
    
    # appends strings to list
    
    for _ in range(5):
        quoteList.append(random_tweet())
        
    # sort quoteList based on length of strings
    
    quoteList.sort(key = len)
    
    middleIndex = len(quoteList) // 2
    
    outputString = quoteList[middleIndex]
    
    return outputString
        
    

if __name__ == "__main__":
  doctest.testmod(verbose=True)
