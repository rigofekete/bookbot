def count_words(text):
    num_words = text.split()
    return len(num_words)

def char_check(text):
    char_dict = {}

    lower_text = text.lower()

    for c in lower_text:
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1

    return char_dict

def sort_list(char_dict):
    dict_list = []
    for key in char_dict:
       #value = char_dict[key]
        dict_list.append({"char": key, "count": char_dict[key]})

    def sort_on(dict_list):
        return dict_list["count"]

    dict_list.sort(reverse=True, key=sort_on)
    return dict_list


        


