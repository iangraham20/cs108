''' text_analysis tests the location of words within the list and compares two lists to find the number of different words
Created October 12, 2016
Lab 6 Exercise 6.1
@author: Ian Christensen (igc2)
@author: Griffin Sparling (grs4)
'''

# Lists for exercise 6.2
empty_list = []
list1 = ['one']
list2 = ['three', 'four', 'elements']

green_eggs_and_ham = [ "i", "am", "sam", "sam", "i", "am", "that",
            "sam-i-am", "that", "sam-i-am", "i", "do", "not", "like", "that", "sam-i-am", "do",
            "you", "like", "green", "eggs", "and", "ham", "i", "do", "not", "like", "them",
            "sam-i-am", "i", "do", "not", "like", "green", "eggs", "and", "ham", "would", "you",
            "like", "them", "here", "or", "there", "i", "would", "not", "like", "them", "here",
            "or", "there", "i", "would", "not", "like", "them", "anywhere", "i", "do", "not",
            "like", "green", "eggs", "and", "ham", "i", "do", "not", "like", "them", "sam-i-am",
            "would", "you", "like", "them", "in", "a", "house", "would", "you", "like", "them",
            "with", "a", "mouse", "i", "do", "not", "like", "them", "in", "a", "house", "i", "do",
            "not", "like", "them", "with", "a", "mouse", "i", "do", "not", "like", "them", "here",
            "or", "there", "i", "do", "not", "like", "them", "anywhere", "i", "do", "not", "like",
            "green", "eggs", "and", "ham", "i", "do", "not", "like", "them", "sam-i-am", "would",
            "you", "eat", "them", "in", "a", "box", "would", "you", "eat", "them", "with", "a",
            "fox", "not", "in", "a", "box", "not", "with", "a", "fox", "not", "in", "a", "house",
            "not", "with", "a", "mouse", "i", "would", "not", "eat", "them", "here", "or", "there",
            "i", "would", "not", "eat", "them", "anywhere", "i", "would", "not", "eat", "green",
            "eggs", "and", "ham", "i", "do", "not", "like", "them", "sam-i-am", "would", "you",
            "could", "you", "in", "a", "car", "eat", "them", "eat", "them", "here", "they", "are",
            "i", "would", "not", "could", "not", "in", "a", "car", "you", "may", "like", "them",
            "you", "will", "see", "you", "may", "like", "them", "in", "a", "tree", "not", "in",
            "a", "tree", "i", "would", "not", "could", "not", "in", "a", "tree", "not", "in", "a",
            "car", "you", "let", "me", "be", "i", "do", "not", "like", "them", "in", "a", "box",
            "i", "do", "not", "like", "them", "with", "a", "fox", "i", "do", "not", "like", "them",
            "in", "a", "house", "i", "do", "not", "like", "them", "with", "a", "mouse", "i", "do",
            "not", "like", "them", "here", "or", "there", "i", "do", "not", "like", "them",
            "anywhere", "i", "do", "not", "like", "green", "eggs", "and", "ham", "i", "do", "not",
            "like", "them", "sam-i-am", "a", "train", "a", "train", "a", "train", "a", "train",
            "could", "you", "would", "you", "on", "a", "train", "not", "on", "a", "train", "not",
            "in", "a", "tree", "not", "in", "a", "car", "sam", "let", "me", "be", "i", "would",
            "not", "could", "not", "in", "a", "box", "i", "could", "not", "would", "not", "with",
            "a", "fox", "i", "will", "not", "eat", "them", "with", "a", "mouse", "i", "will",
            "not", "eat", "them", "in", "a", "house", "i", "will", "not", "eat", "them", "here",
            "or", "there", "i", "will", "not", "eat", "them", "anywhere", "i", "do", "not", "like",
            "them", "sam-i-am", "say", "in", "the", "dark", "here", "in", "the", "dark", "would",
            "you", "could", "you", "in", "the", "dark", "i", "would", "not", "could", "not", "in",
            "the", "dark", "would", "you", "could", "you", "in", "the", "rain", "i", "would",
            "not", "could", "not", "in", "the", "rain", "not", "in", "the", "dark", "not", "on",
            "a", "train", "not", "in", "a", "car", "not", "in", "a", "tree", "i", "do", "not",
            "like", "them", "sam", "you", "see", "not", "in", "a", "house", "not", "in", "a",
            "box", "not", "with", "a", "mouse", "not", "with", "a", "fox", "i", "will", "not",
            "eat", "them", "here", "or", "there", "i", "do", "not", "like", "them", "anywhere",
            "you", "do", "not", "like", "green", "eggs", "and", "ham", "i", "do", "not", "like",
            "them", "sam-i-am", "could", "you", "would", "you", "with", "a", "goat", "i", "would",
            "not", "could", "not", "with", "a", "goat", "would", "you", "could", "you", "on", "a",
            "boat", "i", "could", "not", "would", "not", "on", "a", "boat", "i", "will", "not",
            "will", "not", "with", "a", "goat", "i", "will", "not", "eat", "them", "in", "the",
            "rain", "i", "will", "not", "eat", "them", "on", "a", "train", "not", "in", "the",
            "dark", "not", "in", "a", "tree", "not", "in", "a", "car", "you", "let", "me", "be",
            "i", "do", "not", "like", "them", "in", "a", "box", "i", "do", "not", "like", "them",
            "with", "a", "fox", "i", "will", "not", "eat", "them", "in", "a", "house", "i", "do",
            "not", "like", "them", "with", "a", "mouse", "i", "do", "not", "like", "them", "here",
            "or", "there", "i", "do", "not", "like", "them", "anywhere", "i", "do", "not", "like",
            "green", "eggs", "and", "ham", "i", "do", "not", "like", "them", "sam-i-am", "you",
            "do", "not", "like", "them", "so", "you", "say", "try", "them", "try", "them", "and",
            "you", "may", "try", "them", "and", "you", "may", "i", "say", "sam", "if", "you",
            "will", "let", "me", "be", "i", "will", "try", "them", "you", "will", "see", "say",
            "i", "like", "green", "eggs", "and", "ham", "i", "do", "i", "like", "them", "sam-i-am",
            "and", "i", "would", "eat", "them", "in", "a", "boat", "and", "i", "would", "eat",
            "them", "with", "a", "goat", "and", "i", "will", "eat", "them", "in", "the", "rain",
            "and", "in", "the", "dark", "and", "on", "a", "train", "and", "in", "a", "car", "and",
            "in", "a", "tree", "they", "are", "so", "good", "so", "good", "you", "see", "so", "i",
            "will", "eat", "them", "in", "a", "box", "and", "i", "will", "eat", "them", "with",
            "a", "fox", "and", "i", "will", "eat", "them", "in", "a", "house", "and", "i", "will",
            "eat", "them", "with", "a", "mouse", "and", "i", "will", "eat", "them", "here", "and",
            "there", "say", "i", "will", "eat", "them", "anywhere", "i", "do", "so", "like",
            "green", "eggs", "and", "ham", "thank", "you", "thank", "you", "sam-i-am"]

