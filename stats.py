def get_book_word_count(book_text):
    return len(book_text.split())

def get_book_character_counts(book_text):
    letter_counts = { }
    
    for letter in book_text.lower():
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    return letter_counts

def sort_character_counts(character_dictionary):
    character_list = []

    for character in character_dictionary:
        if not character.isalpha():
            continue

        character_section = {}
        character_section["char"] = character
        character_section["num"] = character_dictionary[character]
        character_list.append(character_section)

    character_list.sort(reverse = True, key = sort_on)
    
    return character_list

def sort_on(character_list):
    return character_list["num"]