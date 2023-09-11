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
                    
         
def longest_semordnilap_v1(words_list):
    ret = ''
    for word in words_list:
        if word[::-1] in word_list:
            if len(ret)<len(word):
                ret = word
    return ret

print(longest_semordnilap_v1(word_list))