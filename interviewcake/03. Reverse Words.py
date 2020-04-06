# https://www.interviewcake.com/question/python3/reverse-words
def reverse_words(message):
    # First we reverse all the characters in the entire message
    reverse(message, 0, len(message)-1)

    # Now reverse each word's characters until we hit a space
    word_start = 0

    for i in range(len(message) + 1):
        # Found the end of the current word
        if i == len(message) or message[i] == ' ':
            reverse(message, word_start, i - 1)
            # Next word's start is one character ahead
            word_start = i + 1


def reverse(message, left_index, right_index):
    # Walk towards the middle, from both sides
    while left_index < right_index:
        # Swap the left char and right char
        message[left_index], message[right_index] = \
            message[right_index], message[left_index]
        left_index += 1
        right_index -= 1


message = ['c', 'a', 'k', 'e', ' ',
           'p', 'o', 'u', 'n', 'd', ' ',
           's', 't', 'e', 'a', 'l']
print(''.join(message))
reverse_words(message)
print(''.join(message))
