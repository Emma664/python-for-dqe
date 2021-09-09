import csv

# read file, lowercase all text, split by words,
# for each word leave only letters (to get rid of all numbers, etc)
# create a new list with words only, count the number of words

with open("volha_newsfeed.txt") as f:
    csv_body = f.read()
csv_body_lowered = csv_body.lower()
words = csv_body_lowered.split()
words_only = []
for word in words:
    new_word = ''
    for i in range(len(word)):
        if word[i].isalpha():
            new_word += word[i]
    if new_word != '':
        words_only.append(new_word)


# create a csv, write the number of words to csv
with open('words_count.csv', 'w') as csvfile:
    csvfile.write(str(len(words_only)))

# read file, split by words,
# for each word leave only letters (to get rid of all numbers, etc)
# create a new list with words only, make it a string with all words from the file
with open("volha_newsfeed.txt") as f:
    csv_body = f.read()
words = csv_body.split()
words_only = []
for word in words:
    new_word = ''
    for i in range(len(word)):
        if word[i].isalpha():
            new_word += word[i]
    if new_word != '':
        words_only.append(new_word)
words_only_joined = ''.join(words_only)

# work with string containing all words
# for each letter of the alphabet, count number of letters in the text
# the same for upper case letters
# add all counts into two lists
alphabet = 'qwertyuiopasdfghjklzxcvbnm'
alphabet_uppercase = 'QWERTYUIOPASDFGHJKLZXCVBNM'
count_all_list = []
count_upper_list = []
for letter in alphabet:
    count_all = words_only_joined.count(letter)
    count_all_list.append(count_all)
for letter in alphabet_uppercase:
    count_upper = words_only_joined.count(letter)
    count_upper_list.append(count_upper)
all_letters = len(words_only_joined)

# for each letter create a list with counts and calculate percentage
# use csv module to add rows to csv
with open('letters_count.csv', 'w', newline='') as csvfile:
    headers = ['letter', 'count_all', 'count_uppercase', 'percentage']
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    for letter in alphabet:
        index_letter = alphabet.index(letter)
        count_letter = count_all_list[index_letter]
        count_upper_letter = count_upper_list[index_letter]
        count_percent = int(count_letter) + int(count_upper_letter) / all_letters * 100
        row = [letter, count_letter, count_upper_letter, int(count_percent)]
        writer.writerow(row)
