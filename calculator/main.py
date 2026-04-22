import sys
from pkg.calculator import Calculator
from pkg.render import format_calc_result


def main():
    calculator = Calculator()

    if len(sys.argv) < 2:
        print("Calculator Tool")
        print(f"Usage: python main.py <expression>")
        print(f'Example: python main.py "2 + 5"')
        return

    expression = " ".join(sys.argv[1:])
    try:
        result = calculator.evaluate(expression)
        if result is not None:
            to_print = format_calc_result(expression, result)
            print(to_print)
        else:
            print("Error: Expression is empty or contains only whitespace.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
