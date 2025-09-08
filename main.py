from stats import get_num_words, get_char_text, dir_to_list
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    get_book_text(sys.argv[1])

def get_book_text(book_name):
    with open(book_name) as text:
        content = text.read()
    num_words = get_num_words(content)
    char_dir = get_char_text(content)
    list_of_dir = dir_to_list(char_dir)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dir in list_of_dir:
        if dir["char"].isalpha():
            print(f"{dir['char']}: {dir['num']}")
    print("============= END ===============re")

main()