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
    char_count = {}
    for char in text:
        lower_case = char.lower()
        if lower_case in char_count:
            char_count[lower_case] += 1
        else:
            char_count[lower_case] = 1
    return char_count

main()
