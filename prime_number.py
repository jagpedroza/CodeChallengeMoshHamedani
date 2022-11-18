""" 
Write a function that prints all the prime numbers between 0 and limit where limit is a parameter. 
"""


#work in progres!!

def prime_number(num):
    primes = [1]
    for numbers in range(2,num+1):
        for prime in primes:
            numbers % prime == 0
            break
        else:
            primes.append(numbers)
    print(primes)

prime_number(10)