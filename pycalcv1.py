import math
import sys

class PyCalcv1:
    def __init__(self):
        self.history = [] # Stores calculation history
        self.memory_val = 0.0
        self.running = True
        self.last_result = None # Stores last result
        self.angle_mode = "degrees"
        
        # Binary operations
        self.binary_ops = {
            "+": (lambda a, b: a + b),
            "-": (lambda a, b: a - b),
            "*": (lambda a, b: a * b),
            "/": self._divide,
            "//": self._floor_divide,
            "**": self._power,
            "%": self._modulus,
        }

        # Unary operations
        self.unary_ops = {
            "sqrt": self._sqrt,
            "log": self._log_base10,
            "tan": self._tangent,
            "sin": lambda a: math.sin(self._to_rad(a)),
            "cos": lambda a: math.cos(self._to_rad(a)),
            "asin": lambda a: self._from_rad(math.asin(a)),
            "acos": lambda a: self._from_rad(math.acos(a)),
            "atan": lambda a: self._from_rad(math.atan(a)),
            "!": self._factorial,
        }
        
        # Constants
        self.constants = {
            "pi": math.pi,
            "e": math.e,
            "tau": math.tau
        }

        # Combine keys for display purposes
        self.all_ops = {**self.binary_ops, **self.unary_ops}

    def _get_valid_number(self, prompt):
        """Prompts user for a number until valid input is received."""
        while True:
            user_input = input(prompt).strip().lower()

            # Check for 'stats'
            if user_input == "stats":
                return "stats"
            
            if user_input == "mode":
                return "mode"

            # Check for 'ans'
            if user_input == "ans":
                if self.last_result is not None:
                    print(f"Last result: {self.last_result}")
                    return self.last_result
                else:
                    print("No previous result available yet.")
                    continue

            if user_input == "help":
                print("Commands: stats, mode, mem, ans, hist")
                continue 

            # Memory function
            if user_input == "mem":
                print(f"Memory Recall: {self.memory_val}")
                return self.memory_val

            # Check for constants
            if user_input in self.constants:
                val = self.constants[user_input]
                print(f"Constant '{user_input}': {val}")
                return val

            # Check for standard input
            try:
                return float(user_input)
            except ValueError:
                print("Error. Invalid input (must be a number, constant, or 'ans').")

    def _display_history(self):
        """Prints calculation history."""
        print("\n--- Calculation History ---")
        if not self.history:
            print("History is empty. Perform a calculation first.")
            return

        for i, entry in enumerate(self.history):
            print(f"[{i + 1}]: {entry}") 
        print("---------------------------\n")

    def _to_rad(self, n):
        """Converts input to radians if mode is degrees."""
        return math.radians(n) if self.angle_mode == "degrees" else n

    def _from_rad(self, n):
        """Converts result back to degrees if mode is degrees."""
        return math.degrees(n) if self.angle_mode == "degrees" else n

    def _toggle_mode(self):
        """Switches between Degrees and Radians."""
        if self.angle_mode == "degrees":
            self.angle_mode = "radians"
        else:
            self.angle_mode = "degrees"
        print(f"Angle mode switched to: {self.angle_mode.upper()}")
    
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
        # Asymptotes (90, 270) in degrees
        check_angle = n1 if self.angle_mode == "degrees" else math.degrees(n1)
    
        if abs((check_angle % 180) - 90) < 1e-9:
            raise ValueError("Tangent undefined at 90, 270...")
         
        return math.tan(self._to_rad(n1))

    def _factorial(self, n1):
        if n1 < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        if not float(n1).is_integer():
            raise ValueError("Factorial is only defined for integers.")
        return math.factorial(int(n1))

    def _run_stats(self):
        print("\n--- Statistics Mode ---")
        raw = input("Enter numbers separated by commas (e.g. 1, 2, 5, 10): ")
        try:
            # Conversion 1, 2 ,3 / 1.0, 2.0, 3.0
            nums = [float(x.strip()) for x in raw.split(",")]
            if not nums: return
            
            mean_val = sum(nums) / len(nums)
            print(f"  > Mean (Average): {mean_val}")
            print(f"  > Max: {max(nums)}")
            print(f"  > Min: {min(nums)}")
            
            # Save history
            self.last_result = mean_val
            self.history.append(f"Stats Mean of {nums} = {mean_val}")
        except ValueError:
            print("Error: Please enter valid numbers separated by commas.")

    # Primary execution
    def run(self):
        print("Launching The Python Calculator... launched!")
        print("===============================================")
        print("//-The Python Calculator-v1-//")
        print("-----------------------------------------------")
        print("(Trigonometry functions expect input in degrees)")
        print("(Type 'mode' to switch to radians)")
        print("===============================================")

        while self.running:
            # Check if 'ans' is available, prompt if so
            ans_prompt = "(Type 'ans' to see last result)" if self.last_result is not None else ""
            
            mode_tag = "[DEG]" if self.angle_mode == "degrees" else "[RAD]"
            num1 = self._get_valid_number(f"\n{mode_tag} Enter first number {ans_prompt}: ")

            if num1 == "stats":
                self._run_stats()
                continue

            if num1 == "mode":
                self._toggle_mode()
                continue
            
            print("Available operations:", " | ".join(self.all_ops.keys()), "| hist | m+ | mc")
            op_symbol = input("Pick an operation (or 'hist'): ").lower().strip()

            if op_symbol == "hist": # Checks for history cmd
                self._display_history()
                continue # Restarts loop

            if op_symbol == "m+":
                if self.last_result is not None:
                    self.memory_val += self.last_result
                    print(f"Added {self.last_result} to memory. (New Memory: {self.memory_val})")
                else:
                    print("No result to add to memory yet.")
                continue # Skip rest of loop

            elif op_symbol == "mc":
                self.memory_val = 0.0
                print("Memory Cleared.")
                continue

            if op_symbol not in self.all_ops:
                print("Invalid operator. Please try again.")
                continue

            num2 = None
            calc_function = None
            calculation_str = "" 

            try:
                # Determine whether unary or binary
                if op_symbol in self.unary_ops:
                    print(f"Selected '{op_symbol}'. No second number needed.")
                    calc_function = self.unary_ops[op_symbol]
                    result = calc_function(num1)
                    calculation_str = f"{op_symbol}({num1})"
                
                elif op_symbol in self.binary_ops:
                    ans_prompt = "(Type 'ans' to use the last result)" if self.last_result is not None else ""
                    num2 = self._get_valid_number(f"Enter the second number {ans_prompt}: ") 
                    if isinstance(num2, str):
                        print(f"Cannot run command '{num2}' mid-calculation. Restarting...")
                        continue
                    calc_function = self.binary_ops[op_symbol]
                    result = calc_function(num1, num2)
                    calculation_str = f"{num1} {op_symbol} {num2}"
                
                result = round(result, 10)
                if result.is_integer():
                    result = int(result)

                print(f"\nResult: {calculation_str} = {result}")
                
                # History tracking
                self.last_result = result
                self.history.append(f"{calculation_str} = {result}")

            except ValueError as e:
                print(f"Math Error: {e}")
            except Exception as e:
                print(f"Unexpected Error: {e}")

            # Exit prompt
            should_continue = input("\nDo you want to continue? (y/n): ")
            if should_continue.lower() != 'y':
                print("Thank you for using //-The Python Calculator-v1-//!")
                self.running = False

if __name__ == "__main__":
    calculator_app = PyCalcv1()
    calculator_app.run()
