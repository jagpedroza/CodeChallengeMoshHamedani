""" 
Write a function called showNumbers that takes a parameter called limit. 
It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. 
For example, if the limit is 3, it should print:
0 EVEN
1 ODD
2 EVEN
3 ODD 
"""

def showNumbers(limit):
    show_numbers_range = range(0, limit +1)
    for number in show_numbers_range:
        if number % 2== 0:
            print(str(number) + " EVEN")
        else:
            print(str(number) + " ODD")

input_limit = int(input("please give a limit to calculate it "))

showNumbers(input_limit)