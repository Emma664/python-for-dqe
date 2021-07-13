# We assign text of homework to the variable homework
homework = '''homEwork:

  tHis iz your homeWork, copy these Text to variable.

 

  You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.

 

  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.

 

  last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.'''

# We split string into list of sentences, using dot as a separator
homework_split = homework.split('.')
# We remove last item of a list, which is an empty list
homework_split.pop(-1)
# We remove whitespaces from the items of the list and then capitalize it
homework_capitalized = [item.strip().capitalize() for item in homework_split]
# We collect last element of each item of the list in the new list
last_sentence = [item.split()[-1] for item in homework_capitalized]
# We join the elements of the list of collected items into the string
last_sentence_joined = ' '.join(last_sentence)
# We capitalize the string and add dot to get a sentence
last_sentence_capitalized = last_sentence_joined.capitalize()
last_sentence_with_dot = last_sentence_capitalized + '.'
# We append our sentence of last words to the list of homework.
homework_capitalized.append(last_sentence_with_dot)
# We join back the list of homework to the string
homework_joined = '. '.join(homework_capitalized)
# We replace iz with is
homework_replaced_iz = homework_joined.replace(' iz ', ' is ')
# We count whitespaces:
# For each item I count length of item and then subtract length of item without whitespaces from both sides
total_spaces = 0
for item in homework:
    number_of_spaces = len(item) - len(item.strip())
    total_spaces += number_of_spaces

print(homework_replaced_iz)
print(f'Number of whitespaces is {total_spaces}.')
