import random

# A function to create a list of random number of dicts
def generate_dictionaries():
    list_of_dictionaries = []
    letters_keys = 'qwertyuiopasdfghjklzxcvbnm'
    for i in range(random.randint(2, 10)):
        # add to dictionary name a number to differentiate dictionaries
        # dictionary_name = 'dictionary' + str(i)
        dictionary_name = {}
        # generate random number of key: value pairs in each dictionary
        for j in range(random.randint(2, 10)):
            # for a key we use choice() function from random module
            # we choose random letter from list of alphabet
            # for value we choose random integer from 0 to 100
            dictionary_name[random.choice(letters_keys)] = random.randint(0, 100)
        # we append to empty list_of_dictionaries every dictionary,
        # so each item of a list is a dictionary
        list_of_dictionaries.append(dictionary_name)
    return list_of_dictionaries


# A function to create common dictionary from a list of random number of dicts
def create_common_dictionary(arbitrary_list):
    # create empty dictionary to union all key: value pairs from dictionaries in the list
    union_dict = {}
    # create empty list to keep all keys from all dictionaries
    keys_all = []
    # create empty list to keep unique keys
    keys_unique = []
    # create empty list to keep shared keys
    keys_shared = []

    for dictionary in arbitrary_list:
        keys_all.extend(list(dictionary.keys()))

    # we use count() function to count appearances of an item in the list
    # if an item appears only once, we add it to the list of unique keys
    for item in keys_all:
        if keys_all.count(item) == 1:
            keys_unique.append(item)
        # if an item appears more then once, we add it to the list of shared keys
        # we check if it is not already there, to avoid duplicates
        elif item not in keys_shared:
            keys_shared.append(item)

    # for each dictionary in our list of dictionaries
    # we check whether each key is in the list of unique keys
    # and if it is, we add this key with its value to the common dictionary
    for dictionary in arbitrary_list:
        for key in dictionary:
            if key in keys_unique:
                union_dict[key] = dictionary[key]

    # we iterate through the list of shared keys
    for key in keys_shared:
        # create a variable to keep the maximum value of shared keys
        max_value = 0
        # create a variable to keep the index number of dictionary with maximum value of shared key
        index_of_max = 0
        # we iterate through the elements(which are dictionaries) of the list with dictionaries
        for i in range(len(arbitrary_list)):
            # if shared key is in keys of a dictionary
            # and its value is greater than maximum value of this key
            # we assign its value to the max_value
            # and write the number of the dictionary to the variable index_of_max
            # we add 1 to this number, because indexing starts with 0
            if key in arbitrary_list[i] and max_value < arbitrary_list[i][key]:
                max_value = arbitrary_list[i][key]
                index_of_max = i + 1
        # we add a key: value pair to the common dictionary
        # key is shared key concatenated with the number of dictionary
        # where there is maximum value of this shared key
        # value is max_value
        union_dict[key + '_' + str(index_of_max)] = max_value
    return union_dict


print(create_common_dictionary(generate_dictionaries()))


# A function which normalizes any text from letter cases point of view
def normalize_case(text):
    text_capitalized = '. '.join([item.strip().capitalize() for item in text.split('.')])
    return text_capitalized


# A function which creates one more sentence from last words of each sentence, and adds it to the text
def add_last_words(text):
    last_sentence = ' '.join([item.split()[-1] for item in text.split('.') if len(item) > 0])
    return normalize_case(text) + ' ' + last_sentence.capitalize() + '.'


# A function to replace ' iz ' misspelling in any given text
def replace_iz(text):
    text_replaced = add_last_words(text).replace(' iz ', ' is ')
    return text_replaced


# A function which counts whitespaces in any text
def count_whitespaces(text):
    total_spaces = 0
    for item in text:
        number_of_spaces = len(item) - len(item.strip())
        total_spaces += number_of_spaces
    return total_spaces


# A function to complete homework on the topic 'Strings'
def do_strings_homework(text):
    print(f'Homework completed:\n {replace_iz(text)}')
    print(f'\nNumber of whitespaces is {count_whitespaces(text)}.')


homework = '''homEwork:

  tHis iz your homeWork, copy these Text to variable.



  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''


test = '''In Python, a shallow copy is a “one-level-deep” copy. It constructs a copied object. But the child objects refer to the children of the original object. Thus, it may seem a bit “strange” at first.
A deep copy is the “real copy.” It is an independent copy of the original object. Most of the time, the deep copy is what you want.
Thanks for reading. I hope you learned something new today.
Happy coding!'''

do_strings_homework(homework)
do_strings_homework(test)
