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













