from functions.get_file_content import get_file_content


def main():
    # 1. Test with lorem.txt (should truncate)
    print('1. get_file_content("calculator", "lorem.txt")')
    print()
    result = get_file_content("calculator", "lorem.txt")
    print(f"Length: {len(result)}")
    print(f"Truncated: {'truncated' in result}")
    print()

    # 2. get_file_content("calculator", "main.py")
    print('2. get_file_content("calculator", "main.py")')
    print()
    result = get_file_content("calculator", "main.py")
    print(result)
    print()

    # 3. get_file_content("calculator", "pkg/calculator.py")
    print('3. get_file_content("calculator", "pkg/calculator.py")')
    print()
    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)
    print()

    # 4. get_file_content("calculator", "/bin/cat") - should return error
    print('4. get_file_content("calculator", "/bin/cat")')
    print()
    result = get_file_content("calculator", "/bin/cat")
    print(result)
    print()

    # 5. get_file_content("calculator", "pkg/does_not_exist.py") - should return error
    print('5. get_file_content("calculator", "pkg/does_not_exist.py")')
    print()
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result)
    print()


if __name__ == "__main__":
    main()
