book_path = "/home/r3d3mption/workspace/github.com/r3d3mption/bookbot/books/frankenstein.txt"


def main():
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

def count_letters(text):
    words = text.split()
    count = {}
    for _ in words:
        _ = _.lower()
        if _ in count:
            count[_] += 1
        else:
            count[_] = 1

    return count


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(book_path) as f:
        return f.read()


main()