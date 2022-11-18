#This function will evaluate which of the numbers are grater

def MaxNumber(num1, num2):
#    if num1.isnumeric() and num2.isnumeric():
        if num1 == num2:
            print("both numbers are equal")
        elif num1 > num2:
            print("The first number:"+ str(num1)+ " greater than the second one: " + str(num2))
        elif num2 > num1:
            print("The second number:"+ str(num2)+ " greater than the first one: " + str(num1))
        else:
            print("verify the inputs")


MaxNumber(53, 53)