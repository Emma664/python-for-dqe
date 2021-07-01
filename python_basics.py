#  import module for working with random numbers
import random
#  create empty list to fill it with random numbers
random_list = []
"""
we need 100 numbers. in range(100) means from i = 0 to i = 99 
in each iteration we add to list one random number in range from 0 to 1000
"""
for i in range(100):
    random_list.append(random.randrange(1001))
# we get into variable the length of the list to improve readability
n = len(random_list)
"""
we use bubble-sort algorithm:
we switch adjacent elements, move the min element to the left
in the inner cycle we go through all the elements of the list: we compare couples
in the outer cycle we repeat this comparison for length of list minus 1 times, 
because the last element will be in place after the previous comparison
"""
for i in range(n - 1):
    for j in range(n - i - 1):
        if random_list[j] > random_list[j + 1]:
            random_list[j], random_list[j + 1] = random_list[j + 1], random_list[j]
# create variables to keep sums of numbers and count numbers
even_numbers_sum = 0
even_numbers_counter = 0
odd_numbers_sum = 0
odd_numbers_counter = 0
"""
for each element in the list we calculate the remainder of the dividing this number by 2,
if it is 0 - the number is even, add this number to sum variable, add 1 to counter variable
it the remainder is 1 - the number is odd
"""
for i in random_list:
    if i % 2 == 0:
        even_numbers_sum += i
        even_numbers_counter += 1
    if i % 2 == 1:
        odd_numbers_sum += i
        odd_numbers_counter += 1

print('Average for even numbers is', even_numbers_sum / even_numbers_counter)
print('Average for odd numbers is', odd_numbers_sum/odd_numbers_counter)
