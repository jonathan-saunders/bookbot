def main():
    book_path = "/home/jonathansaunders/workspace/github.com/jonathan-saunders/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_words(text)
    chars = check_freq(text.lower())
    sorted_chars = dict_to_sorted_list(chars)
    print(f"Begin report of {book_path}")
    print(f"{words} words found in document")
    for item in sorted_chars:
        if not item["char"].isalpha():
            continue
        print(f"The character '{item['char']}' was found {item['num']} times.")
    print("End report")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_words(text):
    words = text.split()
    return len(words)

def check_freq(x):
    freq = {}
    for c in set(x):
       freq[c] = x.count(c)
    return freq

def sort_on(dict):
    return dict["num"]

def dict_to_sorted_list(dict):
    sorted_list = []
    for ch in dict:
        sorted_list.append({"char": ch, "num":dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()