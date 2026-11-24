number_1 = int(input("Enter First Numbers"))
number_2 = int(input("Enter Second Number"))

ops = ["addition","Subtraction","Multiplication","division"] 
print(f" Operations Available -- {ops} ")
operation = str(input("Operation to perform : "))

if operation.lower() == "addition":

    result =  number_1 + number_2
    print(result)
elif operation.lower() == "subraction":
    result = number_1 - number_2
    print(result)
elif operation.lower() == "multiplication":
    result = number_1 * number_2
    print(result)
else:
    if operation.lower() == "division" and number_2 != 0:
        result = number_1 / number_2
        print(result)
    else:
        raise ZeroDivisionError 