import art

print(art.logo)


def add(n1, n2):
    return n1 + n2


def subs(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operation_dictionary = {
    "+": add,
    "-": subs,
    "*": multiply,
    "/": divide,
}

number_1 = float(input("What's the first number?: "))

to_continue = True
while to_continue:
    for symbol in operation_dictionary:
        print(symbol)

    operation = input("Pick an operation from above: ")

    number_2 = float(input("What's the next number?: "))

    calculation_function = operation_dictionary[operation]

    answer = calculation_function(number_1, number_2)

    print(f"{number_1} {operation} {number_2} = {answer}")

    ask = input(f"Type 'Y' to continue with {answer}\ntype 'N' to start new\ntype any other key to exit\n").lower()

    if ask == "y":
        number_1 = answer
    elif ask == "n":
        number_1 = float(input("What's the first number?: "))
    else:
        to_continue = False

# def calculator (x, y, operation):
#     if operation == "+":
#       return x + y
#     elif operation == "-":
#       return x - y
#     elif operation == "*":
#       return x * y
#     elif operation == "/":
#       return x/y


# number_1 = int(input("What's the first number?: "))
# to_continue = True
# while to_continue:
#   print("+\n-\n*\n/")
#   operation = input("Pick an operation: ")
#   number_2 = int(input("What's the next number?: "))
#   result = calculator(number_1, number_2, operation)
#   print(f"{number_1} "+ operation + f" {number_2} = {result} ")
#   ask_agian = input(f"type 'Y' to continue with {result}, otherwise type 'N': ").lower()

#   if ask_agian == "y":
#     number_1 = result
#   else:
#     to_continue = False
