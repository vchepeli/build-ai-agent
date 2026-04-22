from functions.run_python_file import run_python_file


def main():
    # 1. run_python_file("calculator", "main.py")
    print('1. run_python_file("calculator", "main.py")')
    print()
    result = run_python_file("calculator", "main.py")
    print(result)
    print()

    # 2. run_python_file("calculator", "main.py", ["3 + 5"])
    print('2. run_python_file("calculator", "main.py", ["3 + 5"])')
    print()
    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print(result)
    print()

    # 3. run_python_file("calculator", "tests.py")
    print('3. run_python_file("calculator", "tests.py")')
    print()
    result = run_python_file("calculator", "tests.py")
    print(result)
    print()

    # 4. run_python_file("calculator", "../main.py")
    print('4. run_python_file("calculator", "../main.py")')
    print()
    result = run_python_file("calculator", "../main.py")
    print(result)
    print()

    # 5. run_python_file("calculator", "nonexistent.py")
    print('5. run_python_file("calculator", "nonexistent.py")')
    print()
    result = run_python_file("calculator", "nonexistent.py")
    print(result)
    print()

    # 6. run_python_file("calculator", "lorem.txt")
    print('6. run_python_file("calculator", "lorem.txt")')
    print()
    result = run_python_file("calculator", "lorem.txt")
    print(result)
    print()


if __name__ == "__main__":
    main()
