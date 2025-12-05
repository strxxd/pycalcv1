import math
import sys

class PyCalcv1:
    def __init__(self):
        self.history = []
        self.memory_val = 0.0
        self.running = True
        self.last_result = None

        # Binary Operations
        self.binary_ops = {
            "+": (lambda a, b: a + b),
            "-": (lambda a, b: a - b),
            "*": (lambda a, b: a * b),
            "/": self._divide,
            "//": self._floor_divide,
            "**": self._power,
            "%": self._modulus,
        }

        # Unary Operations
        self.unary_ops = {
            "sqrt": self._sqrt,
            "log": self._log_base10,
            "sin": (lambda a: math.sin(math.radians(a))),
            "cos": (lambda a: math.cos(math.radians(a))),
            "tan": self._tangent,
        }
        
        # Combine keys for display purposes
        self.all_ops = {**self.binary_ops, **self.unary_ops}

    def _get_valid_number(self, prompt):
        """Prompts user for a number until valid input is received."""
        while True:
            try:
                return float(input(prompt).strip())
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Binary
    def _divide(self, n1, n2):
        if n2 == 0:
            raise ValueError("Unable to divide by zero.")
        return n1 / n2

    def _power(self, n1, n2):
        if n1 == 0 and n2 < 0:
            raise ValueError("Zero cannot be raised to a negative power.")
        return n1 ** n2

    def _modulus(self, n1, n2):
        if n2 == 0:
            raise ValueError("Unable to perform modulus by zero.")
        return n1 % n2

    def _floor_divide(self, n1, n2):
        if n2 == 0:
            raise ValueError("Unable to divide by zero.")
        return n1 // n2

    # Unary
    def _sqrt(self, n1):
        if n1 < 0:
            raise ValueError("Unable to calculate the square root of a negative number.")
        return math.sqrt(n1)

    def _log_base10(self, n1):
        if n1 <= 0:
            raise ValueError("Logarithm is only defined for positive numbers.")
        return math.log10(n1)

    def _tangent(self, n1):
        if abs((n1 % 180) - 90) < 1e-9:
            raise ValueError("Tangent is undefined for 90, 270, etc.")
        return math.tan(math.radians(n1))

    # Primary Execution
    def run(self):
        print("Launching The Python Calculator... launched!")
        print("\n==============================================")
        print("\n/-The Python Calculator-v1-/")
        print("(Trigonometry functions expect input in degrees)")
        print("\n==============================================")

        while self.running:
            num1 = self._get_valid_number("\nEnter the first number: ")

            print("Available operations:", " | ".join(self.all_ops.keys()))
            op_symbol = input("Pick an operation: ")

            if op_symbol not in self.all_ops:
                print("Invalid operator. Please try again.")
                continue

            num2 = None
            calc_function = None

            try:
                # Determine whether unary or binary
                if op_symbol in self.unary_ops:
                    # Unary operations only use one number
                    print(f"Selected '{op_symbol}'. No second number needed.")
                    calc_function = self.unary_ops[op_symbol]
                    result = calc_function(num1)
                
                elif op_symbol in self.binary_ops:
                    # Binary operations require a second number
                    num2 = self._get_valid_number("Enter the second number: ")
                    calc_function = self.binary_ops[op_symbol]
                    result = calc_function(num1, num2)
                
                result = round(result, 10)
                if result.is_integer():
                    result = int(result)

                if num2 is not None:
                    print(f"\nResult: {num1} {op_symbol} {num2} = {result}")
                else:
                    print(f"\nResult: {op_symbol}({num1}) = {result}")
                # History Tracking
                self.last_result = result

            except ValueError as e:
                print(f"Math Error: {e}")
            except Exception as e:
                print(f"Unexpected Error: {e}")

            # Exit Prompt
            should_continue = input("\nDo you want to continue? (y/n): ")
            if should_continue.lower() != 'y':
                print("Thank you for using -The Python Calculator-v1-!")
                self.running = False

if __name__ == "__main__":
    calculator_app = PyCalcv1()
    calculator_app.run()
