def greet(name, greeting="hello"):
    if not isinstance(name, str) or not isinstance(greeting, str):
        raise TypeError("name and greeting must be strings")
    return f"{greeting.capitalize()}, {name}!"

def calculate_total(*args):
    for num in args:
        if not isinstance(num, (int, float)):
            raise TypeError("All arguments must be numbers")
    total = 0
    for num in args:
        total += num
    return total

def print_user_info(**kwargs):
    if 'name' in kwargs and not isinstance(kwargs['name'], str):
        raise TypeError("name must be a string")
    if 'age' in kwargs and not isinstance(kwargs['age'], int):
        raise TypeError("age must be an integer")
    if 'active' in kwargs and not isinstance(kwargs['active'], bool):
        raise TypeError("active must be a boolean")
        
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")

if __name__ == "__main__":
    print(greet("Alice"))
    print(f"Total: {calculate_total(10, 20, 30)}")
    print_user_info(name="Alice", role="Admin", hobby="Coding")
