""" 
Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.
"""

def print_numbers(limit):
    range_limit = range(0, limit)
    for number in range_limit:
        if number % number == 0:
            print(number)

inp_limit = int(input("give the limit number to get the prime numbers: "))
print_numbers(inp_limit)