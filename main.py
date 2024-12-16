def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_dict = count_characters(text)
    sort_on(char_dict)

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
            dict_list.append({"char": f"{key}", "count" : f"{dict[key]}"})
    return dict_list

def sort_on(dict):
    return dict["count"]

def print_report(path, num_words, char_dict):
    print(f"--- Begin report of {path} ---")
    print(f"{num_words} words found in the document")
    # TODO: print out in descending order, letters and the number of times they appear
    print("--- End of report ---")

main()
