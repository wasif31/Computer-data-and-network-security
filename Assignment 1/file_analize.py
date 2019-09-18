import re


def find_word_freq(freq={}, word=""):
    if word in freq:
        freq[word] = freq[word]+1
    else:
        freq[word] = 1
    return freq


def print_freq(freq={}, header=""):
    print("\n", "*"*20, header, "*"*20)
    print()
    for key in sorted(freq.keys()):
        print(key, ": ", freq[key], end=" | ")
    print("\n\n", "_"*50)


def analyzing_file():
    words=[]
    one_letter_freq = {}
    two_letter_freq = {}
    three_letter_freq = {}

    with open("data.txt", "r") as file:
        lines = file.readlines()
        line = lines[0]
        line = re.sub(",", " ", line)
        line = re.sub("\.+", " ", line)
        line = re.sub("\!+", " ", line)
        line = re.sub(" +", " ", line)
        words = line.split(" ")

    for word in words:
        if len(word) == 1:
            one_letter_freq = find_word_freq(one_letter_freq, word)
        if len(word) == 2:
            two_letter_freq = find_word_freq(two_letter_freq, word)
        if len(word) == 3:
            three_letter_freq = find_word_freq(three_letter_freq, word)

    print_freq(one_letter_freq, "One Letter Frequency")
    print_freq(two_letter_freq, "Two Letter Frequency")
    print_freq(three_letter_freq, "Three Letter Frequency")

    letter_freq = {}
    for letter in line:
        if letter in letter_freq:
            letter_freq[letter] = letter_freq[letter]+1
        else:
            letter_freq[letter] = 1

    print("*"*20, "Individual Character", "*"*20, "\n")
    for letter in sorted(letter_freq.keys()):
        print(letter, ": ", letter_freq[letter], end=" | ")
    print("\n\n", "_"*50)


analyzing_file()