# Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
# Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list
# l1 and even index elements from the list l2.
#
# Given:
# l1 = [3, 6, 9, 12, 15, 18, 21]
# l2 = [4, 8, 12, 16, 20, 24, 28]
#
# Expected Output:
# [6, 12, 18, 4, 12, 20, 28]

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]


def oddEvenList(l1, l2):
    new_lst = []
    for n, i in enumerate(l1):
        if n % 2 != 0:
            new_lst.append(i)
    for n, i in enumerate(l2):
        if n % 2 == 0:
            new_lst.append(i)
    return new_lst


oddEvenList(l1, l2)


# Exercise 2: Remove and add item in a list
# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
#
# Given:
# list1 = [54, 44, 27, 79, 91, 41]

list1 = [54, 44, 27, 79, 91, 41]
print(list1)
num = list1[4]
list1.pop(4)
print(list1)
list1.insert(2, num)
print(list1)
list1.append(num)
print(list1)


# Exercise 3: Slice list into 3 equal chunks and reverse each chunk
#
# Given:
# sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

import numpy as np

b1, b2, b3 = np.array_split(sample_list, 3)

print(b1)
print(list(b1)[::-1])
print(b2)
print(list(b2)[::-1])
print(b3)
print(list(b3)[::-1])



# Exercise 4: Count the occurrence of each element from a list Write a program to iterate a given list and count the
# occurrence of each element and create a dictionary to show the count of each element.
#
# Given:
# sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

#1
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
lst1 = []
for i in sample_list:
    if i not in lst1:
        num = sample_list.count(i)
        print(f"{i} : {num}")
    lst1.append(i)

#2
count_dict = dict()
for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print(count_dict)

print("Printing count of each item  ", count_dict)


# Exercise 5: Create a Python set such that it shows the element from both lists in a pair
#
# Given:
# first_list = [2, 3, 4, 5, 6, 7, 8]
# second_list = [4, 9, 16, 25, 36, 49, 64]
#
# Expected Output:
# Result is  {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

result = zip(first_list, second_list)
result_set = set(result)
print(result_set)


# Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
#
# Given:
# first_set = {23, 42, 65, 57, 78, 83, 29}
# second_set = {57, 83, 29, 67, 73, 43, 48}
#
# Expected Output:
# Intersection is  {57, 83, 29}
# First Set after removing common element  {65, 42, 78, 23}

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

print(list(first_set.intersection(second_set)))
del1 = list(first_set.intersection(second_set))
for i in del1:
    first_set.remove(i)
print(first_set)


# Exercise 7: Checks if one set is a subset or superset of another set. If found, delete all elements from that set
#
# Given:
# first_set = {27, 43, 34}
# second_set = {34, 93, 22, 27, 43, 53, 48}

first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

first_set.issubset(second_set)
second_set.issubset(first_set)

first_set.issuperset(second_set)
second_set.issuperset(first_set)

first_set.clear()


# Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not,
# delete it from the list
#
# Given:
#
# roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
# sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

rn = [i for i in roll_number if i in sample_dict.values()]



# Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates
#
# Given:
# speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}
#
# Expected Outcome:
# [47, 52, 44, 53, 54]

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

#1
setspeed = set(speed.values())
lstspeed = list(setspeed)
print(lstspeed)

#2
speed_list = []
for val in speed.values():
    if val not in speed_list:
        speed_list.append(val)
print("unique list", speed_list)

# Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number
#
# Given:
# sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
#
# Expected Outcome:
# unique items [87, 45, 41, 65, 99]
# tuple (87, 45, 41, 65, 99)
# min: 41
# max: 99

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

sample_set = set(sample_list)
sample_tuple = tuple(sample_set)
print(sample_tuple)
print(min(sample_tuple))
print(max(sample_tuple))


