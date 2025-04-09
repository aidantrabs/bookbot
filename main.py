import sys
from stats import get_num_words, get_book_text, get_num_chars, sort_chars_count

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]

        content = get_book_text(filepath)
        num_words = get_num_words(content)
        char_dict = get_num_chars(content)
        sorted_dict = sort_chars_count(char_dict)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for key in sorted_dict:
            if key.isalpha():
                print(f"{key}: {sorted_dict[key]}")
        print("============= END ===============")

if __name__ == "__main__":
    main()