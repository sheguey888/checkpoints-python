import math
import operator


class Calculator:
    def __init__(self):
        """Initializes the calculator with basic arithmetic operations."""
        self.operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,
        }

    def add_operation(self, symbol, func):
        """Adds a new operation symbol and its associated function."""
        self.operations[symbol] = func

    def calculate(self, num1, symbol, num2=None):
        """
        Validates inputs and evaluates the expression using the registered operations.
        Raises TypeError or ValueError on invalid inputs.
        """
        # Validate that the first number is numeric (int or float, not bool)
        if not isinstance(num1, (int, float)) or isinstance(num1, bool):
            msg = f"TypeError: First operand '{num1}' must be a valid number."
            print(msg)
            raise TypeError(msg)

        # Validate that the operation symbol exists in the dictionary
        if symbol not in self.operations:
            msg = f"ValueError: '{symbol}' is not a recognized operation."
            print(msg)
            raise ValueError(msg)

        # If a second argument is provided, validate it as well
        if num2 is not None:
            if not isinstance(num2, (int, float)) or isinstance(num2, bool):
                msg = f"TypeError: Second operand '{num2}' must be a valid number."
                print(msg)
                raise TypeError(msg)

            # Check division by zero
            if symbol == "/" and num2 == 0:
                msg = "ZeroDivisionError: Division by zero is not allowed."
                print(msg)
                raise ZeroDivisionError(msg)

            return self.operations[symbol](num1, num2)

        # For unary operations (e.g., square root) where num2 is omitted or unused
        return self.operations[symbol](num1)


# Advanced operation functions using the math library
def exponent(base, power):
    return math.pow(base, power)


def square_root(x, _=None):
    """Calculates square root; second operand is ignored if provided."""
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(x)


def logarithm(x, base=math.e):
    """Calculates log of x with given base (defaults to natural log)."""
    if x <= 0:
        raise ValueError("Logarithm argument must be strictly positive.")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1.")
    return math.log(x, base)


def parse_number(prompt_text):
    """Helper to convert string input into float/int for isinstance checks."""
    val = input(prompt_text).strip()
    try:
        val_float = float(val)
        return int(val_float) if val_float.is_integer() else val_float
    except ValueError:
        return val  # Return raw string to trigger Calculator's isinstance error check


def main():
    calc = Calculator()

    # Register advanced operations
    calc.add_operation("^", exponent)
    calc.add_operation("sqrt", square_root)
    calc.add_operation("log", logarithm)

    print("--- Welcome to the Calculator ---")
    print("Available operations:", ", ".join(calc.operations.keys()))
    print("Note: For 'sqrt', enter 0 or press enter for the second number.\n")

    while True:
        try:
            first_input = parse_number("Enter the first number: ")
            symbol = input("Enter the operation symbol: ").strip()

            if symbol == "sqrt":
                second_input = None
            else:
                second_input = parse_number("Enter the second number (base for log, exponent for ^): ")

            result = calc.calculate(first_input, symbol, second_input)
            print(f"Result: {result}\n")

        except Exception as e:
            print(f"Calculation failed: {e}\n")

        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again in ("no", "n", "exit", "quit"):
            print("Exiting calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()
