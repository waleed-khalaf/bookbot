def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    print(f"{word_count} words found in the document")
    count_characters(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(words_to_count):
    words = words_to_count.split()
    word_count = len(words)
    return word_count


def count_characters(text):
    letter_count = { "a" : 0,
               "b" : 0,
               "c" : 0,
               "d" : 0,
               "e" : 0,
               "f" : 0,
               "g" : 0,
               "h" : 0,
               "i" : 0,
               "j" : 0,
               "k" : 0,
               "l" : 0,
               "m" : 0,
               "n" : 0,
               "o" : 0,
               "p" : 0,
               "q" : 0,
               "r" : 0,
               "s" : 0,
               "t" : 0,
               "u" : 0,
               "v" : 0,
               "w" : 0,
               "x" : 0,
               "y" : 0,
               "z" : 0,}
    for letter in text:
        lower_case = letter.lower()
        if lower_case in letter_count:
            letter_count[lower_case] += 1
        else:
            continue
    return letter_count

main()
