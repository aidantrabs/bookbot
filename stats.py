def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def get_num_words(content):
    counter = 0
    word_list = content.split()

    counter += len(word_list)

    return counter

def get_num_chars(content):
    num_character_dict = {}
    unique_chars = list(set(content))
    word_list = content.split()

    for char in unique_chars:
        char = char.lower()
        num_character_dict[char] = 0

    for word in word_list:
        for char in word:
            char = char.lower()
            for letter in unique_chars:
                if char == letter:
                    num_character_dict[letter] += 1
            
    return num_character_dict

def sort_chars_count(char_dict):
    sorted_dict = {}

    for key in sorted(char_dict, key=char_dict.get, reverse=True):
        sorted_dict[key] = char_dict[key]

    return sorted_dict