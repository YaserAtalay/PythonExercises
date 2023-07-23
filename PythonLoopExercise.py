# Exercise 1: Print First 10 natural numbers using while loop

i = 1
while i <= 10:
    print(i)
    i += 1

# Exercise 2: Print the following pattern
# Write a program to print the following number pattern using a loop.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print("")



# Exercise 3: Calculate the sum of all numbers from 1 to a given number
# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)
# Expected Output:
# Enter number 10
# Sum is:  55

# 1
num = int(input("Enter a number"))
result = 0
for i in range(1, num+1):
    result += i
print(result)

# 2
num = int(input("Enter a number"))
sum(range(1, num+1))

# Exercise 4: Write a program to print multiplication table of a given number
# For example, num = 2 so the output should be
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20

num = int(input("Enter a number"))
for i in range(1, 11):
    print(i * num)


# Exercise 5: Display numbers from a list using loop
# Write a program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop
# Given:
# numbers = [12, 75, 150, 180, 145, 525, 50]
# Expected output:
# 75
# 150
# 145

numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i > 500:
        break
    elif i > 150:
        pass
    elif i % 5 == 0:
        print(i)


# Exercise 6: Count the total number of digits in a number
# Write a program to count the total number of digits in a number using a while loop
# For example, the number is 75869, so the output should be 5

num = 75869
count = 0
while num != 0:
    num = num // 10
    count = count + 1
print("Total digits are:", count)


# Exercise 7: Print the following pattern
# Write a program to use for loop to print the following reverse number pattern
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

for i in range(5, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print("")


# Exercise 8: Print list in reverse order using a loop
# Given:
# list1 = [10, 20, 30, 40, 50]
# Expected output:
# 50
# 40
# 30
# 20
# 10

# 1
list1 = [10, 20, 30, 40, 50]
list1.reverse()
print(list1)

# 2
list1 = [10, 20, 30, 40, 50]
for i in range(len(list1)-1, 0, -1):
    print(list1[i])


# Exercise 9: Display numbers from -10 to -1 using for loop
# Expected output:

for i in range(-10, 0, 1):
    print(i)


# Exercise 10: Use else block to display a message “Done” after successful execution of for loop
# For example, the following loop will execute without any error.
# Given:
# for i in range(5):
#     print(i)
# Expected output:
# 0
# 1
# 2
# 3
# 4
# Done!

for i in range(5):
    print(i)
else:
    print("Done!")


# Exercise 11: Write a program to display all prime numbers within a range
# Note: A Prime Number is a number that cannot be made by multiplying other whole numbers.
# A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers
# Examples:
# 6 is not a prime mumber because it can be made by 2×3 = 6
# 37 is a prime number because no other whole numbers multiply together to make it.
# Given:
# # range
# start = 25
# end = 50
# Expected output:
# Prime numbers between 25 and 50 are:
# 29
# 31
# 37
# 41
# 43
# 47

start = 25
end = 50

for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)


# Exercise 12: Display Fibonacci series up to 10 terms
# The Fibonacci Sequence is a series of numbers. The next number is found by adding up the two numbers before it.
# The first two numbers are 0 and 1.
# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series above is 13+21 = 34.
# Expected output:
# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34

num1, num2 = 0, 1
print("Fibonacci sequence:")
for i in range(10):
    print(num1, end="  ")
    res = num1 + num2
    num1 = num2
    num2 = res


# Exercise 13: Find the factorial of a given number
# Write a program to use the loop to find the factorial of a given number.
# The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.
# For example: calculate the factorial of 5
# 5! = 5 × 4 × 3 × 2 × 1 = 120
# Expected output:
# 120

num = 5
result = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        result = result * i
    print("The factorial of", num, "is", result)


# Exercise 14: Reverse a given integer number
# Given:
# 76542
# Expected output:
# 24567

num = 76542
reverse_number = 0
print("Given Number ", num)
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Revere Number ", reverse_number)


# Exercise 15: Use a loop to display elements from a given list present at odd index positions
# Given:
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Note: list index always starts at 0
# Expected output:
# 20 40 60 80 100

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(0, len(my_list)):
    if i % 2 != 0:
        print(my_list[i])


# Exercise 16: Calculate the cube of all numbers from 1 to a given number
# Write a program to rint the cube of all numbers from 1 to a given number

input_number = 6
for i in range(1, input_number+1):
    print(i**3)



