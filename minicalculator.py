
# <=================== This is Mini Calculator ======================>
print("*" * 50)
try: choice = int(input("Press 1 for Addition\nPress 2 for Subtraction\nPress 3 for Multiplication\nPress 4 for Division\nEnter your choice : "))
except ValueError: print("You not enter the number")
else:
    if (choice < 1 or choice > 4):print("Your choice is wrong")
    else:
        try: a,b =  map(int,input("Enter the number seperated with coma: ").split(','))
        except ValueError:  print("You not enter the numbers")
        else:
            if choice == 1:
                print("Sum of {} and {} is".format(a,b), a+b)
            if choice == 2:
                print("Substration between {} and {} is".format(a,b), a-b)
            if choice == 3:
                print("Multiplication of {} and {} is".format(a,b), a*b)
            if choice == 4:
                print("Division of {} and {} is".format(a,b), a/b)
            print("*" * 50)
