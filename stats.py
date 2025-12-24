def get_total_words(contents):
    total = 0
    for line in contents:
        cont = line.split()
        for word in cont: total += 1
    return total

def count_characters(contents):
    char_dict = {}
    for line in contents:
        cont = line.split()
        for word in cont:
            for char in word:
                char = char.lower()
                if char in char_dict: char_dict[char] += 1
                else: char_dict[char] = 1
    return char_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.readlines()
    return file_contents

def report(filepath):
    txt = get_book_text(filepath)
    total = get_total_words(txt)
    char_dict = count_characters(txt)
    ##sort dictionary
    sorted_char_dict = dict(sorted(char_dict.items(), key = lambda x: x[1], reverse = True))

    ## Print
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print(f"----------- Word Count ----------")
    print(f"Found {total} total words")
    print(f"--------- Character Count -------")
    for key, value in sorted_char_dict.items():
        print(f"{key}: {value}")
    print("============= END ===============")
