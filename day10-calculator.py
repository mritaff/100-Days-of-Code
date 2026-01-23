def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):

    if n2 != 0:
        return n1 / n2
    
    return "Error"

def calculator(n1, n2, op):
    while True:
        operations={
                    "+": add,
                    "-": subtract,
                    "*": multiply,
                    "/": divide
                        }


        if op in operations:

            if operations[op] == "Error":
                return False

            else:
                calculation_function = operations[op]
                result = calculation_function(n1, n2)
                return result

        else:
            return False


while True:
    n1 = int(input("Type the first number: "))

    print("+, -, *, /\n")

    op = input("Choose an operation to do: ")

    n2 = int(input("Type the second number: "))

    result = calculator(n1, n2, op)
    print(f"{n1} {op} {n2} = {result}")

    if result == False:
        print("Had an error in the calculation. Try again.")

    while True:
        choice = input("Do you want do another operation with result? (y/n)")
        if choice == "n":
            break
        else:
            print("+, -, *, /\n")

            op = input("Choose an operation to do: ")

            n2 = int(input("Type a number: "))

            result2 = calculator(result, n2, op)
            print(f"{result} {op} {n2} = {result2}")
            result = result2 

    while True:
        choice = input("Do you want to left? (y/n)")

        if choice == "n" or choice == "y":
            break
        else:
            continue
    
    if choice == "y":
        break
