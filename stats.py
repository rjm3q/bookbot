def count_words(file_contents):
    words = file_contents.split()
    return len(words)

def character_count(file_contents):
    chars = {}
    for c in file_contents:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def make_report(data_dict):
    sorted_list=[]
    for ch in data_dict:
        sorted_list.append({"char": ch, "num":data_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list