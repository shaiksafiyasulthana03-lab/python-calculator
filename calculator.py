calculation_history = []
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    try:                                                                           //catches division by zero errors
        return x / y
    except ZeroDivisionError:
        return "Error: Mathematical anomaly (Division by zero is undefined)"
def save_to_history(log_entry):
    calculation_history.append(log_entry)
def show_history():
    if not calculation_history:
        print("\n--- Session History is Empty ---")
    else:
        print("\n--- Chronological Session Hitory ---")
        for index, entry in enumerate(calculation_history, 1):
            print(f"[{index}] {entry}")

def  main():
    while True:
        print("\n=== COMMAND LINE MATHEMATICAL ENGINE ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Mutiply")
        print("4. DIvide")
        print("5. View History")
        print("6. Exit Application")
        choice = input("\nTerminating mathematical engine.Goodbye!")

        if choice == '6':
            print("Terminating mathematical engine. Goodbye!")
            break
        if choice == '5':
            show_history()
            continue
        if choice in [ '1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first operand: "))
                num2 = float(input("Enter second operand: "))
            except ValueError:
                print("Error: Invalid numeric input. Please enter numbers only.")
                continue

        if choice == '1':
            result = add(num1, num2)
            log = f"{num1} + {num2} = {result}"
        elif choice == '2':
            result = subtract(num1, num2)
            log = f"{num1} - {num2} = {result}"
        elif choice == '3':
            result = multiply(num1, num2)
            log = f"{num1} * {num2} = {result}"
        elif choice == '4':
            result = divide(num1, num2)
            log = f"{num1} / {num2} = {result}"

        print(f"Output: {result}")

        //save to history list only if the mathematical result is valid
        if "Error" not in str(result):
            save_to_history(log)
    else:
        print("Invalid Choice! Please select a valid option from 1 to 6.")
if __name == "__main__":
    main()
