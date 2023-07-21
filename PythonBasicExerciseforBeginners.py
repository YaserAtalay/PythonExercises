# Exercise 1: Calculate the multiplication and sum of two numbers. Given two integer numbers return their product only
# if the product is equal to or lower than 1000, else return their sum.

def calculate(num1, num2):
    if num1 * num2 <= 1000:
        return num1 * num2
    else:
        return num1 + num2


calculate(20, 30)
calculate(40, 30)

# Exercise 2: Print the sum of the current number and the previous number. Write a program to iterate the first 10
# numbers and in each iteration, print the sum of the current and previous number.

previous_num = 0
for i in range(1, 11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
    previous_num = i

# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

str = "pynative"

# 1
for n, i in enumerate(str):
    if n % 2 == 0:
        print(i)


# 2

def DoubleCharacter(string):
    lst = []
    for n, i in enumerate(string):
        if n % 2 == 0:
            lst.append(i)
    return lst


DoubleCharacter(str)


# Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.
# For example:
# remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.
# remove_chars("pynative", 2) so output must be native. Here we need to remove first two characters from a string.
# Note: n must be less than the length of the string.

def remove_chars(string, num):
    if num > len(string):
        print("n must be less than the length of the string.")
    else:
        return string[num:]


remove_chars("pynative", 4)
remove_chars("pynative", 2)
remove_chars("pynative", 15)

# Exercise 5: Check if the first and last number of a list is the same. Write a function to return True if the first
# and last number of a given list is same. If numbers are different then return False.

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]


def first_last_same(lst):
    if lst[0] == lst[-1]:
        return True
    else:
        return False


first_last_same(numbers_x)
first_last_same(numbers_y)

# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5

lst1 = [10, 20, 33, 46, 55]

for i in lst1:
    if i % 5 == 0:
        print(i)

# Exercise 7: Return the count of a given substring from a string
# Write a program to find how many times substring “Emma” appears in the given string.

str_x = "Emma is good developer. Emma is a writer"
print(str_x.count("Emma"))

# Exercise 8: Print the following pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for num in range(10):
    for i in range(num):
        print(num, end=" ")
    print("\n")


# Exercise 9: Check Palindrome Number
# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers


def palindromeNumber(num):
    reverse_num = 0
    ori_num = num
    while num > 0:
        reminder = num % 10
        reverse_num = (reverse_num * 10) + reminder
        num = num // 10
    if ori_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")


palindromeNumber(121)
palindromeNumber(152)

# Exercise 10: Create a new list from a two list using the following condition Create a new list from a two list
# using the following condition. Given a two list of numbers, write a program to create a new list such that the new
# list should contain odd numbers from the first list and even numbers from the second list.

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]


def merge_list(lst1, lst2):
    resultList = []
    for i in lst1:
        if i % 2 != 0:
            resultList.append(i)
    for i in lst2:
        if i % 2 == 0:
            resultList.append(i)
    return resultList


merge_list(list1, list2)
merge_list(list2, list1)

# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

number = 7536
print("Given number", number)
while number > 0:
    # get the last digit
    digit = number % 10
    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end=" ")


# Exercise 12: Calculate income tax for the given income by adhering to the below rules
# Taxable Incode      Rate(in %)
# First $10,000	          0
# Next $10,000	         10
# The remaining	         20
# Expected Output:
# For example, suppose the taxable income is 45000 the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = $6000.


def tax(num):
    tax1 = 0
    if num <= 10000:
        return tax1
    elif (num > 10000) & (num <= 20000):
        return int((num - 10000) * 0.1)
    else:
        return int(((num - 20000) * 0.2) + 1000)


tax(10000)
tax(15000)
tax(45000)


# Exercise 13: Print multiplication table form 1 to 10

for i in range(1, 11):
    for x in range(1, 11):
        print(i * x, end = " ")
    print("\t\t")


# Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)
# * * * * *
# * * * *
# * * *
# * *
# *

for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")

# Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.


def exponent(base, exp):
    return base ** exp


exponent(2,5)