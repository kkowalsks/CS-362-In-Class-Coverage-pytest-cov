#Accept user input and make sure that it's a valid integer, repeating the loop if invalid
#while True:
#    try:
#        userinput = int(input("Please enter an integer: "))
#    except ValueError:
#        print("Invalid input, try again")
#        continue
#    else:
#        break


def leapCheck(x):
    #Check if the integer is divisible by 4, output that it is not a leap year if not
    if x % 4 != 0:
        userinput = str(x)
        print(userinput + " is not a leap year")
        return False
    else:
        #Check if integer is also divisible by 100, output that it is a leap year if it is not
        if x % 100 != 0:
            userinput = str(x)
            print(userinput + " is a leap year")
            return True
        else:
            #Check if integer is also divisble by 400, output that it is a leap year if so
            # and output that it is not a leap year if it is indivisible by 400
            if x % 400 != 0:
                    userinput = str(x)
                    print(userinput + " is not a leap year")
                    return False
            else:
                userinput = str(x)
                print(userinput + " is a leap year")
                return True