stop_words = [ "a", "able", "about", "across", "after", "all",
            "almost", "also", "am", "among", "an", "and", "any", "are", "as", "at", "be",
            "because", "been", "but", "by", "can", "cannot", "could", "dear", "did", "do", "does",
            "either", "else", "ever", "every", "for", "from", "get", "got", "had", "has", "have",
            "he", "her", "hers", "him", "his", "how", "however", "i", "if", "in", "into", "is",
            "it", "its", "just", "least", "let", "like", "likely", "may", "me", "might", "most",
            "must", "my", "neither", "no", "nor", "not", "of", "off", "often", "on", "only", "or",
            "other", "our", "own", "rather", "said", "say", "says", "she", "should", "since", "so",
            "some", "than", "that", "the", "their", "them", "then", "there", "these", "they",
            "this", "tis", "to", "too", "twas", "us", "wants", "was", "we", "were", "what", "when",
            "where", "which", "while", "who", "whom", "why", "will", "with", "would", "yet", "you",
            "your" ]

# Exercise 6.1
print('Number of words in Green Eggs and Ham:', len(green_eggs_and_ham))

# Create search function.
def search(target, str_list):
    position = 0
    for element in str_list:
        if target == element:
            return position
        position += 1
    return -1
print(search('', green_eggs_and_ham))

def test_search():
    print('Test empty list:', search('hi', empty_list) == -1)
    print('Test list for valid string:', search('one', list1) == 0)
    print('Test list for invalid string:', search('two', list1) == -1)
    print('Test second string for valid string:', search('four', list2) == 1)
    print('Test second string for invalid string:', search('five', list2) == -1)
test_search()


'''
create maximum variable and assign the value to zero
start for loop to find maximum and minimum
use if statement to find maximum length
assign maximum length to maximum variable
assign maximum to minimum variable
if the string is shorter than the first variable assign to second variable
print lengths of variable one and two
'''

# Exercise 6.4, searching for the longest and shortest strings.
def longest_and_shortest(str_list):
    max_char = 0
    for element in str_list:
        if max_char < len(element):
            max_char = len(element)
    min_char = max_char
    for element in str_list:
        if min > len(element):
            min_char = len(element)
    return(min_char, max_char)

'''
create definition
create variable and assign it to zero
use for loop to search first list for words in second list
assign variable to variable plus one if word is not in the second list
return the statement
'''

# Exercise 6.5, create a function that searches two lists and returns total of missing words
def count_words_not_present(list_one, list_two):
    num_words = 0
    for element in list_one:
        if search(element, list_two):
            num_words += 1
    return num_words

# Exercise 6.3, analysis that determines the index of tested strings
def green_eggs_and_ham_analysis():
    print("Index of 'i':", search('i', green_eggs_and_ham))
    print("Index of 'boat':", search('boat', green_eggs_and_ham))
    print("Index of 'fox':", search('fox', green_eggs_and_ham))
    print("Index of 'thank':", search('thank', green_eggs_and_ham))
    print("Index of 'book':", search('book', green_eggs_and_ham))
    print("Number of words in green eggs and ham that are not in stop words:", count_words_not_present(green_eggs_and_ham, stop_words))
green_eggs_and_ham_analysis()