# write a function that determines if a number is a Harshad number
# and then uses this function to write another function that determines the ith Harshad number.
#
# A Harshad number is an integer that is divisible by the sum of its digits. For example, 81 is a Harshad number,
# because 8+1 = 9 and 81/9 = 9. The first Harshad number is 1.
#
# Assignment 2.1
#
# Write a function isHarshad that takes as input an integer and that has as output True,
# if the integer is a Harshad number, and False if it is not.
# For example, isHarshad(81) should have ouput True.
#
# Hint: Use str to convert the input to a string, see Chapter 8 of the Think Python book.

def isHarshad(n):
    n_str = str(n)
    sum_of_digits = 0
    for i in n_str:
        sum_of_digits = sum_of_digits + int(i)
    if n == 0:
        return False
    elif n % sum_of_digits == 0:
        return True
    else:
        return False


isHarshad(81)


# Assignment 2.2
#
# Write a function ithHarshad that takes as input an integer i and prints out a list of the ith Harshad numbers on screen.
# Make that function has no output, i.e., write a void function.
#
# For example, ithHarshad(25) should print:
#
# "The first 25 Harshad numbers are: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 18, 20, 21, 24, 27, 30, 36, 40,
# 42, 45, 48, 50, 54, 60]".
#
# Hint: use the isHarshad function above.

def ithharshad(arh):
    i = 0       # counter checking of the number is harsh
    j = 0       # counting the number of harsh numbers
    hrash = []
    while True:
        if isHarshad(i):
            hrash.append(i)
            j += 1
            if j == arh:
                break
        i += 1

    print('The first ', arh, 'harshhard numbers are', hrash)
ithharshad(25)




