import random


def generate_dictionaries() -> list:
    """This function creates a list of random number of dicts and
        generates random number of key: value pairs in each dictionary

    Returns
    -------
    list
        a list of dictionaries
    """

    list_of_dictionaries = []
    letters_keys = 'qwertyuiopasdfghjklzxcvbnm'
    for i in range(random.randint(2, 10)):
        dictionary_name = {}
        for j in range(random.randint(2, 10)):
            dictionary_name[random.choice(letters_keys)] = random.randint(0, 100)
        list_of_dictionaries.append(dictionary_name)
    return list_of_dictionaries


def create_common_dictionary(arbitrary_list: list) -> dict:
    """Creates common dictionary from a list of random number of dicts

    Parameters
    ----------
    arbitrary_list : list
        A list of random dicts

    Returns
    -------
    dict
        Dictionary to union all key: value pairs from dictionaries in the list
    """

    union_dict = {}
    keys_all = []
    keys_unique = []
    keys_shared = []

    for dictionary in arbitrary_list:
        keys_all.extend(list(dictionary.keys()))

    for item in keys_all:
        if keys_all.count(item) == 1:
            keys_unique.append(item)
        elif item not in keys_shared:
            keys_shared.append(item)

    for dictionary in arbitrary_list:
        for key in dictionary:
            if key in keys_unique:
                union_dict[key] = dictionary[key]

    for key in keys_shared:
        max_value = 0
        index_of_max = 0
        for i in range(len(arbitrary_list)):
            if key in arbitrary_list[i] and max_value < arbitrary_list[i][key]:
                max_value = arbitrary_list[i][key]
                index_of_max = i + 1
        union_dict[key + '_' + str(index_of_max)] = max_value
    return union_dict


print(create_common_dictionary(generate_dictionaries()))


def normalize_case(text: str) -> str:
    """Normalizes any text from letter cases point of view

       Parameters
       ----------
       text : str
           Any text

       Returns
       -------
       str
           Text with all letters in lower case except the first letter
           of the first word in each sentence.
       """

    text_capitalized = '. '.join([item.strip().capitalize() for item in text.split('.')])
    return text_capitalized


def add_last_words(text: str) -> str:
    """Creates one more sentence from last words of each sentence,
     and adds it to the text

       Parameters
       ----------
       text : str
           Any text

       Returns
       -------
       str
           Text with a sentence added.
       """

    last_sentence = ' '.join([item.split()[-1] for item in text.split('.') if len(item) > 0])
    return normalize_case(text) + ' ' + last_sentence.capitalize() + '.'


def replace_iz(text: str) -> str:
    """Replaces ' iz ' misspelling in any given text.
    iz is surrounded by whitespaces to avoid replacing it inside the words
    e.g. capitalize - here it is spelled correctly and should not be replaced

       Parameters
       ----------
       text : str
           Any text

       Returns
       -------
       str
           Text with 'iz' replaced.
       """

    text_replaced = add_last_words(text).replace(' iz ', ' is ')
    return text_replaced


def count_whitespaces(text: str) -> int:
    """Counts whitespaces in any text

       Parameters
       ----------
       text : str
           Any text

       Returns
       -------
       int
           Number of whitespaces.
       """

    total_spaces = 0
    for item in text:
        number_of_spaces = len(item) - len(item.strip())
        total_spaces += number_of_spaces
    return total_spaces


def do_strings_homework(text: str) -> None:
    """Prints the results of completed homework
    on the topic 'Strings'

       Parameters
       ----------
       text : str
           Any text
       """

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
