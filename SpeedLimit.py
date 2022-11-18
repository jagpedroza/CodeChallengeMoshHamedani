""" 
Write a function for checking the speed of drivers. This function should have one parameter: speed.
If speed is less than 70, it should print “Ok”.
Otherwise, for every 5km above the speed limit (70), 
it should give the driver one demerit point and print the total number of demerit points. 
For example, if the speed is 80, it should print: “Points: 2”.
If the driver gets more than 12 points, the function should print: “License suspended” 
"""


def CheckSpeedLimit(speedlimit):
    if speedlimit<=70:
        print("OK")
    else:
        exceed_speedlimit = speedlimit - 70
        demerit_points = exceed_speedlimit // 5
        if demerit_points <= 12:
            print("Points: " + str(demerit_points))
        else:
            print("License Suspended")

speed_limit = int(input("Write the speed limit to evaluate: "))

CheckSpeedLimit(speed_limit)