from datetime import date
from utils import add, subtract, multiply, divide

print(f"Name : Shahria")
print("Date : ", date.today())

try:

    number1 = float(input("Enter the First Number : "))
    number2 = float(input("Enter the Second Number : "))

    print("Addition : ", add(number1, number2))
    print("Subtraction : ",subtract(number1 , number2))
    print("Multiplication :", multiply(number1 , number2))
    print("Division : ", divide(number1, number2))

except ValueError:
    print("Error: Input can not be zero")