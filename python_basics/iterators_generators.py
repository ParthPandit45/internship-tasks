def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    
    while count < limit:
        yield a 
        a, b = b, a + b
        count += 1

if __name__ == "__main__":
    print("Fibonacci (limit 5):")
    for num in fibonacci_generator(5):
        print(num)
