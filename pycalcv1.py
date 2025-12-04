import math
import sys

add = lambda n1, n2: n1 + n2
subtract = lambda n1, n2: n1 - n2
multiply = lambda n1, n2: n1 * n2
sine = lambda n1, n2=None: math.sin(math.radians(n1))
cosine = lambda n1, n2=None: math.cos(math.radians(n1))

def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a number.")

def divide(n1, n2):
    if n2 == 0:
        raise ValueError("Unable to divide by zero.")
    return n1 / n2

def power(n1, n2):
    if n1 == 0 and n2 < 0:
        raise ValueError("Zero cannot be raised to a negative power.")
    return n1 ** n2

def modulus(n1, n2):
    if n2 == 0:
        raise ValueError("Unable to perform modulus by zero.")
    return n1 % n2

def floor_divide(n1, n2):
    if n2 == 0:
        raise ValueError("Unable to divide by zero.")
    return n1 // n2
 
def square_root(n1, n2=None): 
    if n1 < 0:
        raise ValueError("Unable to calculate the square root of a negative number.")
    return math.sqrt(n1)

def log_base10(n1, n2=None):
    if n1 <= 0:
        raise ValueError("Logarithm is only defined for positive numbers.")
    return math.log10(n1)

def tangent(n1, n2=None):
    if abs((n1 % 180) - 90) < 1e-9: 
        raise ValueError("Tangent is undefined for 90, 270, etc.")
    return math.tan(math.radians(n1))

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    "//": floor_divide,
    "**": power,     
    "%": modulus,    
    "sqrt": square_root,
    "log": log_base10,
    "sin": sine,
    "cos": cosine,
    "tan": tangent
}

unary_operations = ["sqrt", "log", "sin", "cos", "tan"]

def calculator():
    print("Launching The Python Calculator... launched!")
    print("\n==============================================")
    print("\n/-The Python Calculator-v1-/")
    print("(Trigonometry functions expect input in degrees)")
    print("\n==============================================")

    while True: 
        num1 = get_valid_number("\nEnter the first number: ")

        print("Available operations:", " | ".join(operations.keys()))
             
        op_symbol = input("Pick an operation: ")
        
        if op_symbol not in operations:
            print("Invalid operator. Please try again.")
            continue 

        if op_symbol in unary_operations:
            num2 = None
            print(f"Selected '{op_symbol}'. No second number needed.")
        else:
            num2 = get_valid_number("Enter the second number: ")

        try:
            calc_function = operations[op_symbol]
            result = calc_function(num1, num2)
            
            result = round(result, 10)
            
            if result.is_integer():
                result = int(result)

            if num2 is not None:
                print(f"\nResult: {num1} {op_symbol} {num2} = {result}")
            else:
                print(f"\nResult: {op_symbol}({num1}) = {result}")
                
        except ValueError as e:
            print(f"Math Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")

        should_continue = input("\nDo you want to continue? (y/n): ")
        if should_continue.lower() != 'y':
            print("Thank you for using -The Python Calculator-v1-!")
            break

if __name__ == "__main__":
    calculator()