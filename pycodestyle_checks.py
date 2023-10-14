#!/usr/bin/python3


def calculate_square(n):
    """Calculate the square of a number."""
    return n**2


def calculate_sum(a, b):
    """Calculate the sum of two numbers."""
    return a + b


def is_even(num):
    """Check if a number is even."""
    return num % 2 == 0


def print_greeting(name):
    """Print a greeting message."""
    print(f"Hello, {name}!")


def main():
    """Main function to demonstrate the functions."""
    num1 = 5
    num2 = 7
    square_result = calculate_square(num1)
    sum_result = calculate_sum(num1, num2)

    print(f"The square of {num1} is: {square_result}")
    print(f"The sum of {num1} and {num2} is: {sum_result}")

    if is_even(num1):
        print(f"{num1} is even.")
    else:
        print(f"{num1} is odd.")

    print_greeting("Alice")
    print_greeting("Bob")


if __name__ == '__main__':
    main()
