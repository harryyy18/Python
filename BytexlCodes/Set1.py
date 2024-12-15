# 1. A program that converts temperatures from Fahrenheit to Celsius and vice versa.
# 2. A program that calculates the area and perimeter of a rectangle.
# 3. A program that generates a random password of a specified length.
# 4. A program that calculates the average of a list of numbers.
# 5. A program that checks if a given year is a leap year.
# 6. A program that calculates the factorial of a number.
# 7. A program that checks if a given string is a palindrome.
# 8. A program that sorts a list of numbers in ascending or descending order.
# 9. A program that generates a multiplication table for a given number.
# 10. A program that converts a given number from one base to another.

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

# Test
f_temp = 32
c_temp = 0
print(f"{f_temp} Fahrenheit = {fahrenheit_to_celsius(f_temp)} Celsius")
print(f"{c_temp} Celsius = {celsius_to_fahrenheit(c_temp)} Fahrenheit")





def rectangle_area(length, width):
    return length * width

def rectangle_perimeter(length, width):
    return 2 * (length + width)

# Test
length = 5
width = 3
print(f"Area: {rectangle_area(length, width)}, Perimeter: {rectangle_perimeter(length, width)}")




import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Test
password_length = 10
print("Generated Password:", generate_password(password_length))




def calculate_average(numbers):
    return sum(numbers) / len(numbers)

# Test
numbers = [1, 2, 3, 4,  5] 
print("Average:", calculate_average(numbers))




def is_leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return "Perfect Leap Year"
            elif:
                return "Century Leap Year"
        elif:
            return "Simple Leap Year"
        

# Test
year = 2024
print(f"{year} is a leap year:", is_leap_year(year))





def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Test
number = 5
print("Factorial:", factorial(number))





def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

# Test
string = "racecar"
print(f'"{string}" is a palindrome:', is_palindrome(string))




def sort_numbers(numbers, ascending=True):
    return sorted(numbers) if ascending else sorted(numbers, reverse=True)

# Test
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print("Ascending Order:", sort_numbers(numbers))
print("Descending Order:", sort_numbers(numbers, ascending=False))




def generate_multiplication_table(number):
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Test
number = 7
generate_multiplication_table(number)




def convert_base(number, from_base, to_base):
    if from_base == to_base:
        return str(number)
    else:
        return str(int(str(number), from_base)).upper() if to_base == 10 else format(int(str(number), from_base), f'X').upper()

# Test
number = '1F'
from_base = 16
to_base = 10
print(f"Converted from base {from_base} to base {to_base}: {convert_base(number, from_base, to_base)}")
