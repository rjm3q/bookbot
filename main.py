from stats import (count_words, character_count, make_report)

def main():
    path = 'books/frankenstein.txt'
    file_contents = get_book_text(path)
    word_count = count_words(file_contents)
    char_count = character_count(file_contents)
    sorted_char = make_report(char_count)
    print_report(path, word_count, sorted_char)
    
def get_book_text(filepath):
    with open(filepath) as f:   
        return f.read()
    
def print_report(path, word_count, sorted_char):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_char:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    
main()