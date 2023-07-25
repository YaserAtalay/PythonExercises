# Exercise 1A: Create a string made of the first, middle and last character
# Write a program to create a new string made of an input string’s first, middle, and last character.
# Given:
# str1 = "James"
# Expected Output:
# Jms

str1 = "James"
res = str1[0]
mi = int(len(str1)/2)
res = res + str1[mi]
l = len(str1)
res = res + str1[l-1]
print(res)



# Exercise 1B: Create a string made of the middle three characters
# Write a program to create a new string made of the middle three characters of an input string.
# Given:
# Case 1
# str1 = "JhonDipPeta"
# Output
# Dip
# Case 2
# str2 = "JaSonAy"
# Output
# Son

str1 = "JhonDipPeta"
str2 = "JaSonAy"


def get_middle_three_chars(string):
    mi = len(string) // 2
    print(string[mi-1 : mi+2])


get_middle_three_chars(str1)
get_middle_three_chars(str2)

# Exercise 2: Append new string in the middle of a given string
# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
# Given:
# s1 = "Ault"
# s2 = "Kelly"
# Expected Output:
# AuKellylt

s1 = "Ault"
s2 = "Kelly"


def append_middle(s1, s2):
    mi = int(len(s1) / 2)
    x = s1[:mi:]
    x = x + s2
    x = x + s1[mi:]
    print("After appending new string in middle:", x)


append_middle("Ault", "Kelly")


# Exercise 3: Create a new string made of the first, middle, and last characters of each input string
# Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle,
# and last characters.
# Given:
# s1 = "America"
# s2 = "Japan"
# Expected Output:
# AJrpan


def mix_string(s1, s2):
    first_char = s1[0] + s2[0]
    middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2) / 2) + 1]
    last_char = s1[len(s1) - 1] + s2[len(s2) - 1]
    res = first_char + middle_char + last_char
    print("Mix String is ", res)


s1 = "America"
s2 = "Japan"
mix_string(s1, s2)



# Exercise 4: Arrange string characters such that lowercase letters should come first
# Given string contains a combination of the lower and upper case letters.
# Write a program to arrange the characters of a string so that all lowercase letters should come first.
# Given:
# str1 = PyNaTive
# Expected Output:
# yaivePNT

str1 = "PYnAtivE"
lower = []
upper = []
for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)


sorted_str = ''.join(lower + upper)
print('Result:', sorted_str)


# Exercise 5: Count all letters, digits, and special symbols from a given string
# Given:
# str1 = "P@#yn26at^&i5ve"
# Expected Outcome:
# Total counts of chars, digits, and symbols
# Chars = 8
# Digits = 3
# Symbol = 4


def find_digits_chars_symbols(sample_str):
    char_count = 0
    digit_count = 0
    symbol_count = 0
    for char in sample_str:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        else:
            symbol_count += 1

    print("Chars =", char_count, "Digits =", digit_count, "Symbol =", symbol_count)


sample_str = "P@yn2at&#i5ve"
print("total counts of chars, Digits, and symbols \n")
find_digits_chars_symbols(sample_str)

# Exercise 6: Create a mixed String using the following rules
# Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1,
# then the last char of s2, Next, the second char of s1 and second last char of s2,
# and so on.Any leftover chars go at the end of the result.
# Given:
# s1 = "Abc"
# s2 = "Xyz"
# Expected Output:
# AzbycX

s1 = "Abc"
s2 = "Xyz"
s1_length = len(s1)
s2_length = len(s2)
length = s1_length if s1_length > s2_length else s2_length
result = ""
s2 = s2[::-1]
for i in range(length):
    if i < s1_length:
        result = result + s1[i]
    if i < s2_length:
        result = result + s2[i]

print(result)

# Exercise 7: String characters balance Test
# Write a program to check if two strings are balanced.
# For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2.
# The character’s position doesn’t matter.
# Given:
# Case 1:
# s1 = "Yn"
# s2 = "PYnative"
# Expected Output:
# True
# Case 2:
# s1 = "Ynf"
# s2 = "PYnative"
# Expected Output:
# False


