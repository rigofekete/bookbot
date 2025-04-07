from stats import (
        count_words,
        char_check,
        sort_list
)

import sys

def get_book_text(path):
    with open(path) as f:
        contents = f.read()

    return contents


def print_func(book_path, num_words, sorted_dict_list):
    print("=========== BOOKBOT =============")
    print(f"Analazing book found at {book_path}...")
    print("---------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("---------- Character Count ------")
    for pair in sorted_dict_list:
        if pair["char"].isalpha():
            print(f"{pair["char"]}: {pair["count"]}")
    print("============== END =================")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = count_words(text)
    chars_dict = char_check(text)
    sorted_dict_list = sort_list(chars_dict)
    print_func(book_path, num_words, sorted_dict_list)   


main()

