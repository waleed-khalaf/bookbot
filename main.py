def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_dict = count_characters(text)
    list_of_chars = dict_to_list(char_dict)
    print_report(book_path, word_count, list_of_chars)

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

def dict_to_list(dict):
    dict_list = []
    for key in dict:
        if key.isalpha():
            # add to list as dict with separate "num" key and its value
            dict_list.append({"char": key, "count" : dict[key]})
    return dict_list

def sort_on(dict):
    return dict["count"]

def print_report(path, num_words, dict_list):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    print()
    dict_list.sort(reverse=True, key=sort_on)
    for i in range(0, len(dict_list)):
        print(f"The '{dict_list[i]['char']}' character was found {dict_list[i]['count']} times")
    print("--- End of report ---")

main()
