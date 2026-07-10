def divide_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both a and b must be numbers.")
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        return None
    except TypeError:
        print("Error: Invalid operand types for division.")
        return None
    else:
        print("Division completed successfully.")
        return result
    finally:
        print("Cleanup completed.")

def register_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer.")
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Registered user with age {age}")

if __name__ == "__main__":
    divide_numbers(10, 2)
    try:
        register_age(25)
    except ValueError as e:
        print(f"Error: {e}")
