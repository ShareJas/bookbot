import sys
from stats import get_total_words, count_characters, get_book_text, report

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    report(sys.argv[1])