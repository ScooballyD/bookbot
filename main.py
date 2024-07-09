def main():
    path_to_file = "books/frankenstein.txt"
    book = read_book(path_to_file)
    words = book.split()
    
    get_letters(book.lower())
    split_dict(char_count)
    
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{len(words)} words found in the document")
    print("")
    
    dict_list.sort(reverse=True, key=sort_on)
    for dict in dict_list:
        ltr = dict["ltr"]
        num = dict["num"]
        print(f"The '{ltr}' character was found {num} times")
    
    print("--- End report ---")
    

char_count = {}
dict_list = []

def read_book(path):
    with open(path) as f:
        return f.read() 

def get_letters(text):
    for letter in text:
        if letter in char_count:
            char_count[letter] += 1
        elif letter.isalpha() == True:
            char_count[letter] = 1
    return char_count

def sort_on(dict):
    return dict["num"]

def split_dict(dict):
    for key in dict:
        tmp_dict = {}
        tmp_dict["ltr"] = key
        tmp_dict["num"] = dict[key]
        dict_list.append(tmp_dict)




main()