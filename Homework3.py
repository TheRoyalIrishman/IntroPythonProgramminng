from urllib.request import urlopen

def load_words(url: str):
    # opens up the file given from the URL
    wordfile = urlopen(url)
    # reads all of the words from a long list and splits the list on the new line character
    words = wordfile.read().decode('utf-8').upper().split()
    # returns the list as a set, as sets are quicker to sort through than compared to a list
    return set(words)

def allsteps(word: str):

    # conversion to upper case
    word = word.upper()
    # list that will contain the results
    result = []
    
    # ord("A") = 65
    # ord("Z") = 90
    # this for loop will iterate through the ASCII values of all the letters in the alphabet
    for i in range(ord('A'), ord('Z') + 1):
        newWord = word + chr(i)
        # fancy array loop that checks if all the possible words are sorted
        # creates all possible anagrams of a given input word
        anagrams = [word for word in words if sorted(word) == sorted(newWord)]
        # adds anagram to list
        result.extend(anagrams)
    
    return result

# Load the list of English words from the provided source
url = "http://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt"
words = load_words(url)

# Test cases
print(allsteps("APPLE"))
print(allsteps("UC"))
print(allsteps("BEARCAT"))