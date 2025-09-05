import sys
from stats import get_word_count
from stats import get_character_occurence
from stats import get_sorted_char_occurance_dics

book_path = ""

def get_book_text(filepath: str) :
    res: str

    with open(filepath) as f:
        res = f.read()
    
    return res

def print_shenanigans(words_num, sorted_char_stats_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_num} total words")
    print("--------- Character Count -------")
    for char in sorted_char_stats_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

def main():
    if len(sys.argv) <= 1 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    words_num = get_word_count(text)
    sorted_char_stats_list = get_sorted_char_occurance_dics(get_character_occurence(text))
    print_shenanigans(words_num, sorted_char_stats_list)

main()
