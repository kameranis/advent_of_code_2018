import sys

words = []
with open(sys.argv[1], 'r') as f:
    words = list(f)
length = len(words[0])
for i, word1 in enumerate(words):
    for word2 in words[i+1:]:
        counter = 0
        for letter_1, letter_2 in zip(word1, word2):
            counter += (letter_1 == letter_2)
        if counter == length - 1:
            for letter_1, letter_2 in zip(word1, word2):
                if letter_1 == letter_2:
                    print(letter_1, end='')
            print
            break

