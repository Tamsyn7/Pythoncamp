#get the list of arguments

import sys
words = sys.argv[1:]

words.sort()

last_word = words [-1]

all_but_last_word = words[:-1]

sentence = ','.join(all_but_last_word)

sentence += ', and ' + last_word + '.'

print sentence

