# Exercise 1: Accept numbers from a user
# Write a program to accept two numbers from the user and calculate multiplication

num1 = input("Enter a number : ")
num2 = input("Enter a number : ")
print(int(num1) * int(num2))

# Exercise 2: Display three string “Name”, “Is”, “James” as “Name**Is**James”. Use the print() function to format the
# given words in the mentioned format. Display the ** separator between each string. Expected Output: For example:
# print('Name', 'Is', 'James') will display Name**Is**James

print("Name", "Is", "James", sep="**")

# Exercise 3: Convert Decimal number to octal using print() output formatting
# Given:
# num = 8
# Expected Output:
# The octal number of decimal number 8 is 10

num = 8
print('%o' % num)

# Exercise 4: Display float number with 2 decimal places using print()
# Given:
# num = 458.541315
# Expected Output:
# 458.54

num = 458.541315
print("%.2f" % num)

# Exercise 5: Accept a list of 5 float numbers as an input from the user
# Refer:
# Take list as a input in Python.
# Python list
# Expected Output:
# [78.6, 78.6, 85.3, 1.2, 3.5]

numbers = []
for i in range(1, 6):
    numbers.append(float(input(f" {i} Enter the number : ")))
print(numbers)

# Exercise 6: Write all content of a given file into a new file by skipping line number 5

with open("test.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()

with open("new_file.txt", "w") as fp:
    count = 0
    # iterate each lines from a test.txt
    for line in lines:
        # skip 5th lines
        if count == 4:
            count += 1
            continue
        else:
            # write current line
            fp.write(line)
        # in each iteration reduce the count
        count += 1


# Exercise 7: Accept any three string from one input() call
# Write a program to take three names as input from a user in the single input() function call.

#1
strings = input("Enter three string ")
strings = strings.split()
print(strings)
for i, s in enumerate(strings, 1):
    print(f"{i}. İsim : {s}")

#2
str1, str2, str3 = input("Enter three string ").split()
print('Name1:', str1)
print('Name2:', str2)
print('Name3:', str3)


# Exercise 8: Format variables using a string.format() method.
# Write a program to use string.format() method to format the following three variables as per the expected output
# Given:
# totalMoney = 1000
# quantity = 3
# price = 450
# Expected Output:
# I have 1000 dollars so I can buy 3 football for 450.00 dollars.

totalMoney = 1000
quantity = 3
price = 450
print("I have {1} dollars so I can buy {0} football for {2} dollars.".format(quantity, totalMoney, price))

# Exercise 9: Check file is empty or not
# Write a program to check if the given file is empty or not

import os

size = os.stat("test.txt").st_size
if size == 0:
    print('file is empty')


# Exercise 10: Read line number 4 from the following file
# Create a test.txt file and add the below content to it.
# test.txt file:
# line1
# line2
# line3
# line4
# line5
# line6
# line7

with open("test.txt2", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()
    # get line number 3
    print(lines[2])

