def get_num_words(book_text):
    word_list = book_text.split()
    count = 0
    for i in range(0, len(word_list)):
        count += 1
    return count


def get_char_text(book_text):
    char_dir = {}

    for char in book_text.lower():
        if char in char_dir:
            char_dir[char] += 1
        else:
            char_dir[char] = 1

    return char_dir

def dir_to_list(char_dir):
    new_list = []
    for key, value in char_dir.items():
        new_list.append({"char": key, "num": value})
    new_list.sort(reverse=True, key=sort_on)
    return new_list

def sort_on(items):
    return items["num"]