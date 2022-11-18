""" 
Write a function called show_stars(rows). If rows is 5, it should print the following:
*
**
***
****
***** 
"""

def estrellas(num):
    #num = int(input("Provide the number: "))
    max_val = num+1
    printed_val = max_val
    for star in range(num+1):
        print("*" * star)
    
estrellas(10)
