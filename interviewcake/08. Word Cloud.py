def get_word(start, count, text):
    return text[start: start + count].lower()


def insert_word_in_map(word, map):
    if word not in map:
        map[word] = 0
    map[word] += 1


def build_word_cloud(text):
    map = {}
    start_word = 0
    char_count = 0
    for i in range(1, len(text) + 1):
        if text[i-1].isalpha():
            char_count += 1
        else:
            word = get_word(start_word, char_count, text)
            insert_word_in_map(word, map)
            start_word = start_word + char_count + 1
            char_count = 0

    word = get_word(start_word, char_count, text)
    insert_word_in_map(word, map)

    return map


print(build_word_cloud('After beating the eggs, Dana read the next step:'))
