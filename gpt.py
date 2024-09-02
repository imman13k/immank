def calculate_area_of_rectangle(length, width):
    return length * width

# Example usage:
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
print("Area of the rectangle:", calculate_area_of_rectangle(length, width))

print("......................................")

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Example usage:
celsius = float(input("Enter temperature in Celsius: "))
print("Temperature in Fahrenheit:", celsius_to_fahrenheit(celsius))

print("......................................")

import math

def solve_quadratic_equation(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2*a)
        return (root,)
    else:
        return "No real roots"

# Example usage:
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
roots = solve_quadratic_equation(a, b, c)
print("Roots of the quadratic equation:", roots)

print("......................................")

def find_largest_number(numbers):
    return max(numbers)

# Example usage:
numbers = list(map(float, input("Enter a list of numbers separated by space: ").split()))
print("Largest number:", find_largest_number(numbers))

print("......................................")

def is_palindrome(s):
    return s == s[::-1]

# Example usage:
string = input("Enter a string to check if it is a palindrome: ")
print("Is palindrome:", is_palindrome(string))


print("......................................")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Example usage:
num = int(input("Enter a number to find its factorial: "))
print("Factorial of the number:", factorial(num))

print("......................................")




