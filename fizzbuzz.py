for i in range(1, 101):
    if i % 5 and i % 3:
        print("FizzBuzz")
    elif i % 5:
        print("Buzz")
    elif i % 3:
        print("Fizz")
    else:
        print(i)
