"""
import module random:
 to generate number of dictionaries in list (2-10)
 to generate number of key: value pairs in each dictionary (2-10)
 to generate numeric values (0-100)
"""
import random
# create empty list to be appended with dictionaries
list_of_dictionaries = []
# create empty dictionary to union all key: value pairs from dictionaries in the list
union_dict = {}
# create empty list to keep all keys from all dictionaries
keys_all = []
# create empty list to keep unique keys
keys_unique = []
# create empty list to keep shared keys
keys_shared = []
# create string with all letters of alphabet for keys of dictionaries
letters_keys = 'qwertyuiopasdfghjklzxcvbnm'

# generate random number of dictionaries to make a list
for i in range(random.randint(2, 10)):
    # add to dictionary name a number to differentiate dictionaries
    dictionary_name = 'dictionary' + str(i)
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

# we collect all keys from all dictionaries in one list
for dictionary in list_of_dictionaries:
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
for dictionary in list_of_dictionaries:
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
    for i in range(len(list_of_dictionaries)):
        # if shared key is in keys of a dictionary
        # and its value is greater than maximum value of this key
        # we assign its value to the max_value
        # and write the number of the dictionary to the variable index_of_max
        # we add 1 to this number, because indexing starts with 0
        if key in list_of_dictionaries[i] and max_value < list_of_dictionaries[i][key]:
            max_value = list_of_dictionaries[i][key]
            index_of_max = i + 1
    # we add a key: value pair to the common dictionary
    # key is shared key concatenated with the number of dictionary
    # where there is maximum value of this shared key
    # value is max_value
    union_dict[key + '_' + str(index_of_max)] = max_value