def string_balance_test(s1, s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag


s1 = "Yn"
s2 = "PYnative"
flag = string_balance_test(s1, s2)
print("s1 and s2 are balanced:", flag)

s1 = "Ynf"
s2 = "PYnative"
flag = string_balance_test(s1, s2)
print("s1 and s2 are balanced:", flag)


# Exercise 8: Find all occurrences of a substring in a given string by ignoring the case
# Write a program to find all occurrences of “USA” in a given string ignoring the case.
# Given:
# str1 = "Welcome to USA. usa awesome, isn't it?"
# Expected Outcome:
# The USA count is: 2

str1 = "Welcome to USA. usa awesome, isn't it?"
sub_string = "usa"
temp_str = str1.lower()
count = temp_str.count(sub_string)
print("The USA count is:", count)



# Exercise 9: Calculate the sum and average of the digits present in a string
# Given a string s1, write a program to return the sum and average of the digits that appear in the string,
# ignoring all other characters.
# Given:
# str1 = "PYnative29@#8496"
# Expected Outcome:
# Sum is: 38 Average is  6.333333333333333

input_str = "PYnative29@#8496"
total = 0
cnt = 0
for char in input_str:
    if char.isdigit():
        total += int(char)
        cnt += 1

# average = sum / count of digits
avg = total / cnt
print("Sum is:", total, "Average is ", avg)



# Exercise 10: Write a program to count occurrences of all characters within a string
# Given:
# str1 = "Apple"
# Expected Outcome:
# {'A': 1, 'p': 2, 'l': 1, 'e': 1}

str1 = "Apple"
char_dict = dict()
for char in str1:
    count = str1.count(char)
    char_dict[char] = count
print('Result:', char_dict)


# Exercise 11: Reverse a given string
# Given:
# str1 = "PYnative"
# Expected Output:
# evitanYP

str1 = "PYnative"
str1[::-1]

# Exercise 12: Find the last position of a given substring
# Write a program to find the last position of a substring “Emma” in a given string.
# Given:
# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# Expected Output:
# Last occurrence of Emma starts at index 43

str1 = "Emma is a data scientist who knows Python. Emma works at google."
print("Original String is:", str1)

index = str1.rfind("Emma")
print("Last occurrence of Emma starts at index:", index)


# Exercise 13: Split a string on hyphens
# Write a program to split a given string on hyphens and display each substring.
# Given:
# str1 = Emma-is-a-data-scientist
# Expected Output:
# Displaying each substring
# Emma
# is
# a
# data
# scientist

str1 = "Emma-is-a-data-scientist"
sub_string = str1.split("-")
for i in sub_string:
    print(i)

# Exercise 14: Remove empty strings from a list of strings
# Given:
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# Expected Output:
# Original list of sting
# ['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']
# After removing empty strings
# ['Emma', 'Jon', 'Kelly', 'Eric']

str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
res_list = []
for s in str_list:
    if s:
        res_list.append(s)
print(res_list)


# Exercise 15: Remove special symbols / punctuation from a string
# Given:
# str1 = "/*Jon is @developer & musician"
# Expected Output:
# "Jon is developer musician"

import string

str1 = "/*Jon is @developer & musician"
print("Original string is ", str1)

new_str = str1.translate(str.maketrans('', '', string.punctuation))

print("New string is ", new_str)


# Exercise 16: Removal all characters from a string except integers
# Given:
# str1 = 'I am 25 years and 10 months old'
# Expected Output:
# 2510

str1 = 'I am 25 years and 10 months old'
print("Original string is", str1)
res = "".join([item for item in str1 if item.isdigit()])
print(res)



# Exercise 17: Find words with both alphabets and numbers
# Write a program to find words with both alphabets and numbers from an input string.
# Given:
# str1 = "Emma25 is Data scientist50 and AI Expert"
# Expected Output:
# Emma25
# scientist50

str1 = "Emma25 is Data scientist50 and AI Expert"
print("The original string is : " + str1)
res = []
temp = str1.split()

for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)

print("Displaying words with alphabets and numbers")
for i in res:
    print(i)


# Exercise 18: Replace each special symbol with # in the following string
# Given:
# str1 = '/*Jon is @developer & musician!!'
# Expected Output:
# ##Jon is #developer # musician##

str1 = '/*Jon is @developer & musician!!'
print("The original string is : ", str1)
replace_char = '#'
for char in string.punctuation:
    str1 = str1.replace(char, replace_char)
print("The strings after replacement : ", str1)