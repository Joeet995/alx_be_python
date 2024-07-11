def safe_divide(numerator: float, denominator: float):
    try:
        result = numerator / denominator
        print(f"The result of the division is {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")