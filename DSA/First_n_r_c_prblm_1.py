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

