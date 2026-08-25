def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

try:
    print("===== FUNCTION CALCULATOR =====")
    print("1 = ADD")
    print("2 = SUBTRACT")
    print("3 = MULTIPLY")
    print("4 = DIVIDE")

    o = int(input("Choose an operation: "))

    num1 = int(input("Choose your first number: "))
    num2 = int(input("Choose your second number: "))

    if o == 1:
        print("Sum of both these numbers: ", add(num1, num2))

    elif o == 2:
        print("Difference of both these numbers: ", subtract(num1, num2))

    elif o == 3:
        print("Product of both these numbers: ", multiply(num1, num2))

    elif o == 4:
        print("Quotient of both these numbers: ", divide(num1, num2))

    else:
        print("Please enter 1, 2, 3, 4 not any other numbers.")

except ValueError:
    print("Invalid input!")

except ZeroDivisionError:
    print("Division by zero is error.")

except:
    print("Wrong input.")

finally:
    print("This will work no matter what!")