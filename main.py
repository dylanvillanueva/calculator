import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def format_number(answer):
    if answer.is_integer():
        return int(answer)
    else:
        return answer


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(art.logo)

    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{format_number(num1)} {operation_symbol} {format_number(num2)} = {format_number(answer)}")

        continue_operations = input(f"Type 'y' to continue calculating with {format_number(answer)}, "
                                    f"or type 'n' to start a new calculation: ").lower()

        if continue_operations == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()