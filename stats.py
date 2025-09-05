def get_word_count(book_text: str):
    return len(book_text.split())

def get_character_occurence(book_text: str):
    words = book_text.split()
    res_dic = {}
    for word in words :
        for char in word :
            char = char.lower()
            if char in res_dic :
                res_dic[char] += 1
            else:
                res_dic[char] = 1
    
    return res_dic

def get_sorted_char_occurance_dics(raw_char_occurance):
    res_list = []
    for char in raw_char_occurance:
        res_list.append({"char" : char, "num" : raw_char_occurance[char]})

    res_list.sort(reverse = True, key = sort_by)

    return res_list

def sort_by(items):
    return items["num"]