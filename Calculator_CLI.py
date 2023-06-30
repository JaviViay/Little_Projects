#import the math library fot the root squart option
import math
#show the options of the calculator
print("1. Addition")
print("2. Substration")
print("3. Multiplication")
print("4. Division")
print("5. Power")
print("6. Square root")
print("7. Module:")
print("8. Quotient:")
#select an option
option = input("Select an option: ")
#define present
total_num = 0.0
next_num_q = "yes"
#addition option
if option == "1":
    num1 = float(input("Insert the first number: "))
    num2 = float(input("Insert the next number: "))
    total_num = num1 + num2
    while next_num_q == "yes":
        next_num_q = input("Any operation more? (yes/no): ")
        if next_num_q == "yes":
            next_num = float(input("Insert the next number: "))
            total_num = total_num + next_num
    print("The result of the addition is: ", total_num)
#substration option
elif option == "2":
    num1 = float(input("Insert the first number: "))
    num2 = float(input("Insert the next number: "))
    total_num = num1 - num2
    while next_num_q == "yes":
        next_num_q = input("Any operation more? (yes/no): ")
        if next_num_q == "yes":
            next_num = float(input("Insert the next number: "))
            total_num = total_num - next_num
    print("The result of the substration is: ", total_num)
#multiplication option
elif option == "3":
    num1 = float(input("Insert the first number: "))
    num2 = float(input("Insert the next number: "))
    total_num = num1 * num2
    while next_num_q == "yes":
        next_num_q = input("Any operation more? (yes/no): ")
        if next_num_q == "yes":
            next_num = float(input("Insert the next number: "))
            total_num = total_num * next_num
    print("The result of the multiplication is: ", total_num)
#division option
elif option == "4":
    num1 = float(input("Insert the first number: "))
    num2 = float(input("Insert the next number: "))
    total_num = num1 / num2
    while next_num_q == "yes":
        next_num_q = input("Any operation more? (yes/no): ")
        if next_num_q == "yes":
            next_num = float(input("Insert the next number: "))
            total_num = total_num / next_num
    print("The result of the division is: ", total_num)
#power option
elif option == "5":
    num1 = float(input("Insert the first number: "))
    num2 = float(input("Insert the next number: "))
    total_num = num1 ** num2
    print("The result of the exponentation is: ", total_num)
#square option
elif option == "6":
    num1 = float(input("Insert a number: "))
    print("The result of the square root is: ", math.sqrt(num1))
#module option
elif option == "7":
    num1 = float(input("Insert the first number: "))
    num2 = float(input("Insert the next number: "))
    total_num = num1 % num2
    print("The result of the remainder of division is: ", total_num)
#quotient option
elif option == "8":
    num1 = float(input("Insert the first number: "))
    num2 = float(input("Insert the next number: "))
    total_num = num1 // num2
    print("The result of the quotient of division is: ", total_num)
#invalid option
else:
    print("Invalid option")