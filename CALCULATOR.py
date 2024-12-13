def calculator():
    print("Welcome to the Python Calculator!")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Soustraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    while True:
        operation = input("Enter the number of the operation you want to perform (1/2/3/4): ")

        if operation in ['1', '2', '3', '4']:
            try:

                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if operation == '1':
                    print(f"The result of {num1} + {num2} is {num1 + num2}")
                elif operation == '2':
                    print(f"The result of {num1} - {num2} is {num1 - num2}")
                elif operation == '3':
                    print(f"The result of {num1} * {num2} is {num1 * num2}")
                elif operation == '4':
                    if num2 != 0:
                        print(f"The result of {num1} / {num2} is {num1 / num2}")
                    else:
                        print("Error: Division by zero is not allowed.")
            except ValueError:
                print("Invalid input! Please enter numeric values.")

        else:
            print("Invalid operation! Please select a valid option.")


        another_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if another_calculation != 'yes':
            print("Goodbye!")
            break


calculator()
