while True:
    try:
        num1 = float(input("Enter first number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /,//,**,%): ")

    try:
        if operation == "+":
            print(f"{num1} + {num2} = {num1 + num2}")
        elif operation == "-":
            print(f"{num1} - {num2} = {num1 - num2}")
        elif operation == "*":
            print(f"{num1} * {num2} = {num1 * num2}")
        elif operation == "/":
            print(f"{num1} / {num2} = {num1 / num2}")
        elif operation == "//":
            print(f"{num1} // {num2} = {num1 // num2}")
        elif operation == "**":
            print(f"{num1} ** {num2} = {num1 ** num2}")
        elif operation == "%":
            print(f"{num1} % {num2} = {num1 % num2}")
        else:
            print("Invalid operation")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    again = input("Do you want to perform another calculation? (yes/no): ")
    if again.lower() == "yes":
        break

