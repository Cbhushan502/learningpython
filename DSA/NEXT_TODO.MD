# Top problems based on semordnilap

## Semordnilap?

If you look carefully at the word semordnilap, you might notice that it’s palindromes spelled backward. While a palindrome is a word or phrase that reads the same in both directions, a semordnilap is one that spells a different word or phrase in reverse.

You can have a lot of fun with semordnilaps in your writing, especially in fiction and poetry. The clever use of semordnilaps can add extra layers of meaning or humor and increase readers’ enjoyment of your words.

## Problem 1: Semordnilap Pairs in a List
 Given a list of words, find all semordnilap pairs present in the list. A semordnilap pair is a pair of words that, when spelled backward, forms another valid word. 

Pyhton 3.8

```
def is_semordnilap(word1, word2):
    return word1[::-1] == word2

def find_semordnilap_pairs(word_list):
    semordnilap_pairs = []
    seen_words = set()
    for word in word_list:
        word_lower = word.lower()
        if word_lower not in seen_words:
            reversed_word = word_lower[::-1]
            if reversed_word in word_list:
                semordnilap_pairs.append((word, reversed_word))
            seen_words.add(word_lower)  
    return semordnilap_pairs
word_list = ["cod", "ein", "python", "3.8", "dog", "god", "apple", "elppa", "banana", "ananab", "car", "rac"]
result = find_semordnilap_pairs(word_list)
print(result)

```
## Problem 2: Longest Semordnilap in a List
Given a list of words, find the longest semordnilap (if any) present in the list. A semordnilap is a word that, when spelled backward, forms another valid word.

Python 3.8

```
def is_semordnilap(word1, word2):
    return word1[::-1] == word2

def find_longest_semordnilap(words):
    longest_semordnilap = ""
    for i, word1 in enumerate(words):   
        for j, word2 in enumerate(words):
            if i !=j and is_semordnilap(word1, word2):
                if len(word1) > len(longest_semordnilap):
                    longest_semordnilap = word1
    return longest_semordnilap

word_list = ["diaper", "repaid", "gateman", "nametag", "desserts", "stressed"]
result = find_longest_semordnilap(word_list)
print("Longest semordnilap word:", result)

                    OR
         
         
def longest_semordnilap_v1(words_list):
    ret = ''
    for word in words_list:
        if word[::-1] in word_list:
            if len(ret)<len(word):
                ret = word
    return ret

print(longest_semordnilap_v1(word_list))

```

## Problem 3: Semordnilap Checker
Write a function that takes a word as input and returns True if it is a semordnilap, and False otherwise.

Python 3.8

```
def is_semordnilap(word):
    return word == word[::-1]
word1 = "level"      #This is semordnilap means TRUE
word2 = "deified"    #This is semordnilap measn TRUE
word3 = "hello"      #This is not semordnilap means FALSE
print(is_semordnilap(word1))  
print(is_semordnilap(word2))  
print(is_semordnilap(word3)) 

```

## Problem 4: Semordnilap Words in a Text File
Given a text file containing a list of words (one word per line), find all semordnilap pairs present in the file.

Pyhton 3.8

```
def is_semordnilap(word1, word2):

    if len(word1) == len(word2) and word1 != word2:
        
        return word1[::-1] == word2
    return False

def find_semordnilap_pairs_in_file(file_path):
    semordnilaps = []
    with open(file_path, 'r') as file:
        words = [word.strip() for word in file]
        
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if is_semordnilap(words[i], words[j]):
                semordnilaps.append((words[i], words[j]))
    
    return semordnilaps

file_path = "/home/csaran/Desktop/Words"
semordnilap_pairs = find_semordnilap_pairs_in_file(file_path)
print(semordnilap_pairs)

``` 
# Top Problems based on First Non-repeating character

## Problem 1:Given a string, find and return the first non-repeating character. If there are no non-repeating characters, return None.

Python 3.8

```
def first_non_repeating_char(input_str):
    char_count = {} # i'm takeing  dictionary to store character counts

    for char in input_str:
        char_count[char] = char_count.get(char, 0) + 1

    for char in input_str:
        if char_count[char] == 1:
            return char 
        
    return None  


input_string = "aabbccd"
result = first_non_repeating_char(input_string)
if result:
    print("First non-repeating character:", result)
else:
    print("No non-repeating character found.")    

#Output:d

```

## Problem 2: First Non-repeating Character in Stream
You are given a stream of characters. Implement a function that processes the characters one by one and returns the first non-repeating character after each new character is processed.

Python 3.8

```














