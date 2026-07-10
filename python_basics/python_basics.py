import functions
import data_structures
import comprehensions
import error_handling
import iterators_generators


def check_status(age, active):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer.")
    elif age < 18:
        print("User is a minor.")
    else:
        print("User is an adult.")


def count_down(start):
    for i in range(start, 0, -1):
        print(f"Count: {i}")
    print("Countdown complete.")


def get_int(prompt, default):
    try:
        return int(input(prompt))
    except ValueError:
        return default


def get_list(prompt, cast_type, default):
    val = input(f"{prompt}: > ")
    if not val:
        return default
    try:
        return [cast_type(x) for x in val.split()]
    except ValueError:
        return default


if __name__ == "__main__":
    print("Python Basics")
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))

    check_status(user_age, True)
    count_down(get_int("\nEnter a number for the countdown: ", 3))

    print("\n Functions")
    print(functions.greet(user_name, "Hello"))

    nums = get_list("\nEnter numbers to calculate total", int, [10, 20, 30])
    print(f"Total: {functions.calculate_total(*nums)}")

    functions.print_user_info(name=user_name, age=user_age)

    print("\n Data Structures ")
    my_tasks = get_list("Enter tasks", str, None)
    print(f"List: {data_structures.list_demo(my_tasks)}")

    try:
        x_coord = float(input("\nEnter X coordinate: "))
        y_coord = float(input("Enter Y coordinate: "))
        coords = (x_coord, y_coord)
        print(f"Tuple: {data_structures.tuple_demo(coords)}")
    except ValueError:
        print(f"Tuple: {data_structures.tuple_demo()}")

    ids = get_list("\nEnter IDs", int, [])
    if ids:
        print(f"Set: {data_structures.set_demo(ids)}")
    else:
        print(f"Set: {data_structures.set_demo()}")

    try:
        score = int(input('\nEnter starting score: '))
        print(f"Dictionary: {data_structures.dict_demo(username=user_name, score=score)}")
    except ValueError:
        print(f"Dictionary: {data_structures.dict_demo(username=user_name)}")

    print("\n Append & Extend")
    comp_nums = get_list("Enter numbers for append/extend", int, [1, 2, 3, 4, 5])
    print(f"Result: {comprehensions.demonstrate_append_extend(comp_nums)}")

    comp_words = get_list("Enter words to calculate lengths", str, ['python', 'code'])
    print(f"Word lengths: {comprehensions.make_word_lengths(comp_words)}")

    print("\n Error Handling")
    try:
        num = float(input("Enter numerator: "))
        den = float(input("Enter denominator: "))
        error_handling.divide_numbers(num, den)
    except ValueError:
        print("Invalid number.")

    try:
        error_handling.register_age(int(input("\nEnter age to register: ")))
    except ValueError as e:
        print(f"Error: {e}")

    print("\n Iterators & Generators")
    limit = get_int("Enter limit for Fibonacci: ", 5)
    for num in iterators_generators.fibonacci_generator(limit):
        print(num)
