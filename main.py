from art import logo

print(logo)

calculation_end = False
first_num = float(input("What is the first number?: "))
operation = input("Pick an operation ( + | - | * | / ): ")
next_num = float(input("what is the next number?: "))


def operations(num1, num2, operator):
    output = 0
    if operator == "+":
        output = num1 + num2
    elif operator == "-":
        output = num1 - num2
    elif operator == "*":
        output = num1 * num2
    elif operator == "/":
        output = round(num1 / num2, 2)
    else:
        print("Invalid Operation. Please from the given options")
    return output


answer = operations(first_num, next_num, operation)
print(f"{first_num} {operation} {next_num} = {answer}")

while calculation_end != True:
    move_ahead = input(
        f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: "
    )
    if move_ahead == "y":
        operation = input("Pick an operation ( + | - | * | / ): ")
        next_num = float(input("what is the next number?: "))
        next_answer = operations(answer, next_num, operation)
        print(f"{answer} {operation} {next_num} = {next_answer}")
    else:
        calculation_end = True
