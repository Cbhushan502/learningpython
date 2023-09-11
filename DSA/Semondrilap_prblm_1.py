def is_semordnilap(word1, word2):
    # Check if two words are semordnilap by comparing their reversed forms.
    return word1[::-1] == word2

def find_semordnilap_pairs(word_list):
    semordnilap_pairs = []
    seen_words = set()

    for word in word_list:
        # Convert the word to lowercase for case-insensitive matching.
        word_lower = word.lower()

        # Skip duplicate words to avoid counting them as semordnilap pairs with themselves.
        if word_lower not in seen_words:
            reversed_word = word_lower[::-1]
            if reversed_word in word_list:
                # Check if the reversed word exists in the list.
                # If it does, add it as a semordnilap pair.
                semordnilap_pairs.append((word, reversed_word))
            seen_words.add(word_lower)  # Add the word to the set of seen words.

    return semordnilap_pairs

word_list = ["cod", "ein", "python", "3.8", "dog", "god", "apple", "elppa", "banana", "ananab", "car", "rac"]
result = find_semordnilap_pairs(word_list)
print(result)
