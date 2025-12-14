import sys

from stats import get_book_word_count
from stats import get_book_character_counts
from stats import sort_character_counts

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    
    word_count = get_book_word_count(book_text)
    print(f"Found {word_count} total words")

    print("----------- Character Count ----------")

    letter_counts = get_book_character_counts(book_text)
    sorted_letters = sort_character_counts(letter_counts)

    for section in sorted_letters:
        print(f"{section["char"]}: {section["num"]}")

    print("============= END ===============")

main()