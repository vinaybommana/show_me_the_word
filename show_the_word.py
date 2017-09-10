import os
import time
import fileinput
import numpy as np
# import random

# words contain all the lines in the "vocabulary_words.md" file.
words = []

# I've got this type of reading ".md" files from python documentation
with fileinput.input(files=('vocabulary_words.md')) as f:
    for line in f:
        words.append(line)


def show_word(word):
    # we can change to whatever time in seconds we want.
    time.sleep(60)
    # print(word)
    # The words in vocabulary.md are in the form
    # * base_word - meaning
    # so initially we split the word using "-" delimiter
    words_list = word.split("-")
    # print(words_list)
    # we've captured the base word and stripping the "* " from the word.
    base_word = words_list[0].strip("* ")
    # print(base_word)
    # some base_words may not have meanings :(
    # so we need to show only the base_word
    if len(words_list) > 1:
        meaning = words_list[1].strip("\n")
        # notify-send is a linux program
        # it is not related to python in anyway
        os.system('notify-send "{}" "{}"'.format(base_word, meaning))
        # this should be the best line of the entire program
        # I've found the only use of formatting here in learning
        # from Zed shaw's learn python the hard way
        # and a little help from stack overflow.
    else:
        os.system('notify-send "{}"'.format(base_word))


def main():
    while True:
        # we've used numpy's random.choice for diversity in the random
        # choices.
        show_word(np.random.choice(words))


if __name__ == "__main__":
    main()
