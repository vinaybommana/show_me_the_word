import os
import time
import fileinput
import numpy as np
# import random

words = []

with fileinput.input(files=('vocabulary_words.md')) as f:
    for line in f:
        words.append(line)


def show_word(word):
    time.sleep(60)
    # print(word)
    words_list = word.split("-")
    # print(words_list)
    base_word = words_list[0].strip("* ")
    # print(base_word)
    if len(words_list) > 1:
        meaning = words_list[1].strip("\n")
        os.system('notify-send "{}" "{}"'.format(base_word, meaning))
        # this should be the best line of the entire program
    else:
        os.system('notify-send "{}"'.format(base_word))


def main():
    while True:
        show_word(np.random.choice(words))


if __name__ == "__main__":
    main()
