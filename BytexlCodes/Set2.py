# 1. A program that models a bank account, with classes for the account, the customer,
# and the bank.
# 2. A program that simulates a school management system, with classes for the
# students, the teachers, and the courses.
# 3. A program that reads a text file and counts the number of words in it.
# 4. A program that reads a CSV file and calculates the average of the values in a specified column.
# 5. A program that reads an Excel file and prints the data in a tabular format.


class Bank:
    def __init__(self):
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

class Customer:
    def __init__(self, name, account):
        self.name = name
        self.account = account

class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

# Usage
bank = Bank()
customer1 = Customer("John", Account(1000))
bank.add_customer(customer1)
customer1.account.deposit(500)
customer1.account.withdraw(200)
print(customer1.account.balance)




class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

class Course:
    def __init__(self, name, teacher, students):
        self.name = name
        self.teacher = teacher
        self.students = students

# Usage
student1 = Student("Alice", 10)
teacher1 = Teacher("Mr. Smith", "Math")
course1 = Course("Mathematics", teacher1, [student1])




def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)

# Usage
word_count = count_words("example.txt")
print("Word count:", word_count)




import csv

def calculate_average(filename, column_index):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header if exists
        total = 0
        count = 0
        for row in reader:
            total += float(row[column_index])
            count += 1
        if count == 0:
            return 0
        return total / count

# Usage
average = calculate_average("data.csv", 1)  # Assuming the column index is 1
print("Average:", average)




import pandas as pd

def print_excel_data(filename):
    df = pd.read_excel(filename)
    print(df)

# Usage
print_excel_data("data.xlsx")


