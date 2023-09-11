def is_semordnilap(word):
    return word == word[::-1]
word1 = "level"
word2 = "deified" 
word3 = "hello"
print(is_semordnilap(word1))  
print(is_semordnilap(word2))  
print(is_semordnilap(word3)) 
