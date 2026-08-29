from datetime import date
from utils import add, subtract

print(f"Name : Shahria")
print("Date : ", date.today())

number1 = float(input("Enter the First Number : "))
number2 = float(input("Enter the Second Number : "))

print("Addition : ", add(number1, number2))
print("Subtraction : ",subtract(number1 , number2))
 